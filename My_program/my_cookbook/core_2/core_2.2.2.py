# 字符串开头或结尾匹配

# 检查字符串开头或结尾的一个简单方法是使用str.startswith() 或者是
# str.endswith() 方法。

import os
from urllib.request import urlopen

filename = 'spam.txt'
f = filename.endswith('.txt')
print(f)

url = 'http://www.baidu.com'
u = url.startswith('http:')
print(u)

'''如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去，然后传
给startswith() 或者endswith() 方法：'''

'''------------------------------------------------------------------------------------------------'''

'''os.listdir(path='.')
返回一个list，包含给定path 目录下所有条目的名字。该list是任意顺序，不包括特殊条目'.'以及'..'，即使它们存在于目录中。

path可以是str类型或bytes类型。如果path的类型为bytes，则返回的文件名也将为bytes类型；否则，它们的类型为str。

此函数还可以支持指定一个文件描述器（file descriptor）；该文件描述器必须引用一个目录。

注要将str文件名编码为bytes，请使用fsencode()。
另请参阅scandir()函数返回目录条目以及文件属性信息，为许多常见用例提供更好的性能。'''


filename1 = os.listdir('.')
print(filename1)




def read_data(name):
    if name.startswich(('http:','https:','ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

choices = ['http:','ftp:']
url = 'http://www.baidu.com'

#TypeError: startswith first arg must be str or a tuple of str, not list
#针对上面错误，需要把choices这个列表转换为元祖，具体方法如下

c = tuple(choices)
u = url.startswith(c)
print(u)

