# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tushare as ts
token='4e756df3ddf4450cbd617eaad43d8a5431510412aacba01025359b8d'
pro = ts.pro_api(token)
#输入证券名称
name='xcny'
#输入证券代码
name=ts.get_k_data('600777',start='2023-01-01',end='2023-08-15',ktype='D')
name.head()
name.to_csv('xcny.csv')
'''
token='4e756df3ddf4450cbd617eaad43d8a5431510412aacba01025359b8d'
pro = ts.pro_api(token)
df_daily=pro.index_daily(ts_code="000001.SH")
df_daily.head()
#sh=ts.get_index()
#sh=ts.get_(code='000001.SH',start='2019-01-01',end='2023-07-25',ktype='D')
#sh.head()
df_daily.to_csv('sh.csv')
'''
