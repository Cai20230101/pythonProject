import akshare as ak
import pymysql

# 连接MySQL数据库
conn = pymysql.connect(host='localhost', port=3358, user='root', password='a123456.', database='ck')
cursor = conn.cursor()

# 插入数据
select_sql = '''
select * from  ck.act_hi_detail  
'''

cursor.execute(select_sql)
data = cursor.fetchall()
print(data)
