# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 10:47:11 2019

@author: Sandy Sun
"""

import pandas as pd
import numpy as np
# import data sets
test_names = pd.read_excel('Test Campaign Names.xlsx')
# reference (a new excel file with different sheets)
client_short_names = pd.ExcelFile('Campaign Naming Convention.xlsx').parse(0)
channel = pd.ExcelFile('Campaign Naming Convention.xlsx').parse(1) 
tactic = pd.ExcelFile('Campaign Naming Convention.xlsx').parse(2)
brand = pd.ExcelFile('Campaign Naming Convention.xlsx').parse(3) 
criterion = pd.ExcelFile('Campaign Naming Convention.xlsx').parse(4) 
country = pd.ExcelFile('Campaign Naming Convention.xlsx').parse(5) 
language = pd.ExcelFile('Campaign Naming Convention.xlsx').parse(6) 
engine = pd.ExcelFile('Campaign Naming Convention.xlsx').parse(7) 

####this new df deletes hidden columns like 'O/S/B' and 'O/S/B short'.'''



'''General Rules to Consider'''
# whether there are 10 dashes in each campaign name
def countdash(df):
    #change each cell in test_names as a string 
    campaign_name = list(df['Campaign name'])
    for i in campaign_name:
        index = df[df['Campaign name']==i].index.tolist()[0]
        if i.count('_') == 10:
            df.loc[index,'countdash'] = 'Pass'
        else:
            df.loc[index,'countdash'] = 'Fail'
    return df

# for those sections that are not up to creater, whether they have correct info
def correct_info(df):
    for i in df["Campaign name"]:
        index = df[df['Campaign name'] == i].index.tolist()[0]
        if i.split("_")[1] in list(client_short_names.client_short_name.unique()) and \
        i.split("_")[3] in list(channel.Channel.unique()) and \
        i.split("_")[4] in list(tactic.Tactic.unique()) and \
        i.split("_")[5] in list(brand['Brand/Non/Comp'].unique()) and \
        i.split("_")[6] in list(criterion['Criterion Type'].unique()) and \
        i.split("_")[8] in list(country.Country.unique()) and \
        i.split("_")[9] in list(language.Language.unique()) and \
        i.split("_")[10] in list(engine.Engine.unique()):
            df.loc[index,'info'] = 'Pass'
        else:
            df.loc[index,'info'] = 'Fail'
    return df

dic_tactic = {}
for index,row in tactic.iterrows():
    dic_tactic[row[0]] = row[1]
dic_tactic = {v : k for k, v in dic_tactic.items()}

# matching in tactic
def match(df):
    for i in df['Campaign name']:
        index = df[df['Campaign name']==i].index.tolist()[0]
        if i.split('_')[4] in dic_tactic.keys():
            if i.split('_')[3] in dic_tactic[i.split('_')[4]]:
                df.loc[index,'match']='Pass'
            else:
                df.loc[index,'match']='Fail'
        else:
            df.loc[index,'match']='Fail'
    return df

# whether there are at most 5 dashes for product name 
def five_dash(df):
    campaign_name = list(df['Campaign name'])
    for i in campaign_name:
        index = df[df['Campaign name']==i].index.tolist()[0]
        if i.split("_")[2].count('-') <= 5:
            df.loc[index,'five_dash'] = 'Pass'
        else:
            df.loc[index,'five_dash'] = 'Fail'
    return df





'''Specific Rules for Non-Paid Campaigns'''
# whether is Paid Social channel 
def non_ps(df):
    for i in df["Campaign name"]:
        index = df[df['Campaign name']==i].index.tolist()[0]
        if i.split("_")[3] != 'PS':
            df.loc[index,'non_ps'] = 'Pass'
        else:
            df.loc[index,'non_ps'] = 'Fail'
    return df

# whether there is 'PS' to represent social Tactic and Engine
tactic_ps = []
for i in range(len(tactic['Tactic Long'])):
    if '(PS)' in tactic['Tactic Long'][i]:
        tactic_ps.append(tactic['Tactic'][i])

engine_ps = []
for i in range(len(engine['Engine Long'])):
    if '(PS)' in engine['Engine Long'][i]:
        engine_ps.append(engine['Engine'][i])

def non_social(df):
    for i in df["Campaign name"]:
        index = df[df['Campaign name']==i].index.tolist()[0]
        if i.split("_")[4] in tactic_ps or i.split("_")[9] in engine_ps:  
            df.loc[index,'non_social'] = 'Fail'
        else:
            df.loc[index,'non_social'] = 'Pass'
    return df





'''Application'''
def Naming (df):
    df = countdash(df)
    df = correct_info(df)
    df = match(df)
    df = five_dash(df)
    df = non_ps(df)
    df = non_social(df)
    for index, row in df.iterrows():
        if 'Fail' in list(row)[1:7]:
            df.loc[index,'Final Result'] = 'Fail'
        else:
            df.loc[index,'Final Result'] = 'Pass'
    df = df.drop(columns="countdash")
    df = df.drop(columns="info")
    df = df.drop(columns='match')
    df = df.drop(columns="five_dash")
    df = df.drop(columns="non_ps")
    df = df.drop(columns="non_social")
    return df 

Naming(test_names)['Final Result'].value_counts()




