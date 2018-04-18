# coding:utf-8
# File Name: one-2018-4-18.py
# Created Date: 2018-04-18 09:11:35
# Last modified: 2018-04-18 09:23:32
# Author: yeyong

strat = "2018-1-1" #起始时间
end = "2018-4-19"  #结束时间
universe=  DynamicUniverse("HS3000")  #证券池 , 沪深3000
benchmark = 'HS300'  #参考标准
freq = 'd'  #使用日线回测
refresh_rate = 1  #调仓频率


#账户信息
accounts = {
        'fantasy_account': AccountConfig(account_type='security', capital_base=10000000)
        }


def initialize(context):
    pass


def handle_data(context):
    previous_date = context.previous_date.strftime("%Y-%m-%d")
    #获取因子pe 的历史数据量, 截止到上一个交易日
    hist = context.history(symbol=context.get_universe(exclude_halt=True), attribute='PE', time_range=1, style="tas")[previous_date]
    #排序, 从小到大
    signal = hist['PE'].order(ascending=True)
    target_position = signal[:100].index

    
    account = context.get_account('fantasy_account')
    current_position = account.get_position(exclude_halt=True)

    for stock in set(current_position).difference(target_position):
        account.order_to(stock, 0)



    for stock in target_position:
        account.order(stock, 10000)
