import pymysql
import csv

def from_mysql_get_all_info():
    '''
    Connect to the database
    Use the cursor to get all the data in the table
    '''
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        db='sale_data',
        password='123456',     #password
        charset='gbk')
    cursor = conn.cursor()
    sql = 'SELECT * FROM data_2'
    cursor.execute(sql.encode('gbk'))
    data = cursor.fetchall()
    conn.close()
    return data
from_mysql_get_all_info()

def write_csv():
    '''
    Write data to local
    '''
    data = from_mysql_get_all_info()
    filename = '2000.csv'
    with open(filename, mode='w',newline ='', encoding='gbk') as f:
        write = csv.writer(f,dialect='excel')
        for item in data:
            write.writerow(item)

write_csv()