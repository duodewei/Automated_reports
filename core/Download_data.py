import pymysql
import csv

class down_Sql:
    def __init__(self,user, password, sql):
        self.user = user
        self.password = password
        self.sql = sql

    def from_mysql_get_all_info(self, host, port, db, charset):
        '''
        Connect to the database
        Use the cursor to get all the data in the table
        '''
        conn = pymysql.connect(
            host = host,
            port = port,
            user = self.user,
            db = db,
            password= self.password,     #password
            charset= charset)
        cursor = conn.cursor()
        sql = self.sql
        cursor.execute(self.sql.encode('gbk'))
        data = cursor.fetchall()
        conn.close()
        return data

    def write_csv(self, data, filename):
        '''
        Write data to local
        '''
        filename = filename
        with open(filename, mode='w',newline ='', encoding='gbk') as f:
            write = csv.writer(f,dialect='excel')
            for item in data:
                write.writerow(item)

