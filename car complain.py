# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:30:13 2021

@author: meishikun
"""


# #对汽车投诉信息进行分析
import pandas as pd

result = pd.read_csv('car_complain.csv')

result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))
print(result.columns)
tags = result.columns[7:]
df= result.groupby(['brand'])['id'].agg(['count'])
df2= result.groupby(['brand'])[tags].agg(['sum'])
df2 = df.merge(df2, left_index=True, right_index=True, how='left')
df2.reset_index(inplace=True)
df2= df2.sort_values('count', ascending=False)
print(df2)
query = ('A11', 'sum')
print(df2.sort_values(query, ascending=False))