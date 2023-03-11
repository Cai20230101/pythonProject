import akshare as ak
import pandas
import tools.excel_to_mysql as em
import xlrd
import pymysql
from datetime import date, datetime

# 建表并生成插入语句
from xlrd import xldate_as_tuple

# 分时数据-新浪 接口: stock_zh_a_minute
# symbol	str	symbol='sh000300'; 同日频率数据接口
# period	str	period='1'; 获取 1, 5, 15, 30, 60 分钟的数据频率
# adjust	str	adjust=""; 默认为空: 返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据;

gp_value = 'sh601698'

# 股票信息
data = ak.stock_zh_a_minute(symbol=gp_value,period="30",adjust="qfq")
print(data)

file = gp_value + ".xlsx"
file_path = "E:\excel\\"+file
data.to_excel(file_path,index=False)

db = pymysql.connect(host='localhost', port=3358, user='root', passwd="a123456.", db='cj')


dir_path = "E:/excel/"  # "D:/"
em.excelrun(db,dir_path,file)





