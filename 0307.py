import akshare as ak

# 股票信息
# data = ak.stock_individual_info_em(symbol="000692")
# print(data)

# 实时行情数据  全部股票的近期数据 沪深京 A 股
# 沪 A 股 接口: stock_sh_a_spot_em
# 深 A 股 接口: stock_sz_a_spot_em
# 京 A 股 接口: stock_bj_a_spot_em
# 新股 接口: stock_new_a_spot_em
# 风险警示板 接口: stock_zh_a_st_em
# 股票指数 接口: stock_zh_index_spot

# 历史行情数据-东财 接口: stock_zh_a_hist
# symbol	str	symbol='603777'; 股票代码可以在 ak.stock_zh_a_spot_em() 中获取
# period	str	period='daily'; choice of {'daily', 'weekly', 'monthly'}
# start_date	str	start_date='20210301'; 开始查询的日期
# end_date	str	end_date='20210616'; 结束查询的日期
# adjust	str	默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据

# 历史指数行情数据-新浪 接口: stock_zh_index_daily
# 腾讯 接口: stock_zh_index_daily_tx
# symbol	str	symbol="sz399552"

# 分时数据-新浪 接口: stock_zh_a_minute
# symbol	str	symbol='sh000300'; 同日频率数据接口
# period	str	period='1'; 获取 1, 5, 15, 30, 60 分钟的数据频率
# adjust	str	adjust=""; 默认为空: 返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据;

# 分时数据-东财 接口: stock_zh_a_hist_min_em
# symbol	str	symbol='sh000300'; 股票代码
# start_date	str	start_date="1979-09-01 09:32:00"; 日期时间; 默认返回所有数据
# end_date	str	end_date="2222-01-01 09:32:00"; 日期时间; 默认返回所有数据
# period	str	period='5'; choice of {'1', '5', '15', '30', '60'}; 其中 1 分钟数据返回近 5 个交易日数据且不复权
# adjust	str	adjust=''; choice of {'', 'qfq', 'hfq'}; '': 不复权, 'qfq': 前复权, 'hfq': 后复权, 其中 1 分钟数据返回近 5 个交易日数据且不复权

# 千股千评 接口: stock_comment_em

# 个股排行 接口: stock_hsgt_hold_stock_em
# market	str	market="沪股通"; choice of {"北向", "沪股通", "深股通"}
# indicator	str	indicator="沪股通"; choice of {"今日排行", "3日排行", "5日排行", "10日排行", "月排行", "季排行", "年排行"}

# 行业资金流  接口: stock_fund_flow_industry
# symbol	str	symbol="即时"; choice of {“即时”, "3日排行", "5日排行", "10日排行", "20日排行"}

# 个股资金流  接口: stock_individual_fund_flow
# stock	str	stock="000425"; 股票代码
# market	str	market="sh"; 上海证券交易所: sh, 深证证券交易所: sz, 北京证券交易所: bj

# 大盘资金流  接口: stock_market_fund_flow

# 同花顺-成份股-概念名称  接口: stock_board_concept_cons_ths
# symbol	str	symbol="阿里巴巴概念"; 可以通过调用 ak.stock_board_concept_name_ths() 查看同花顺的所有概念名称; 注意：其中 "国家大基金持股" 为 "国家大基金持股 ", 最后有一个空格

# 同花顺-成份股-行业名称  接口: stock_board_industry_cons_ths
# symbol	str	symbol="半导体及元件"; 可以通过调用 ak.stock_board_industry_name_ths() 查看同花顺的所有行业名称

# 东方财富-行业板块  接口: stock_board_industry_name_em

# 盘口异动  接口: stock_changes_em
# symbol	str	symbol="大笔买入"; choice of {'火箭发射', '快速反弹', '大笔买入', '封涨停板', '打开跌停板', '有大买盘', '竞价上涨', '高开5日线', '向上缺口', '60日新高', '60日大幅上涨', '加速下跌', '高台跳水', '大笔卖出', '封跌停板', '打开涨停板', '有大卖盘', '竞价下跌', '低开5日线', '向下缺口', '60日新低', '60日大幅下跌'}


# 涨停股池  接口: stock_zt_pool_em
# date	str	date='20210525'

# 昨日涨停股池  接口: stock_zt_pool_previous_em
# date	str	date='20210525'

# 强势股池  接口: stock_zt_pool_strong_em
# date	str	date='20210525'

# 次新股池  接口: stock_zt_pool_sub_new_em
# date	str	date='20210525'

# 跌停股池  接口: stock_zt_pool_dtgc_em
# date	str	date='20210525'

# 创新高  接口：stock_rank_cxg_ths
# symbol	str	symbol="创月新高"; choice of {"创月新高", "半年新高", "一年新高", "历史新高"}

# 创新低  接口：stock_rank_cxd_ths
# symbol	str	symbol="创月新高"; choice of {"创月新高", "半年新高", "一年新高", "历史新高"}

# 连续上涨  接口：stock_rank_lxsz_ths

# 连续下跌  接口：stock_rank_lxxd_ths

# 持续放量  接口: stock_rank_cxfl_ths

# 持续缩量  接口: stock_rank_cxsl_ths

# 向上突破  接口: stock_rank_xstp_ths
# symbol	str	symbol="500日均线"; choice of {"5日均线", "10日均线", "20日均线", "30日均线", "60日均线", "90日均线", "250日均线", "500日均线"}

# 量价齐升  接口: stock_rank_ljqs_ths

# 货币报价最新数据  接口: currency_latest

# 货币对价格转换  接口: currency_convert
# base	str	Y	base="USD"; 基础货币
# to	str	Y	to="CNY"; 需要转换到的货币
# amount	str	Y	amount="10000"; 转换量
# api_key	str	Y	api_key="Please put your api key here"; you can register currencyscoop, Gmail well be better

data = ak.stock_zh_a_spot_em()

print(data)