import akshare as ak
import pymysql


dir_path = "D:/"
insert_data("stock_data.xlsx")
excel_path = "%s%s" % (dir_path, file_name)


# 连接MySQL数据库
conn = pymysql.connect(host='localhost', port=3358, user='root', password='a123456.', database='ck')
cursor = conn.cursor()

# 获取全部股票的信息
stock_df = ak.stock_zh_a_spot_em()

# 创建表
# create_table_sql = '''
# CREATE TABLE IF NOT EXISTS stock_spot_data (
#     id INT(11) NOT NULL AUTO_INCREMENT,
#     ts_code VARCHAR(20) NOT NULL,
#     name VARCHAR(20) NOT NULL,
#     last_price FLOAT(10, 2) NOT NULL,
#     pre_close FLOAT(10, 2) NOT NULL,
#     open FLOAT(10, 2) NOT NULL,
#     high FLOAT(10, 2) NOT NULL,
#     low FLOAT(10, 2) NOT NULL,
#     bid_price1 FLOAT(10, 2) NOT NULL,
#     ask_price1 FLOAT(10, 2) NOT NULL,
#     volume FLOAT(10, 2) NOT NULL,
#     amount FLOAT(10, 2) NOT NULL,
#     date VARCHAR(20) NOT NULL,
#     time VARCHAR(20) NOT NULL,
#     PRIMARY KEY (id)
# )
# '''
# cursor.execute(create_table_sql)

# 插入数据
insert_sql = '''
INSERT INTO stock_spot_data (ts_code, name, last_price, pre_close, open, high, low, bid_price1, ask_price1, volume, amount, date, time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

for i in range(len(stock_df)):
    values = tuple(stock_df.iloc[i])
    cursor.execute(insert_sql, values)

conn.commit()

cursor.close()
conn.close()
