# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 23:20:46 2022

@author: yhj
"""

import requests
import time 
import re 

payload={}
headers = {
  'Accept': '*/*',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cookie': 'qgqp_b_id=7d61021f429c4be11b425804d272a4f4; ct=Y-mMKFXvCNGF_JP5uOegCXDuEqv5O2qWExbJfsnNydN38eGJ7W4zRiTe42kyWG4Z32wiZjSdo9ICACSab_gVbySfJi4ae2EcmdAR4HMvjcQ0tJVg0ZruIovpr5y8f_GmOKen75dMXJLDh52xV-51y7azxRdPqp6MkBglp1jY_8U; ut=FobyicMgeV6hWLWpPMBgr20zqXrxBpG-QetTd9AeUSynHux6wb0NLF5qEb-J7AQbyq_a0juA6I-tIh3UIGINB3Mo3jF2piLMCBEwr3QYtGJCa9SYXm0MMuC0tYqrpwAO0X_ZRVNf1RmslHRb1euxoAgMKpP0gixdocsr150gpZ2JqWjSewwSgvaDftUXkP0h-ThrHdOa6eLVLm6Ie2U6Qa9n1N6Q54ZTI3A6uki6DLdd3087GWEy9xy2JVSxcTAjNcD9kFsf_CelCQmwhAV8jhmNP8LScYR3OulaL9SvV-tNT9KkjzwvoUKyzgLmeAaFe9l8ygClIVo; uidal=1615316182094850%e6%b0%a7%e5%8c%96%e5%89%821234; sid=162856060; vtpst=%7c; st_si=85700860196967; st_asi=delete; HAList=ty-0-301095-N%u5E7F%u7ACB%u5FAE%2Cty-0-300059-%u4E1C%u65B9%u8D22%u5BCC%2Cty-114-lh2209-%u751F%u732A2209; st_pvi=22578720146374; st_sp=2022-06-06%2010%3A58%3A50; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=10; st_psi=20220806231825729-113200301321-4672187498',
  'Proxy-Connection': 'keep-alive',
  'Referer': 'http://quote.eastmoney.com/',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
stock_list_SH=[]
f=open('C:/Users\yhj\.spyder-py3\stock_spider/SH_list.txt','w')
for i in range(1,112):
    #f=open('C:/Users\yhj\.spyder-py3\stock_spider/SH_list.txt','w')
    url = "http://60.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124032804641106756227_1659799040396&pn="+str(i)+"&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=1615316182094850|0|0|0|web&fid=f3&fs=m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1659799040427"
    response = requests.request("GET", url, headers=headers, data=payload)
    res=response.text
    #print(response.text)
    pattern=re.compile(r'"f12":"(\d+)"',re.S)
    items=re.findall(pattern, res)
    #print(items)
    time.sleep(1)
    for i in items:
        stock_list_SH.append('SH'+i)
        print(i)

        f.write(str('SH'+i+','))
        f.write('\n')
f.close()
print(stock_list_SH)

stock_list_SZ=[]
f=open('C:/Users\yhj\.spyder-py3\stock_spider/SZ_list.txt','w')
for i in  range(1,140):
    url = "http://27.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124012264056286345393_1659860370117&pn="+str(i)+"&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=1615316182094850|0|0|0|web&fid=f3&fs=m:0+t:6,m:0+t:80&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1659860370123"
    response = requests.request("GET", url, headers=headers, data=payload)
    res=response.text
    #print(response.text)
    pattern=re.compile(r'"f12":"(\d+)"',re.S)
    items=re.findall(pattern, res)
    #print(items)
    time.sleep(1)
    for i in items:
        stock_list_SZ.append('SZ'+i)
        print(i)

        f.write(str('SZ'+i+','))
        f.write('\n')
f.close()
       
print(stock_list_SZ)

stock_list=stock_list_SH+stock_list_SZ
print(stock_list)



