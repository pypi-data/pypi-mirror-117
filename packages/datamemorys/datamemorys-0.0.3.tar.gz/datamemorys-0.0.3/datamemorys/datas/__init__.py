from pandas import DataFrame
import pandas
import json
import requests
from datamemorys.core import SYCM_DATAS

class DMDataFrame(DataFrame):
    def __init__(self,DM_tablename,loginnNickName,**args):


        loginnNickName=loginnNickName.split(":")[0]
        j=requests.get(SYCM_DATAS[DM_tablename].format(loginnNickName)).json()
        if j['code']!=0:            
            super().__init__()
        else:
            d=j['data']
            c=j['comments']
            data=[]
            for x in d:
                v={}               
                for y in x.keys():                   
                    v[c[y]['cName']]=x[y]
                data.append(v)  
                df_=DataFrame(data)          
            for x in args:
                if c[x]['cName'] in df_.keys():                    
                    df_=df_[df_[c[x]['cName']]==args[x]]
            super().__init__(df_)


            


    def Mysqlsqlstr(self,tablename):
        df=self.astype(str)
        kk=df.keys()
        d=[[df[y][x] for y in kk] for x in df.index]
        d=["('"+"','".join(x)+"')" for x in d]
        sql="insert into {}(`".format(tablename)+"`,`".join(kk)+"`) values"+ ",".join(d)
        return sql