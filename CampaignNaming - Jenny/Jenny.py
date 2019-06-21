#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 15:11:03 2019

@author: zhangwang(Jenny)
"""

import pandas as pd
from openpyxl import load_workbook
from collections import defaultdict

file = "Non-Paid.xlsx" 
#is a excel file with list of campaign names for QA Check

rules = "Rules.xlsx" 
#is a excel sheet that documents all types of rules. 
#if there is any change in QA Checking rules, we can just update this excel file

'''STEP 1: Read Campaign Names and QA rules from excel sheet'''
campaign = pd.ExcelFile(file).parse("Test Google Ads Campaigns")
rule = pd.ExcelFile(rules)
    
rlst = []
for i in range(len(rule.sheet_names)):
    rlst.append(rule.sheet_names[i])

#get rules for different checking scenarios as lists
UDS = list(rule.parse(str(rlst[0]))["UDS"])
EDL = list(rule.parse(str(rlst[1]))["EDL"])
CLNT = list(rule.parse(str(rlst[2]))["CLNT"])
PRD = list(rule.parse(str(rlst[3]))["PRD"])
BNM = list(rule.parse(str(rlst[5]))["BNM"])
CRI = list(rule.parse(str(rlst[6]))["CRI"])
NLT = list(rule.parse(str(rlst[7]))["NLT"])
CNT = list(rule.parse(str(rlst[8]))["CNT"])
LNG = list(rule.parse(str(rlst[9]))["LNG"])
ENG = list(rule.parse(str(rlst[10]))["ENG"])
    
#matching channel and tactics, then combined into a dictionary
test = rule.parse("CHNL_TACT")
CHNL_TACT = defaultdict(list)

for index, row in test.iterrows():
    CHNL_TACT[row["CHNL"]].append(row["TACT"])
        
 
'''STEP 2: The QA Rules for all scenarios'''
#NOTES: if there is any change in rules, just update the individual QA_test function
QA1 = []
QA2 = []
QA3 = []
QA4 = []
QA5 = []
QA6 = []
QA7 = []
QA8 = []
QA9 = []
QA10 = []
QA11 = [] 
result = []

#QA1: Check underscores number
def QA1_test(lst):
    if len(lst) == UDS[0]:
        QA1.append(0)
    else:
        QA1.append(1)
        
    return QA1

#QA2: Check EDL
def QA2_test(a, lst):
    if lst[a] in EDL:
        QA2.append(0)
    else:
        QA2.append(1)
        
    return QA2 

#QA3: Check client short name
def QA3_test(a, lst):
    if lst[a] in CLNT:
        QA3.append(0)
    else:
        QA3.append(1)
        
    return QA3

#QA4: Check product name
def QA4_test(a, lst):
    if len(lst[a].split("-"))<=PRD[0] or "-" not in lst[a]:
        QA4.append(0)
    else:
        QA4.append(1)
        
    #return plst
    return QA4

#QA5: Check whether Channel and tactic match
def QA5_test(a, lst):
    if lst[a] in CHNL_TACT and lst[a+1] in CHNL_TACT.get(lst[a]):
        QA5.append(0)
    else: 
        QA5.append(1)

    return QA5

#QA6: Check Brand/Non/Comp 
def QA6_test(a, lst):
    if lst[a] in BNM:
        QA6.append(0)
    else:
        QA6.append(1)
    
    return QA6

#QA7: Check criterion type
def QA7_test(a, lst):
    if lst[a] in CRI:
        QA7.append(0)
    else:
        QA7.append(1)

    return QA7

#QA8: Check NLT
def QA8_test(a, lst):
    if len(lst[a].split("-"))<=NLT[0] or "-" not in lst[a]:
        QA8.append(0)
    else:
        QA8.append(1)

    return QA8

#QA9: Check country
def QA9_test(a, lst):
    if lst[a] in CNT:
        QA9.append(0)
    else:
        QA9.append(1)
        
    return QA9

#QA10: Check language
def QA10_test(a, lst):
    if lst[a] in LNG:
        QA10.append(0)
    else:
        QA10.append(1)
        
    return QA10

#QA11: Check target engine 
def QA11_test(a, lst):
    if lst[a] in ENG:
        QA11.append(0)
    else:
        QA11.append(1)

    return QA11


'''STEP 3: Perform the QA Check'''
def QA_check():
    for i in range(len(campaign["Campaign name"])):
        lst = campaign["Campaign name"][i].split("_")
        QA1_test(lst)
        a = 0
        QA2_test(a,lst)
        a += 1
        QA3_test(a,lst)
        a += 1
        QA4_test(a,lst)
        a += 1
        QA5_test(a,lst)
        a += 2
        QA6_test(a,lst)
        a += 1
        QA7_test(a,lst)
        a += 1
        QA8_test(a,lst)
        a += 1
        QA9_test(a,lst)
        a += 1
        QA10_test(a,lst)
        a += 1
        QA11_test(a,lst)   
        
        QA = QA1[i]+QA2[i]+QA3[i]+QA4[i]+QA5[i]+QA6[i]+QA7[i]+QA8[i]+QA9[i]+QA10[i]+QA11[i]
        if QA == 0:
            result.append("Pass")
        else:
            result.append("Fail")

QA_check()

'''STEP 4: Save the result'''
#combine QA Check result into a dataframe
name = list(campaign["Campaign name"])
QA_result = pd.DataFrame(list(zip(name, result, QA1, QA2, QA3, QA4, QA5, QA6, 
                                  QA7, QA8, QA9, QA10, QA11)),
                     columns = ["Campaign name","Pass/Fail","Underscores",
                                "EDL","Client Short Name","Product",
                               "Channel & Tactic","Brand/Non/Comp",
                               "Criterion Type","NLT","Country","Language",
                               "Engine"])
#NOTES: for each campaign name, the dataframe include the overall result - Pass or Faill AND the individua result of each criteria

#save result to the original campaign names excel file
book = load_workbook(file)
writer = pd.ExcelWriter(file, engine='openpyxl') 
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

QA_result.to_excel(writer, "QA_Result", index = False)

writer.save()