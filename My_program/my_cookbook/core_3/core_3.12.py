# 时间转换
# from datetime import timedelta
# 
# a = timedelta(days=2,hours=6)
# b = timedelta(hours=4.5)
# c = a+b
# print(c.days)
# print(c.seconds)

#计算是否是瑞年

from datetime import datetime
from datetime import timedelta
a = input('请输入年月日：')
a = datetime(2012,3,1)
b = datetime(2012,2,28)
c = a-b
d=c.days