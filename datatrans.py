from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import easyxf
import pandas as pd
import datetime
import time
import random

EIP_Raw_data = pd.read_excel("C:\\Users\\t03492\\Desktop\\datatransfer\\EIP_applyforBusiness_table.xlsx")
EIP_data = EIP_Raw_data[EIP_Raw_data['第二列'] == 7]
print(EIP_data.index)
print(len(EIP_data.index))
print(EIP_data['费用报销申请编号'])
M7_data = pd.read_excel("C:\\Users\\t03492\\Desktop\\datatransfer\\mission7_business_bill_details.xlsx")

cellstyle = easyxf('font: height 180, name SimSun;'
                    'align: wrap on, vert center, horiz left;' 
                    'borders: left thin, right thin, top thin, bottom thin, left_colour red, top_colour red, bottom_colour red;'
                    )

leaderposition = ['部门经理', '项目经理', '客户经理']
pzh_num = []
for i in EIP_data.index:
    print(i)
    rb = open_workbook("C:\\Users\\t03492\\Desktop\\datatransfer\\凭证号-任务X-年-出差申请表模板.xls",formatting_info=True)
    w = copy(rb)
    w_sheet = w.get_sheet(0)
    w_sheet.write(2,2,str(EIP_data['制单人'][i]), cellstyle)
    w_sheet.write(2,4, str(EIP_data['制单日期'][i]), cellstyle)

    w_sheet.write(5,2, str(EIP_data['申请人'][i]), cellstyle)
    w_sheet.write(5,4, str(EIP_data['申请日期'][i]), cellstyle)
    w_sheet.write(6,2, str(EIP_data['申请部门'][i]), cellstyle)
    w_sheet.write(6,4, str(EIP_data['申请人工号'][i]), cellstyle)
    w_sheet.write(7,2, str(EIP_data['职位'][i]), cellstyle)
    w_sheet.write(7,4, str(EIP_data['直接上级'][i]), cellstyle)
    w_sheet.write(8,2, str(EIP_data['签约公司'][i]), cellstyle)
    if EIP_data['签约公司'][i] == '天博':
        w_sheet.write(8,4, '上海', cellstyle)
    else:
        w_sheet.write(8,4, '北京', cellstyle)

    w_sheet.write(11,2, str(EIP_data['出差申请编号'][i]), cellstyle)
    w_sheet.write(12,2, str(EIP_data['出差事由'][i]), cellstyle)
    w_sheet.write(15,2, str(EIP_data['出差开始日期'][i]), cellstyle)
    w_sheet.write(15,4, str(EIP_data['出差结束日期'][i]), cellstyle)
    w_sheet.write(16,2, str(EIP_data['出差国别'][i]), cellstyle)
    w_sheet.write(16,4, str(EIP_data['出差省份'][i]), cellstyle)
    w_sheet.write(17,2, str(EIP_data['出差城市'][i]), cellstyle)

    positon_int = random.randint(0, 2)
    submit_time_interval = random.randint(600, 900)
    approve_time_interval = random.randint(115200, 151200)

    timestr = str(EIP_data['制单日期'][i])
    timeArray = time.strptime(timestr, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))

    submit_timeArray = timeStamp + submit_time_interval
    approve_timeArray = timeStamp + approve_time_interval

    subtime = time.localtime(submit_timeArray)
    apptime = time.localtime(approve_timeArray)

    submit_time = time.strftime("%Y-%m-%d %H:%M:%S", subtime)
    approve_time = time.strftime("%Y-%m-%d %H:%M:%S", apptime)

    applyInfo = str(EIP_data['申请人'][i]) + '_' + str(EIP_data['申请部门'][i]) + '_'+ str(EIP_data['职位'][i])
    leaderInfo = str(EIP_data['直接上级'][i]) + '_' + str(EIP_data['申请部门'][i]) + '_'+ leaderposition[positon_int]

    w_sheet.write(21,2, applyInfo, cellstyle)
    w_sheet.write(21,3, submit_time, cellstyle)
    w_sheet.write(22,2, leaderInfo, cellstyle)
    w_sheet.write(22,3, approve_time, cellstyle)

    if EIP_data['费用报销申请编号'][i] in list(M7_data['源单单号']):
        row_num = M7_data[M7_data.源单单号 == EIP_data['费用报销申请编号'][i]].index.tolist()
        index = row_num[0]
        if M7_data['凭证号'][index] in pzh_num:
            filepath = "C:\\Users\\t03492\\Desktop\\datatransfer\\"+ str(M7_data['凭证号'][index]) +"-任务7-" + str(M7_data['会计年度'][index])+"-出差申请表模板(1).xls"
            w.save(filepath)
        pzh_num.append(M7_data['凭证号'][index])
        print(row_num)
        print(M7_data['凭证号'][index])
        print(M7_data['会计年度'][index])
        filepath = "C:\\Users\\t03492\\Desktop\\datatransfer\\"+ str(M7_data['凭证号'][index]) +"-任务7-" + str(M7_data['会计年度'][index])+"-出差申请表模板.xls"
        w.save(filepath)
    else:
        print(EIP_data['费用报销申请编号'][i])

print(sorted(pzh_num))
