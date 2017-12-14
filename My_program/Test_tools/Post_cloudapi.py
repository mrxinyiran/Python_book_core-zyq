# 实现两次点击，查看返回值，测试连点时使用。
from urllib import request, parse
from tkinter import *

print('Login to cloudapi')
# date1 = input('1')
# date2 = input('2')
# date3 = input('3')
# date4 = input('4')
# date5 = input('5')
# date6 = input('6')
# date7 = input('7')
# date8 = input('8')
# date9 = input('9')
# date10 = input('10')
# date11 = input('11')
# date12 = input('12')







login_data = parse.urlencode([
    # ('待输入参数1', date1),
    # ('待输入参数2', date2),
    # ('待输入参数3', date3),
    # ('待输入参数4', date4),
    # ('待输入参数5', date5),
    # ('待输入参数6', date6),
    # ('待输入参数7', date7),
    # ('待输入参数8', date8),
    # ('待输入参数9', date9),
    # ('待输入参数10', date10),
    # ('待输入参数10', date11),
    # ('待输入参数10', date12),




    # ('pagerefer', )
])

req = request.Request('http://rd.clouddev.baidu-youxi.com/material/gift.php?act=materiel&sign=123&data=eyJuYW1lIjoiXHU2ZDRiXHU4YmQ1MiIsImdpZnRfaWQiOjExMTExMTIsImdpZnRfbmFtZSI6Ilx1NmQ0Ylx1OGJkNTExMTExMiIsImdpZnRfdHlwZSI6MiwiYXBwX2lkIjozMDY3NTE1LCJnaWZ0X3N0YXR1cyI6MywiZ2lmdF9icmllZiI6Ilx1NGY2MFx1NTk3ZFx1NTU0YSIsImdpZnRfdXNhZ2UiOiIxMTExMSIsImdpZnRfYXZhaWxfc3RhcnRfZGF0ZSI6MTQ5NjgxNzgxMywiZ2lmdF9hdmFpbF9lbmRfZGF0ZSI6MTQ5NjgxNzg2MCwiZ2lmdF9jb2RlX3ZhbHVlIjoxMDAwLCJzZXJpYWxzIjpbImFhNSIsImFhNiIsImFhNyJdfQ==')

print("第一次返回结果展示：")
with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    '''date_1 = f.read().decode('utf-8')
    print('Data:', date_1)'''


req2 = request.Request('http://rd.clouddev.baidu-youxi.com/material/gift.php?act=materiel&sign=123&data=eyJuYW1lIjoiXHU2ZDRiXHU4YmQ1MiIsImdpZnRfaWQiOjExMTExMTIsImdpZnRfbmFtZSI6Ilx1NmQ0Ylx1OGJkNTExMTExMiIsImdpZnRfdHlwZSI6MiwiYXBwX2lkIjozMDY3NTE1LCJnaWZ0X3N0YXR1cyI6MywiZ2lmdF9icmllZiI6Ilx1NGY2MFx1NTk3ZFx1NTU0YSIsImdpZnRfdXNhZ2UiOiIxMTExMSIsImdpZnRfYXZhaWxfc3RhcnRfZGF0ZSI6MTQ5NjgxNzgxMywiZ2lmdF9hdmFpbF9lbmRfZGF0ZSI6MTQ5NjgxNzg2MCwiZ2lmdF9jb2RlX3ZhbHVlIjoxMDAwLCJzZXJpYWxzIjpbImFhNSIsImFhNiIsImFhNyJdfQ==')
print("第二次返回结果")
with request.urlopen(req2, data=login_data.encode('utf-8')) as g:
    print('Status:', g.status, g.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    date_2 = g.read().decode('utf-8')
    print('Data:',date_2 )


if (date_1!=date_2):
    root = Tk()
    label = Label(root, text="接口处理正确")
    label.pack()
    root.mainloop()
else:
    root = Tk()
    label = Label(root, text="接口处理错误")
    label.pack()
    root.mainloop()
