import re

import requests
import os
import time
import json

import xlwt

cookie = "buvid3=63B1C902-3DD5-CD46-85D8-9A69679BC65665004infoc; CURRENT_FNVAL=80; blackside_state=1; sid=6aaqymp9; rpdid=|(u)mJ~Rlll~0J'uYkR||uuYm; fingerprint=33bf6967b63128e997c2ee0e3659a990; buvid_fp=63B1C902-3DD5-CD46-85D8-9A69679BC65665004infoc; buvid_fp_plain=63B1C902-3DD5-CD46-85D8-9A69679BC65665004infoc"
file_dir = "F:/summer_project/commentFiles/"
dir_xls = "F:/summer_project/commentFiles/savename.xls"
content_api = 'https://api.bilibili.com/x/v2/reply/main?jsonp=jsonp&type=1&mode=3&plat=1'
# 1:评论(楼层);2:最新评论(时间);3:热门评论(热度)
comment_mode = 3
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
        'cookie': cookie  # 在请求头里复制自己的cookie
    }

# bv转av，输入如BVxxxxxxxxx，输出一串数字av号
def bv2av(bv:str)->str:
    response = requests.get(url='https://api.bilibili.com/x/web-interface/view',params={'bvid':bv},headers=headers)
    av = str(response.json()['data']['aid'])
    return av

def scrape_url(url:str)->dict:
    if '/' in url or '?' in url:
        # 分解链接
        bv = url.split('/')[-1].split('?')[0]
    av = bv2av(bv)
    pattern = re.compile(r'{.*}') # 去除外层的jquery括号，让数据能被json解析

    params={'jsonp':'jsonp','type':1,'oid':av,'mode':3,'plat':1} # 构造参数
    headers['referer'] = url # 修改referer为当前视频url
    next = 0 # 初始值为0

    comment_list=[]
    for k in range(0,10):
        params['next'] = next
        response = requests.get(url=content_api,params=params,headers=headers)
        json_text = pattern.search(response.text).group(0)
        is_end = json.loads(json_text)['data']['cursor']['is_end']
        if is_end: # is_end为True就break
            break
        replies_info = json.loads(json_text)['data']['replies']

        for i in replies_info:
            res = {'like': i['like'], 'mid': i['member']['mid'], 'uname': i['member']['uname'],'massage':i['content']['message']}
            comment_list.append(res)
        if next!=0: # 坑爹的参数，经过实践发现第一组next为0，第二组next为2，之后依次+1递增，next设为0和1返回数据一样。为了和实际保持一样，出此下策
            next+=1
        else:
            next+=2
    print(len(comment_list))
    return comment_list

# scrape_url('https://www.bilibili.com/video/BV11S4y1H7K5?vd_source=b4ae041177452820e3cba3a0a491efbb')
