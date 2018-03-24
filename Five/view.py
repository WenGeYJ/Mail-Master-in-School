# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators import csrf
from django.contrib import auth
from django.contrib.auth.models import User
from main.models import Book
from main.models import StudentUser
from main.models import SubscribedBook
from main.models import FavoredBook
from main.models import ArrivalMessage
from main.models import Temp
import json
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=50)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'home.html')
    else:
        if request.user.username == 'manager':
            return render(request, 'home2.html')
        else:
            return render(request, 'homelogged.html', {'username': request.user.username})


def regist(request):
    type=-1
    if request.method == 'POST':
        usename = request.POST.get('u')
        password = request.POST.get('p')
        password2 = request.POST.get('pp')
        emai = request.POST.get('e')
        phonenumber=request.POST.get('phonenumber')
        studentclass=request.POST.get('sc')
        studentnumber=request.POST.get('sn')
        type = 0
        if phonenumber=='':
            phonenumber='0'
        if studentclass=='':
            studentclass='0'
        if studentnumber=='':
            studentnumber='0'
        if usename == '':  # 用户名为空
            type += 1
            return render(request, 'regist.html', {'type': type})
        if password == '':  # 密码为空
            type += 2
            return render(request, 'regist.html', {'type': type})
        if User.objects.filter(username=usename):  # 用户名已存在
            type += 4
            return render(request, 'regist.html', {'type': type})
        if password != password2:  # 密码不同
            type += 8
            return render(request, 'regist.html', {'type': type})
        if '@' not in emai:  # email格式有误
            type += 16
            return render(request, 'regist.html', {'type': type})
        if User.objects.filter(email=emai):  # email已存在
            type += 32
            return render(request, 'regist.html', {'type': type})
        if type == 0:
            user = User.objects.create_user(username=usename,password=password,email=emai)
            studentuser=StudentUser(userName=usename, mailBox=emai, name=usename, phoneNumber=phonenumber, studentClass
                                    =studentclass, studentNumber=studentnumber)
            studentuser.save()
            user.save()
            return render(request, 'home.html')
        else:
            return render(request, 'regist.html', {'type':type})
    return render(request, 'regist.html', {'type': type})


def login(request):
    type = -1
    if request.method == 'POST':
        type+=1
        usename = request.POST.get('u')
        pasword = request.POST.get('p')

        user = auth.authenticate(username=usename, password=pasword)
        if User.objects.filter(username=usename):
            type += 1
        if user is not None and user.is_active:
            auth.login(request, user)
            if usename == "manager":
                return render(request, 'home2.html')
            return render(request, 'homelogged.html', {'username': usename})
        else:
            return render(request,'login.html', {'type': type})
    return render(request,'login.html', {'type': type})


def checkinfo(request):
    if not request.user.is_authenticated():
        return render(request,'home.html')
    else:
        studentuser=StudentUser.objects.filter(userName=request.user.username)[0]
        return render(request, 'personalinfo.html', {'sc': studentuser.studentClass, 'sn': studentuser.studentNumber,
            'username': request.user.username, 'email':studentuser.mailBox,
                                                     'name': studentuser.name, 'pn': studentuser.phoneNumber})


def ShowBook(request):
    if not request.user.is_authenticated():
        return render(request,'home.html')
    if request.method == 'POST':
        num = request.POST.get('key')
        nfbook = FavoredBook(userName = request.user.username, bookID=num)
        nfbook.save()
    bookList = Book.objects.all()
    tmp = []
    tmp2 = []
    for i in range(5):
        tem=[]
        tem.append(bookList[i].bookName)
        tem.append(bookList[i].mailNumber)
        tem.append(bookList[i].cBussiness)
        tem.append(bookList[i].pricePerYear)
        tem.append(bookList[i].pictureUrl)
        tmp2.append(tem)
    for i in bookList:
        tem=[]
        tem.append(i.bookName)
        tem.append(i.mailNumber)
        tem.append(i.cBussiness)
        tem.append(i.pricePerYear)
        tem.append(i.pictureUrl)
        tmp.append(tem)
    lenth = len(tmp)
    books = FavoredBook.objects.filter(userName=request.user.username)
    temp = []
    for i in books:
        t1 = []
        t1.append(i.bookID-1)
        temp.append(t1)
    temp.sort()
    return render(request, 'ShowBook.html', {'bookListf': json.dumps(tmp2), 'bookList': json.dumps(tmp), 'maxnum': lenth, 'favor': json.dumps(temp)})


def ShowSubscribedBook(request):
    if not request.user.is_authenticated():
        return render(request, 'home.html')
    stu = StudentUser.objects.filter(userName = request.user.username)[0]
    tmpList = SubscribedBook.objects.filter(userName=stu.studentClass)
    temp = []
    subscribedBookList = []
    for item in tmpList:
        temp.append(Book.objects.get(bookID=item.bookID))
    for i in temp:
        tmp = []
        tmp.append(i.bookName)
        tmp.append(i.mailNumber)
        tmp.append(i.cBussiness)
        tmp.append(i.pricePerYear)
        subscribedBookList.append(tmp)
    return render(request, 'SubscripBook.html', {'subscribedBookList': subscribedBookList})


