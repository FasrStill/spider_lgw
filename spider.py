# -*-coding:utf-8-*-
from multiprocessing import Pool
from urllib.parse import urlencode
from openpyxl import Workbook
import requests
import os


def get_index_page(pn):
    data = {
        'city': '北京',
        'needAddtionalResult': 'false'
    }
    data2 = {
        'first': 'false',
        'pn': pn,
        'kd': 'python爬虫工程师'
    }
    url = 'https://www.lagou.com/jobs/positionAjax.json?' + urlencode(data)
    json = requests.post(url, data2).json()
    list_con = json['content']['positionResult']['result']
    content_list = []
    for content in list_con:
        contents = []
        contents.append(content['companyFullName'])
        contents.append(content['companySize'])
        contents.append(content['createTime'])
        contents.append(content['district'])
        contents.append(content['education'])
        contents.append(content['financeStage'])
        contents.append(content['firstType'])
        content_list.append(contents)
    return content_list


def save_content(content):
    wb = Workbook()
    ws = wb.active
    ws.title = 'python爬虫工程师'
    for row in content:
        ws.append(row)
    wb.save('职位信息1.xlsx')


def main(pn):
    content = get_index_page(pn)
    save_content(content)

if __name__ == '__main__':
    groups = [x for x in range(1, 10)]
    pool = Pool()
    pool.map(main, groups)