import os
import pandas as pd
import re

pd.set_option('display.max_columns', 2000)
pd.set_option('display.max_rows', 2000)
pd.set_option('display.width', 5000)
pd.set_option('display.max_colwidth', 50)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

def mymovefile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.move(srcfile,dstfile)          #移动文件
        print ("move %s -> %s"%( srcfile,dstfile))

def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)      #复制文件
        print ("copy %s -> %s"%( srcfile,dstfile))

def get_all_files(folder):
    filenames_path = []
    files_name = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            filename = os.path.join(root, file)
            filenames_path.append(filename)
            files_name.append(file[0:3])
    return filenames_path



def match_delete(word):
    word = int(word)
    if word in list(data_kehudiqudaima['代码']):
        pass
    else:
        if word in wrong_line_code:
            pass
        else:
            wrong_line_code.append(word)
    return word


if __name__ == '__main__':
    folder_path = './file_path'
    files_path = get_all_files(folder_path)
    data = pd.read_excel(files_path[0]
                         , keep_default_na=False
                         )
    fulu_file_path = r'./fulu/kehudiqudaima.xlsx'
    data_kehudiqudaima = pd.read_excel(fulu_file_path)
    fulu_file_path_2 = r'./fulu/qichacha.xls'
    data_qichacha = pd.read_excel(fulu_file_path_2)

    data.loc[data['内部机构号'] == 965182, '金融机构代码'] = data.loc[data['内部机构号'] == 965182, '金融机构代码'].map(lambda word: str(word[:15]) + str(word[16:]))
    data['客户注册地址'] = data['客户注册地址'].map(lambda word: str(word).replace('?', '').replace('!', '').replace('^', '').replace('？', '').replace('！', ''))  # 不能包含特殊字符
    wrong_line_code = []
    data['客户地区代码'] = data['客户地区代码'].map(lambda word: match_delete(word))  # 客户地区代码这列的数字如果不在fulu/kehudiqudaima.xlsx列，则删除
    data = data[~(data['客户地区代码'].isin(wrong_line_code))]
    data['存款产品类别'] = data['存款产品类别'].map(lambda word: 'D051' if word == 'D05' else word)  # D05改成D051
    data['存款产品类别'] = data['存款产品类别'].map(lambda word: 'D061' if word == 'D06' else word)  # D06改成D061
    data['存款协议起始日期'] = data['存款协议起始日期'].mask(data['交易日期'] < data['存款协议起始日期'], data['交易日期'])  # 如果交易日期的日期小于存款协议起始日期，则把存款协议起始日期改成与交易日期一致
    data['交易对手存款账户编码'] = data['交易对手存款账户编码'].map(lambda word: str(word).replace('?', '').replace('!', '').replace('^', '').replace('？', '').replace('！', ''))  # 不能包含特殊字符
    data['交易对手证件类型'] = data['交易对手证件类型'].map(lambda word: 'A03' if word == 502 else word)  # 如果为502的改为A03
    data = data[~(data['交易对手证件类型'].isin(['B03', 'B01']))]
    data['交易对手代码'] = data['交易对手代码'].map(lambda word: str(word).replace('?', '').replace('!', '').replace('^', '').replace('？', '').replace('！', ''))  # 不能包含特殊字符
    data.loc[data['交易对手证件类型'] == 'A02', '交易对手代码'] = data.loc[data['交易对手证件类型'] == 'A02', '交易对手代码'].map(lambda word: word.replace('-', ''))  # 如果“交易对手证件类型”为A02的，去掉‘-’；
    data.loc[data['交易对手代码'].map(lambda word: len(str(word)) != 9 and len(str(word)) != 18), '交易对手证件类型'] = data.loc[data['交易对手代码'].map(lambda word: len(str(word)) != 9 and len(str(word)) != 18), '交易对手证件类型'].map(lambda word: 'A03')  # 如果去掉‘-’后长度还是不等于9位和18位的，那就把“交易对手证件类型”改为A03；
    data.loc[data['交易对手代码'].map(lambda word: word == ''), '交易对手证件类型'] = data.loc[data['交易对手代码'].map(lambda word: word == ''), '交易对手证件类型'].map(lambda word: '')  # 如果去掉‘-’后长度还是不等于9位和18位的，那就把“交易对手证件类型”改为A03；
    data['交易对手名称'] = data['交易对手名称'].map(lambda word: str(word).replace('?', '').replace('!', '').replace('^', '').replace('？', '').replace('！', ''))  # 不能包含特殊字符
    data['客户证件代码'] = data['客户证件代码'].map(lambda word: str(word).replace('-', ''))  # “客户证件代码”全部数据去掉“-”；
    data.loc[data['客户证件代码'].map(lambda word: len(str(word)) != 9), '客户证件类型'] = data.loc[data['客户证件代码'].map(lambda word: len(str(word)) != 9), '客户证件类型'].map(lambda word: 'A03')  # 不是9位的全部改成A03
    data.loc[data['客户证件代码'].map(lambda word: len(str(word)) == 18), '客户证件类型'] = data.loc[data['客户证件代码'].map(lambda word: len(str(word)) == 18), '客户证件类型'].map(lambda word: 'A01')  # “客户证件代码”18位的将对应的“客户证件类型”改为A01,
    data['客户证件代码'] = data['客户证件代码'].map(lambda word: str(word).replace('?', '').replace('!', '').replace('^', '').replace('？', '').replace('！', ''))  # 不能包含特殊字符
    data['交易渠道'] = data['交易渠道'].map(lambda word: '0' + str(word) if len(str(word)) == 1 else str(word))
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: '无' if (word == '-') or (word == '') or (word == ' ') else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: str(word)[:-1] if str(word)[-1] == '|' else str(word))  # 删除最后一个字符是‘|’
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: str(word).replace(' ', '无').replace('?', '').replace('!', '').replace('^', '').replace('？', '').replace('！', '').replace('*', '').replace('#', '').replace('＊', '').replace('＃', ''))  # 不能包含特殊字符
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: re.sub(r'[0-9]+', '', str(word)))  # 不能包含数字
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: re.sub(r'[a-zA-Z]', '', str(word)))  # 不能包含字母
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: '其他转账' if word == '转账' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B01' if word == '工程及采购' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B0101' if word == '购买煤炭类原材料' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B0102' if word == '购买石油类原材料' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B0103' if word == '购买/租赁机器设备' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B0104' if word == '购买/租赁房产' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B0105' if word == '工程款项' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B0106' if word == '保证金' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B02' if word == '费用' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B0201' if word == '电费' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B0202' if word == '水费' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B0203' if word == '燃气费' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B0204' if word == '蒸汽费' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B0205' if word == '工资/奖金' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B0206' if word == '除工资外的劳务费用' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B0207' if word == '税款' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B03' if word == '代扣、代付' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B0301' if word == '代扣电费' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B0302' if word == '代扣水费' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B0303' if word == '代扣燃气费' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B0304' if word == '代扣蒸汽费' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B0305' if word == '代发工资' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B0306' if word == '代缴税费' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B0307' if word == '代缴社保' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B04' if word == '收入' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B05' if word == '融资' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: 'B06' if word == '金融产品交易' else word)
    data['存款交易用途'] = data['存款交易用途'].map(lambda word: '无' if word == '' else word)
    data.loc[data['存款交易用途'] == 0, '存款交易用途'] = data.loc[data['存款交易用途'] == 0, '存款交易用途'].map(lambda word: '无' if word == 'A' else word)
    data.loc[data['现金转账标识'] == 1, '存款交易用途'] = data.loc[data['现金转账标识'] == 1, '存款交易用途'].map(lambda word: 'A')  # 如果现金转账标识为1，则存款交易用途改为A
    print('附注：'
          '1.删除列名'
          '2.存款发生额+存款发生金额折人民币+利率水平，这三列手动转换为数字')
    data.to_excel(r'./file_path/result.xlsx')





