# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 19:36:50 2022

@author: yhj
"""

import requests
import stock_url
import re
import pandas as pd 
import stock_index
#import time
def request_data(stock_list):
    url=stock_url.url+str(stock_list)
    print(url)
    headers=stock_url.headers
    res=requests.get(url,headers=headers)
    if res.status_code==200:
        return res.text
    else:
        print("Can't enter")
        return None
def parse_html(html):
    final_item=[]
    items_eps_final=[]
    items_date_final=[]
    items_bps_final=[]
    #ncfs means Cash Flow Per Share
    items_ncfps_final=[]
    #yoygotor means Year On Year Growth Of Total Operating Revenue
    items_yoygotor_final=[]
    #yoygokfnp means "扣非净利润同比增长"
    items_yoygokfnp_final=[]
    items_roe_final=[]
    #rogp means Rate Of Gross Profit
    items_rogp_final=[]
    #npr means Net Profit Ratio
    items_npr_final=[]
    #rolta means Ratio Of Liabilities To Assets
    items_rolta_final=[]
    #tat means Total Assets Turnover
    items_tat_final=[]
    #it means Inventory Turnover
    items_it_final=[]
    #troar means Turnover rate of accounts receivable
    items_troar_final=[]
    
    #pattern_eps=re.compile(r'"EPSJB" : ((\-)?\d+(\.\d+)?),',re.S)
    pattern_eps=re.compile(r'"EPSJB" : (\S+),',re.S)
    #pattern_date=re.compile(r'"REPORT_DATE" : "(([0-9]{4})-([0-9]{2})-([0-9]{2}))',re.S)
    pattern_date=re.compile(r'"REPORT_DATE" : "(([0-9]{4})-([0-9]{2})-([0-9]{2}))',re.S)
    #pattern_bps=re.compile(r'"BPS" : ((\-)?\d+(\.\d+)?)',re.S)
    pattern_bps=re.compile(r'"BPS" : (\S+),',re.S)
    #pattern_ncfps=re.compile(r'"MGJYXJJE" : ((\-)?\d+(\.\d+)?),',re.S)
    pattern_ncfps=re.compile(r'"MGJYXJJE" : (\S+),',re.S)
    #pattern_yoygotor=re.compile(r'"TOTALOPERATEREVETZ" : ((\-)?\d+(\.\d+)?),',re.S)
    pattern_yoygotor=re.compile(r'"TOTALOPERATEREVETZ" : (\S+),',re.S)
    #pattern_yoygokfnp=re.compile(r'"KCFJCXSYJLRTZ" : ((\-)?\d+(\.\d+)?),',re.S)
    pattern_yoygokfnp=re.compile(r'"KCFJCXSYJLRTZ" : (\S+),',re.S)
    #pattern_roe=re.compile(r'"ROEJQ" : ((\-)?\d+(\.\d+)?),',re.S)
    pattern_roe=re.compile(r'"ROEJQ" : (\S+),',re.S)
    #pattern_rogp=re.compile(r'"XSMLL" : ((\-)?\d+(\.\d+)?),',re.S)
    pattern_rogp=re.compile(r'"XSMLL" : (\S+),',re.S)
    #pattern_npr=re.compile(r'"XSJLL" : ((\-)?\d+(\.\d+)?),',re.S)
    pattern_npr=re.compile(r'"XSJLL" : (\S+),',re.S)
    #pattern_rolta=re.compile(r'"ZCFZL" : ((\-)?\d+(\.\d+)?),',re.S)
    pattern_rolta=re.compile(r'"ZCFZL" : (\S+),',re.S)
    #pattern_tat=re.compile(r'"TOAZZL" : ((\-)?\d+(\.\d+)?),',re.S)
    pattern_tat=re.compile(r'"TOAZZL" : (\S+),',re.S)
    #pattern_it=re.compile(r'"CHZZL" : ((\-)?\d+(\.\d+)?),',re.S)
    pattern_it=re.compile(r'"CHZZL" : (\S+),',re.S)
    #pattern_troar=re.compile(r'"YSZKZZL" : ((\-)?\d+(\.\d+)?),',re.S)
    pattern_troar=re.compile(r'"YSZKZZL" : (\S+),',re.S)
    
    items_eps=re.findall(pattern_eps,html)
    print(items_eps)
    items_date=re.findall(pattern_date,html)
    print(items_date)
    items_bps=re.findall(pattern_bps,html)
    print(items_bps)
    items_ncfps=re.findall(pattern_ncfps,html)
    print(items_ncfps)
    items_yoygotor=re.findall(pattern_yoygotor,html)
    print(items_yoygotor)
    items_yoygokfnp=re.findall(pattern_yoygokfnp,html)
    print(items_yoygokfnp)
    items_roe=re.findall(pattern_roe,html)
    print(items_roe)
    items_rogp=re.findall(pattern_rogp,html)
    print(items_rogp)
    items_npr=re.findall(pattern_npr,html)
    print(items_npr)
    items_rolta=re.findall(pattern_rolta,html)
    print(items_rolta)
    items_tat=re.findall(pattern_tat,html)
    print(items_tat)
    items_it=re.findall(pattern_it,html)
    print(items_it)
    items_troar=re.findall(pattern_troar,html)
    print(items_troar)
    
    
    """
    for i in range(len(items_eps)):
        items_eps_final.append(items_eps[i][0])
        """
    for i in range(len(items_date)):
        items_date_final.append(items_date[i][0])
        """
    for i in range(len(items_bps)):
        items_bps_final.append(items_bps[i][0])
    for i in range(len(items_ncfps)):
        items_ncfps_final.append(items_ncfps[i][0])
    for i in range(len(items_yoygotor)):
        items_yoygotor_final.append(items_yoygotor[i][0])
    for i in range(len(items_yoygokfnp)):
        items_yoygokfnp_final.append(items_yoygokfnp[i][0])
    for i in range(len(items_roe)):
        items_roe_final.append(items_roe[i][0])
    for i in range(len(items_rogp)):
        items_rogp_final.append(items_rogp[i][0])
    for i in range(len(items_npr)):
        items_npr_final.append(items_npr[i][0])
    for i in range(len(items_rolta)):
        items_rolta_final.append(items_rolta[i][0])
    for i in range(len(items_tat)):
        items_tat_final.append(items_tat[i][0])
    for i in range(len(items_it)):
        items_it_final.append(items_it[i][0])
    for i in range(len(items_troar)):
        items_troar_final.append(items_troar[i][0])
    """
    for i in range(len(items_date_final)):
        #print(items_date_final[i])
        final_item.append(items_date_final[i])
        
        #final_item.append(items_eps_final[i])  
        final_item.append(items_eps[i])  
        #final_item.append(items_bps_final[i])
        final_item.append(items_bps[i])
        #final_item.append(items_ncfps_final[i])
        final_item.append(items_ncfps[i])
        #print(type(items_yoygotor_final[i]))
        #print(items_yoygotor_final[i])
    
        #final_item.append(items_yoygotor_final[i])
        final_item.append(items_yoygotor[i])
        
        #if items_yoygokfnp_final[i]!='null':
        #final_item.append(items_yoygokfnp_final[i])
        final_item.append(items_yoygokfnp[i])
       # else:
            #final_item.append('0')
        #final_item.append(items_roe_final[i])
        final_item.append(items_roe[i])
        #final_item.append(items_rogp_final[i])
        final_item.append(items_rogp[i])
        #final_item.append(items_npr_final[i])
        final_item.append(items_npr[i])
        #final_item.append(items_rolta_final[i])
        final_item.append(items_rolta[i])
        #final_item.append(items_tat_final[i])
        final_item.append(items_tat[i])
        #final_item.append(items_it_final[i])
        final_item.append(items_it[i])
        #final_item.append(items_troar_final[i])
        final_item.append(items_troar[i])
    
    return final_item
 
    
    #return items_troar_final

def write_to_excel(item,stock_list):
    #with pd.ExcelWriter(r'C:/Users\yhj\.spyder-py3\stock_spider/test_dsl.xlsx') as writer:
        columns=[]
        if item:
            #print(item[0])
            for i in range(len(item)):
                if re.search(r'(([0-9]{4})-([0-9]{2})-([0-9]{2}))',item[i]):
                    #print('yes!')
                    columns.append(item[i])
            #with pd.ExcelWriter('C:/Users\yhj\.spyder-py3\stock_spidertest_dsl.xlsx') as writer:
            pos1=[]
            for j in range(len(columns)):
                for i in range(len(item)):
                    if item[i]==columns[j]:
                        """
                        while(item[i]!=columns[j+1]):
                            content.append(item[i])
                        break
                        """
                        pos1.append(i)
                        """
                    if item[i]==columns[j+1]:
                        pos2.append(i)
                        """
            """
            df=pd.DataFrame(item[pos1[0]+1:pos1[1]],
                            columns=[item[pos1[0]:pos1[1]][0]]
                            
                )
            """
            df=pd.DataFrame(data=None,
                            columns=['black_cell'],
                            index=['EPS','BPS','每股经营现金流','总营收同比增长','扣非净利润同比增长',
                                   'ROE','毛利率','净利率','资产负债率','总资产周转率','存货周转率','应收账款周转率']
                            
                )
              
              
            
            #for i in columns[1:-1]:
            for i in range(len(columns)-1):
                #print(item[pos1[i]:pos1[i+1]])
                """
                df=pd.DataFrame(item[pos1[i+1]:pos1[i+1]],
                                columns=[item[pos1[i]:pos1[i+1]][0]],
                                index=['1','2','3','4','5','6','7','8','9','10','11','12']
                
                    )
                """
                df.insert(loc=0,column=columns[i],value=item[pos1[i]+1:pos1[i+1]])
                #print(i)
                
            #print(item[pos1[len(pos1)-1]:])
            df.insert(loc=0,column=columns[-1],value=item[pos1[-1]+1:])
            df.drop('black_cell',axis=1,inplace=True)
            #print(df)
            #print(pos1)
            #df.to_excel(writer,sheet_name=stock_list)
            return(df)
            print("Done!")
            
        else:
            print("Write Error !")
    
"""    
 writer=pd.ExcelWriter('C:/Users\yhj\.spyder-py3\stock_spidertest_dsl.xlsx')
 filepath=pd.ExcelFile('C:/Users\yhj\.spyder-py3\stock_spider/test_dsl.xlsx')
 df.to_excel(filepath,sheet_name=stock_list,storage_options=())
 """  
     #with pd.ExcelWriter('C:/Users\yhj\.spyder-py3\stock_spidertest_dsl.xlsx') as writer:
         #with pd.ExcelWriter('C:/Users\yhj\.spyder-py3\stock_spidertest_dsl.xlsx') as writer:




if __name__=='__main__':
    #url='http://emweb.securities.eastmoney.com/NewFinanceAnalysis/Index?type=web&code=sh603233'
    with pd.ExcelWriter(r'C:/Users\yhj\.spyder-py3\stock_spider/test_dsl.xlsx') as writer:

        for i in  stock_index.stock_list:
            a=request_data(i)
            if a:
                b=parse_html(a)
                #print(b)
                print("-------------------------")
                #time.sleep(1)
                df_=write_to_excel(b,i)   
                df_.to_excel(writer,sheet_name=i)
        