def ShowFavoredBook(request):
    if not request.user.is_authenticated():
        return render(request,'home.html')
    tmpList = FavoredBook.objects.filter(userID=request.user.id)
    favoredBookList = []
    for item in tmpList:
        favoredBookList.append(Book.objects.get(bookID=item.bookID))
    return render(request, 'ShowFavoredBook.html', {'favoredBookList': favoredBookList})


def ShowArrivalMessage(request):
    if not request.user.is_authenticated():
        return render(request,'home.html')
    student=StudentUser.objects.filter(userName=request.user.username)[0]
    tmpList = ArrivalMessage.objects.filter(classID=student.studentClass)
    arrivalMessageList = []
    for item in tmpList:
        tmp = []
        tmp.append(item.time)
        bookInfo = Book.objects.filter(bookID=item.bookID)
        for i in bookInfo:
            tmp.append(i.bookName)
            tmp.append(i.mailNumber)
        arrivalMessageList.append(tmp)
    return render(request, 'BookArrival.html', {'arrivalMessageList': arrivalMessageList})

def showbooklist(request):
    if not request.user.is_authenticated():
        return render(request,'home.html')
    stu = StudentUser.objects.filter(userName=request.user.username)[0]
    stu = stu.studentClass
    return render(request, 'bookform.html', {'stu': stu})


def myfavor(request):
    if not request.user.is_authenticated():
        return render(request,'home.html')
    if request.method == 'POST':
        num = request.POST.get('key')
        o = FavoredBook.objects.filter(userName=request.user.username, bookID = num)[0]
        o.delete()
    books = FavoredBook.objects.filter(userName=request.user.username)
    temp = []
    for i in books:
        tmp = []
        book = Book.objects.filter(bookID=i.bookID)[0]
        tmp.append(book.bookName)
        tmp.append(book.mailNumber)
        tmp.append(book.cBussiness)
        tmp.append(book.pricePerYear)
        temp.append(tmp)
    return render(request, 'favoredbook.html', {'books': temp})


def logout(request):
    if not request.user.is_authenticated():
        return render(request,'home.html')
    auth.logout(request)
    return render(request, "home.html")

def abc(request):
    return render(request, 'class.html')


def searchclass(request):
    return render(request, 'class.html')

books=[]
classid='0'
def notify(request):
    if not request.user.is_authenticated():
        return render(request,'home.html')
    if request.user.username!="manager":
        return HttpResponse("没有访问权限")
    if request.method=='POST':
        keyword=request.POST.get('keyword')
        classidtmp=Temp(classid=keyword)
        classidtmp.save()
        classid=keyword
        books=SubscribedBook.objects.filter(userName=keyword)
        tmp=[]
        for i in books:
            tmp.append(Book.objects.filter(bookID=i.bookID)[0].bookName)
        lenth = len(books)
        return render(request, 'SendInfo.html', {'maxnum':lenth, 'bookname': json.dumps(tmp), 'class0': classid})

def regiestbooks(request):
    if not request.user.is_authenticated():
        return render(request,'home.html')
    if request.user.username!="manager":
        return HttpResponse("没有访问权限")
    classidtmp = Temp.objects.all()[0]
    classid = classidtmp.classid
    books = SubscribedBook.objects.filter(userName=classid)
    tmp = []
    for i in books:
        tmp.append(i.bookID)
        #tmp.append(Book.objects.filter(bookID=i.bookID)[0].bookName)
    check_box_list = request.POST.getlist("check")
    for j in check_box_list:
        arrivalmessage=ArrivalMessage(bookID=tmp[int(j)], classID=classid)
        arrivalmessage.save()
    return render(request, 'class.html')


def modifysubscribe(request):
    if not request.user.is_authenticated():
        return render(request,'home.html')
    if request.user.username!="manager":
        return HttpResponse("没有访问权限")
    if request.method == 'POST':
        classid = request.POST.get('classid')
        num = request.POST.get('num')
        if classid == '' or num == '':
            return render(request, 'modifysubscribe.html')
        book = Book.objects.filter(mailNumber=num)[0]
        num = book.bookID
        print (1, classid, num)
        newbook = SubscribedBook(bookID=num, userName=classid)
        newbook.save()
    return render(request, 'modifysubscribe.html')


def modifypersonalinfo(request):
    u = StudentUser.objects.get(userName=request.user.username)
    if request.method == 'POST':
        phone = request.POST.get('phonenumber')
        email = request.POST.get('e')
        if email != '' :
            if '@' in email:
                u.mailBox = email
        if phone != '':
            u.phoneNumber = phone
        u.save()
        return render(request, 'personalinfo.html', {'sc': u.studentClass, 'sn': u.studentNumber,
            'username': request.user.username, 'email': u.mailBox,
                                                     'name': u.name, 'pn': u.phoneNumber})
    return render(request, "personalmodi.html", {'username': u.userName, 'name': u.name, 'pn': u.phoneNumber,
                                                 'email': u.mailBox, 'sc': u.studentClass, 'sn': u.studentNumber})