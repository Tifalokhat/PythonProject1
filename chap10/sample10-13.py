from datetime import datetime
dt=datetime.now()
print('当前的系统时间为：',dt)

dt2=datetime(2028,8,8,20,8)
print('dt2的数据类型',type(dt2))
print('年：',dt2.year,'月：',dt2.month,'日：',dt2.day)
print('时：',dt2.hour,'分：',dt2.minute,'秒：',dt2.second)

labor_day=datetime(2028,5,1,0,0,0)
national_day=datetime(2028,10,1,0,0,0)
print('2028年5月1日比2028年10月1日早吗？',labor_day<national_day)

nowdt=datetime.now()
nowdt_str=nowdt.strftime('%Y/%m/%d %H:%M:%S')
print('nowdt的数据类型：',type(nowdt),'nowdt所表示的数据是什么？',nowdt)
print('nowdt_str的数据类型：',type(nowdt_str),'nowdt_str所表示的数据是什么？',nowdt_str)

str_datetime='2028年8月8日20点8分'
dt3=datetime.strptime(str_datetime,'%Y年%m月%d日%H点%M分')
print('str_datetime的数据类型：',type(str_datetime),'str_date所表示的数据：',str_datetime)
print('dt3的数据类型：',type(dt3),'dt3所表示的数据：',dt3)