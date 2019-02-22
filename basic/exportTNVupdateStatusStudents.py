#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pymongo import MongoClient
import xlwt
import json

APP_KEY = 'df6bda1a157d49cea82447c3e925dd6d'


def combine(item):
    if "requestParam" in item.keys():
        request_param = json.loads(item['requestParam'])
        return {
            'number': request_param['number'],
            'realName': request_param['realName'],
            'idCard': request_param['idCard'],
            'verifyResult': request_param['verifyResult'],
            'createTime': item['createTime']
        }
    else:
        return {
            'number': item['number'],
            'realName': item['realName'],
            'idCard': item['idCard'],
            'verifyResult': item['verifyResult'],
            'createTime': item['createTime']
        }


def save_ret_to_excel(out_file, map_obj):
    xlwt.Workbook()
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('My Worksheet')
    worksheet.write(0, 0, 'number')
    worksheet.write(0, 1, 'readName')
    worksheet.write(0, 2, 'idCard')
    worksheet.write(0, 3, 'verifyResult')
    worksheet.write(0, 4, 'createTime')

    i = 1
    for o in map_obj:
        print(o)
        worksheet.write(i, 0, o['number'])
        worksheet.write(i, 1, o['realName'])
        worksheet.write(i, 2, o['idCard'])
        worksheet.write(i, 3, o['verifyResult'])
        worksheet.write(i, 4, o['createTime'])
        i += 1
        print(i)
    workbook.save(out_file)


if __name__ == '__main__':
    conn = MongoClient('10.100.136.39', 27017)
    #conn = MongoClient('10.100.136.39', 27017)
    db = conn.logdb
    collection = db.apptoolservocelog
    li = collection.find({'requestPath': '/mobile/modifyVerifyResult', 'errorMessage': '修改成功', 'appKey': APP_KEY})
    ll = map(combine, li)
    out = 'D:/手工实名认证.xls'
    save_ret_to_excel(out, ll)
    print("end!!")