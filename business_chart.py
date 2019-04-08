import xlrd
from xlutils.copy import copy
import pandas as pd 
from pandas import ExcelWriter

EIP_data = xlrd.open_workbook('C:\\Users\\t03492\\Desktop\\datatransfer\\EIP_applyforBusiness_table.xlsx', formatting_info = True)

Mis_data = xlrd.open_workbook('C:/Users/t03492/Desktop/datatransfer/mission7_business_bill_details.xlsx', formatting_info=True) #target
temp_chart = xlrd.open_workbook(r'C:\Users\t03492\Desktop\datatransfer\凭证号-任务X-年-出差申请表模板.xlsx', formatting_info=True)
chart_output = copy(temp_chart)
chart = chart_output.get_sheet(0)
chart.write(2, 2, '六星')
chart_output.save(r'C:\Users\t03492\Desktop\datatransfer\凭证号-任务7-2014-出差申请表模板.xlsx')
print(df_EIP['制单人'][1])
print(df_output.iloc[0:3, 0])
df_output.iloc[1, 1] = df_EIP['制单人'][1]
df_output.iloc[1, 3] = df_EIP['制单日期'][1]
writer = ExcelWriter(r'C:\Users\t03492\Desktop\datatransfer\凭证号-任务7-2014-出差申请表模板.xlsx')
df_output.to_excel(r'C:\Users\t03492\Desktop\datatransfer\凭证号-任务7-2014-出差申请表模板.xlsx', 'Sheet1')
