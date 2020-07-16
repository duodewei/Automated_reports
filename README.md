# Automated_reports
After automatically analyzing the sales data and generating a report, send it to the next designated.
## 需求
编写一个日销售量分析的自动化报表程序，可以从数据库中下载每日销售数据，并将数据进行汇总分析后生成.csv文件，并自动邮件发送到指定邮箱，选择Python作为编程语言。


## 背景
现在数据库中保存了2019年5，6，7月份企业的后台订单数据，包括创建时间，收货省份，订单号，订单量和销售量。可以将需求细分为以下几步：
- 从MySQL数据库中将全部数据保存到本地（对数据库数据进行筛选运行效率会更好）
- 对数据进行数据透视表操作，汇总每日各个省份的销售数据，并绘制直方图，生成一个日销售报表文件
- 自动邮件发送该文件到指定邮箱
- 系统设置每天定时自动执行该脚本

## 代码介绍
- core文件存放逻辑文件
- data为测试数据
- run是运行主程序
