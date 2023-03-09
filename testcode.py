import akshare as ak
import pymysql
from sys import path
import tools.excel_to_mysql as em


db = pymysql.connect(host='localhost', port=3358, user='root', passwd="a123456.", db='cj')
dir_path = "D:/"
file_name ="stock_data.xlsx"
em.insert_data(db,dir_path,file_name)

