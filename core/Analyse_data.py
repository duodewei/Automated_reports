import pandas as pd
import numpy as np
import datetime

data= pd.read_csv(r'2000.csv', encoding = 'gbk')
data.columns=["创建时间", "收货省", "订单编号", "订单量", "总量"]
data["创建时间"] = pd.to_datetime(data["创建时间"])
data = data.set_index("创建时间")

print('---------获取具体某天的数据-----------')
# Get the data of one day
one_day = data['2019-05-05']
report = pd.pivot_table(one_day,index=['收货省'], columns=['创建时间'],values=['总量'],aggfunc='sum', fill_value=0)
report['sum']=report.sum(axis=1)

#Write data to csv file
import xlsxwriter
workbook = xlsxwriter.Workbook(r'3000.csv')
worksheet = workbook.add_worksheet('sheet1')
chart = workbook.add_chart({'type': 'column'})

#Format the table
format=workbook.add_format()
format.set_border(1)
format_title=workbook.add_format()
format_title.set_border(1)
format_title.set_bg_color('#cccccc')
format_title.set_align('center')
format_title.set_bold()
format_ave=workbook.add_format()
format_ave.set_border(1)
format_ave.set_num_format('0.00')

#Write data to the table
title = [u'发货省',u'总运输量']
worksheet.write_row('A1',title,format_title)
Accept_province = report.index
worksheet.write_column('A2', Accept_province ,format)

total = report["sum"]
total_data = []
for i in range(len(total)):
    i2 = total[i]
    total_data.append(i2)

for x in range(len(total_data)):
    print(total_data[x])
    worksheet.write_number('B'+ str(x+2), total_data[x], format)

report.ix[[1],:].values

#Drawing
def chart_series(cur_row):
    chart.add_series({
    'categories': '=Sheet1!$B$1:$B$1',
    'values':   '=Sheet1!$B$'+cur_row+':$B$'+cur_row,
    'line':    {'color': 'black'},
    'name':  '=Sheet1!$A$'+cur_row,
  })


for row in range(2, len(total_data)+2):
    chart_series(str(row))

chart.set_size({'width': 577, 'height': 287})
chart.set_title ({'name': u'每日销售总量汇总表'})
chart.set_y_axis({'name': '销售总量'})
chart.set_x_axis({'name':'各省市数据'})
worksheet.insert_chart('F1', chart)
workbook.close()