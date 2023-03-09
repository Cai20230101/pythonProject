"""
根据excel在mysql中建表(表名为文件名,字段为csv中的header,默认所有字段为varchar,如需更改,在数据库中更改即可),并插入数据
"""

import xlrd
import pymysql
from datetime import date, datetime

# 建表并生成插入语句
from xlrd import xldate_as_tuple


def create_table(conn,file_name, header):
    db = conn
    cursor = conn.cursor()

    table_name = file_name.split(".")[0]

    header = [str(i).replace("－", "_").replace("-", "_").replace("(", "_").replace(")", "") for i in header]
    create_sql = "CREATE TABLE `%s` (`id` int(11) NOT NULL AUTO_INCREMENT," % table_name
    for i in header:
        create_sql += "`%s` varchar(255) DEFAULT NULL," % i
    create_sql += "PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;"
    cursor.execute(create_sql)
    db.commit()
    insert_sql = "insert into %s(%s)values(%s)" % (table_name, ",".join(header), ",".join(['%s'] * len(header)))
    print(insert_sql)
    return insert_sql


# 每一千条插入数据库一次
def insert_data(conn,dir_path,file_name):
    db = conn
    cursor = conn.cursor()
    excel_path = "%s%s" % (dir_path, file_name)
    wb = xlrd.open_workbook(filename=excel_path)

    # 通过sheet索引
    worksheet = wb.sheet_by_index(0)

    # 通过sheet名
    # worksheet = wb.sheet_by_name("人员")

    cols_count = worksheet.ncols
    insert_datas = []
    for i in range(worksheet.nrows):
        if i == 0:
            row_data = worksheet.row_values(0)
            insert_sql = create_table(db,file_name, row_data)
            continue

        row_data = []
        for j in range(cols_count):
            cell_type = worksheet.cell(i, j).ctype
            cell_value = worksheet.cell_value(i, j)
            if cell_type == 3:
                # 转成datetime对象
                date_tool = datetime(*xldate_as_tuple(cell_value, 0))
                cell_value = date_tool.strftime('%Y-%d-%m %H:%M:%S')
            elif cell_type == 4:
                cell_value = True if cell_value == 1 else False
            row_data.append(cell_value)
        sql_data = tuple(row_data)

        print(sql_data)
        insert_datas.append(sql_data)
        if i + 1 % 1000 == 0:
            cursor.executemany(insert_sql, insert_datas)
            db.commit()
            insert_datas = []

    if len(insert_datas) != 0:
        cursor.executemany(insert_sql, insert_datas)
        db.commit()

    db.close()


def excelrun(conn,dir_path,filename) :

    # db = pymysql.connect(host='localhost', port=3358, user='root', passwd="a123456.", db='cj')
    db = conn


    dir_path = dir_path  #"D:/"
    insert_data(db,dir_path,filename)
    # insert_data("stock_data.xlsx")
    db.close()