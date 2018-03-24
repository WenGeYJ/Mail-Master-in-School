#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import os
# 打开数据库连接
db = MySQLdb.connect("localhost","root","12345678","test")
cursor = db.cursor()
count = 0
os.chdir('information')
path1 = os.getcwd()
s1 = os.listdir(path1)
for i in s1:
    if i[0] == '.':
        s1.remove(i)
for i in s1:
    path2 = path1+'/'+i
    s2 = os.listdir(path2)
    for j in s2:
        if j[0] == '.':
            s2.remove(j)
    for j in s2:
        path3 = path2+'/'+j
        s3 = os.listdir(path3)
        for k in s3:
            if k[0] == '.':
                s3.remove(k)
        for k in s3:
            path4 = path3+'/'+k
            s4=os.listdir(path4)
            for l in s4:
                count += 1
                info = []
                name = path4+'/'+l
                #print name
                file_object = open(name)
                lineList = file_object.readlines()
                for lineNum in range(10):
                    if lineNum != 2:
                        if lineNum in range(6, 10):
                            lineList[lineNum] = lineList[lineNum][15:]
                        if lineNum in range(3, 6):
                            if lineList[lineNum]=='暂无\n':
                                lineList[lineNum] = '-1\n'
                            else:
                                lineList[lineNum] = lineList[lineNum][:len(lineList[lineNum])-3]
                        info.append(lineList[lineNum][:len(lineList[lineNum])-1])
                introduction = ' '
                for lineNum in range(11, len(lineList)):
                    introduction+=lineList[lineNum][:len(lineList[lineNum])-1]
                introduction=introduction.replace('\r', '')
                introduction=introduction.replace(r"\\'", '\"')
                sql = """INSERT INTO main_book(id, bookID, bookName, pictureUrl, pricePerMonth, priceHalfYear, pricePerYear, 
                cBussiness, standNumber, mailNumber, bookType, bookKind1, bookKind2, bookKind3, introduction) VALUES
                (NULL, %(bookID)d, '%(bookName)s', '%(pictureUrl)s', %(pricePerMonth)f, %(priceHalfYear)f, %(pricePerYear)f, 
                '%(cBussiness)s', '%(standNumber)s', '%(mailNumber)s', '%(bookType)s', '%(bookKind1)s', '%(bookKind2)s', 
                '%(bookKind3)s', '%(introduction)s')"""%{'bookID': count, 'bookName': info[0], 'pictureUrl': info[1],
                'pricePerMonth': float(info[2]), 'priceHalfYear': float(info[3]), 'pricePerYear': float(info[4]), 'cBussiness':
                info[5], 'standNumber': info[6], 'mailNumber': info[7], 'bookType': info[8], 'bookKind1': i, 'bookKind2':
                j, 'bookKind3': k, 'introduction': introduction}
                try:
                    cursor.execute(sql)
                    db.commit()
                except:
                    print sql
                    db.rollback()
db.close()