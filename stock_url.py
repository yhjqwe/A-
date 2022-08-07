# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 19:51:13 2022

@author: yhj
"""

import requests

#url = "http://emweb.securities.eastmoney.com/NewFinanceAnalysis/ZYZBAjaxNew?type=0&code=SH603233"
url = "http://emweb.securities.eastmoney.com/NewFinanceAnalysis/ZYZBAjaxNew?type=0&code="

payload={}
headers = {
  'Accept': '*/*',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Connection': 'keep-alive',
  'Cookie': 'qgqp_b_id=7d61021f429c4be11b425804d272a4f4; HAList=ty-114-lh2209-%u751F%u732A2209; ct=Y-mMKFXvCNGF_JP5uOegCXDuEqv5O2qWExbJfsnNydN38eGJ7W4zRiTe42kyWG4Z32wiZjSdo9ICACSab_gVbySfJi4ae2EcmdAR4HMvjcQ0tJVg0ZruIovpr5y8f_GmOKen75dMXJLDh52xV-51y7azxRdPqp6MkBglp1jY_8U; ut=FobyicMgeV6hWLWpPMBgr20zqXrxBpG-QetTd9AeUSynHux6wb0NLF5qEb-J7AQbyq_a0juA6I-tIh3UIGINB3Mo3jF2piLMCBEwr3QYtGJCa9SYXm0MMuC0tYqrpwAO0X_ZRVNf1RmslHRb1euxoAgMKpP0gixdocsr150gpZ2JqWjSewwSgvaDftUXkP0h-ThrHdOa6eLVLm6Ie2U6Qa9n1N6Q54ZTI3A6uki6DLdd3087GWEy9xy2JVSxcTAjNcD9kFsf_CelCQmwhAV8jhmNP8LScYR3OulaL9SvV-tNT9KkjzwvoUKyzgLmeAaFe9l8ygClIVo; uidal=1615316182094850%e6%b0%a7%e5%8c%96%e5%89%821234; sid=162856060; vtpst=%7c; st_si=66127078206913; st_asi=delete; Hm_lvt_f5b8577eb864c9edb45975f456f5dc27=1659786289; Hm_lpvt_f5b8577eb864c9edb45975f456f5dc27=1659786289; st_pvi=22578720146374; st_sp=2022-06-06%2010%3A58%3A50; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=2; st_psi=20220806194448533-113301310291-9126716511',
  'Referer': 'http://emweb.securities.eastmoney.com/NewFinanceAnalysis/Index?type=web&code=sh603233',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest'
}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)
