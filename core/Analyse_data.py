import pandas as pd
import numpy as np
import datetime
import xlsxwriter


class analyse:
    def __init__(self, file1, file2, total_data = [], report=''):
        self.file1 = file1
        self.file2 = file2
        self.total_data = total_data
        self.report = report


    def get_data(self, which_day):
        data= pd.read_csv(self.file1, encoding = 'gbk')

        #为下载后的数据添加表头
        data.columns=["创建时间", "收货省", "订单编号", "订单量", "总量"]

        #分析时间数据，所以将时间列转换为时间格式
        data["创建时间"] = pd.to_datetime(data["创建时间"])
        data = data.set_index("创建时间")

        #print('---------获取具体某天的数据-----------')
        # Get the data of one day

        #获取具体哪天的数据
        one_day = data[which_day]

        #数据透视，并计算当天各省份销售数量之和
        self.report = pd.pivot_table(one_day,index=['收货省'], columns=['创建时间'],values=['总量'],aggfunc='sum', fill_value=0)
        self.report['sum'] = self.report.sum(axis=1)

    #Write data to csv file

    def write_toexcel(self):
        self.workbook = xlsxwriter.Workbook(self.file2)
        self.worksheet = self.workbook.add_worksheet('Sheet1')
        self.chart = self.workbook.add_chart({'type': 'column'})

        #Format the table
        format=self.workbook.add_format()
        format.set_border(1)
        format_title=self.workbook.add_format()
        format_title.set_border(1)
        format_title.set_bg_color('#cccccc')
        format_title.set_align('center')
        format_title.set_bold()
        format_ave=self.workbook.add_format()
        format_ave.set_border(1)
        format_ave.set_num_format('0.00')

        #Write data to the table
        title = [u'发货省',u'总运输量']
        self.worksheet.write_row('A1',title,format_title)
        Accept_province = self.report.index
        self.worksheet.write_column('A2', Accept_province ,format)

        total = self.report["sum"]

        for i in range(len(total)):
            i2 = total[i]
            self.total_data.append(i2)

        for x in range(len(self.total_data)):
            #print(self.total_data[x])
            self.worksheet.write_number('B'+ str(x+2), self.total_data[x], format)

        #self.report.ix[[1],:].values

    #Drawing
    def chart_series(self,cur_row):
        self.chart.add_series({
        'categories': '=Sheet1!$B$1:$B$1',
        'values':   '=Sheet1!$B$'+cur_row+':$B$'+cur_row,
        'line':    {'color': 'black'},
        'name':  '=Sheet1!$A$'+cur_row,
      })

    def drawing(self):
        for row in range(2, len(self.total_data)+2):
            analyse.chart_series(self, str(row))

        self.chart.set_size({'width': 577, 'height': 287})
        self.chart.set_title ({'name': u'每日销售总量汇总表'})
        self.chart.set_y_axis({'name': '销售总量'})
        self.chart.set_x_axis({'name':'各省市数据'})
        self.worksheet.insert_chart('F1', self.chart)
        self.workbook.close()

