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
M7_data = pd.read_excel("C:\\Users\\t03492\\Desktop\\datatransfer\\mission7_business_bill_details.xlsx")

cellstyle = easyxf('font: height 180, name SimSun;'
                    'align: wrap on, vert center, horiz left;' 
                    'borders: left thin, right thin, top thin, bottom thin, left_colour red, top_colour red, bottom_colour red;'
                    )

leaderposition = ['部门经理', '项目经理', '客户经理']
for i in EIP_data.index:
    print(i)
rb = open_workbook("C:\\Users\\t03492\\Desktop\\datatransfer\\凭证号-任务X-年-出差申请表模板.xls",formatting_info=True)
w = copy(rb)
w_sheet = w.get_sheet(0)
w_sheet.write(2,2,str(EIP_data['制单人'][0]), cellstyle)
w_sheet.write(2,4, str(EIP_data['制单日期'][0]), cellstyle)

w_sheet.write(5,2, str(EIP_data['申请人'][0]))
w_sheet.write(5,4, str(EIP_data['申请日期'][0]))
w_sheet.write(6,2, str(EIP_data['申请部门'][0]))
w_sheet.write(6,4, str(EIP_data['申请人工号'][0]))
w_sheet.write(7,2, str(EIP_data['职位'][0]))
w_sheet.write(7,4, str(EIP_data['直接上级'][0]))
w_sheet.write(8,2, str(EIP_data['签约公司'][0]))
if EIP_data['签约公司'][0] == '天博':
    w_sheet.write(8,4, '上海')
else:
    w_sheet.write(8,4, '北京')

w_sheet.write(11,2, str(EIP_data['出差申请编号'][0]))
w_sheet.write(12,2, str(EIP_data['出差事由'][0]))
w_sheet.write(15,2, str(EIP_data['出差开始日期'][0]))
w_sheet.write(15,4, str(EIP_data['出差结束日期'][0]))
w_sheet.write(16,2, str(EIP_data['出差国别'][0]))
w_sheet.write(16,4, str(EIP_data['出差省份'][0]))
w_sheet.write(17,2, str(EIP_data['出差城市'][0]))

positon_int = random.randint(0, 3)
submit_time_interval = random.randint(600, 900)
approve_time_interval = random.randint(115200, 151200)
print(submit_time_interval)

timestr = str(EIP_data['制单日期'][0])
timeArray = time.strptime(timestr, "%Y-%m-%d %H:%M:%S")
timeStamp = int(time.mktime(timeArray))
print(timeStamp)
submit_timeArray = timeStamp + submit_time_interval
approve_timeArray = timeStamp + approve_time_interval
print(submit_timeArray, approve_timeArray)
subtime = time.localtime(submit_timeArray)
apptime = time.localtime(approve_timeArray)
submit_time = time.strftime("%Y-%m-%d %H:%M:%S", subtime)
approve_time = time.strftime("%Y-%m-%d %H:%M:%S", apptime)
print(submit_time, approve_time)

applyInfo = str(EIP_data['申请人'][0]) + '_' + str(EIP_data['申请部门'][0]) + '_'+ str(EIP_data['职位'][0])
leaderInfo = str(EIP_data['直接上级'][0]) + '_' + str(EIP_data['申请部门'][0]) + '_'+ leaderposition[positon_int]


w_sheet.write(21,2, applyInfo, cellstyle)
w_sheet.write(21,3, submit_time, cellstyle)
w_sheet.write(22,2, leaderInfo, cellstyle)
w_sheet.write(22,3, approve_time, cellstyle)

# print(EIP_data['费用报销申请编号'][0])
# print(EIP_data['费用报销申请编号'][0] in list(M7_data['源单单号']))
if EIP_data['费用报销申请编号'][0] in list(M7_data['源单单号']):
    row_num = M7_data[M7_data.源单单号 == EIP_data['费用报销申请编号'][0]].index.tolist()
    index = row_num[0]
    print(row_num)
    print(M7_data['凭证号'][index])
    print(M7_data['会计年度'][index])
    filepath = "C:\\Users\\t03492\\Desktop\\datatransfer\\test-"+ str(M7_data['凭证号'][index]) +"-任务7-" + str(M7_data['会计年度'][index])+"-出差申请表模板.xls"
    w.save(filepath)