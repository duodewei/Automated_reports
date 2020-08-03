
#程序入口
import sys
#导入链接数据库，下载数据和邮件发送数据文件
from core.Analyse_data import analyse
from core.Download_data import down_Sql
from core.Emaile_data import emaile



if __name__ == "__main__":
    # 链接数据库，并设置MySQL语句
    Search1 = down_Sql('root', '123456', 'SELECT * FROM data_2')
    # 设置链接数据库名和方式后下载数据
    data2 = Search1.from_mysql_get_all_info('localhost', 3306, 'sale_data', 'gbk')
    # 将数据写入本地文件等待进一步分析
    Search1.write_csv(data2, 'D:/2000.csv')

    # 将数据分析后写入新的文件
    Write = analyse('D:/2000.csv', 'D:/3000.csv')
    #获取具体哪天的数据，注意时间格式
    Write.get_data('2019-05-06')
    # 写入excel
    Write.write_toexcel()
    # 并绘制数据透视图
    Write.drawing()

    #发送邮件，设置发送人，验证码，收件人（可以设置两个）以及邮件主题
    sender1 = emaile("mqw_test@163.com","VPAUITGNHJFNRVLN",["1594015406@qq.com", "mqw_1996@163.com"],  """每日销售报表""", 'D:/3000.csv')
    #发送文件
    sender1.send_emaile()
