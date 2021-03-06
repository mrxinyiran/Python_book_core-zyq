'''fnmatch 实现shell patterns表匹配字符串或文件名

fnmatch.fnmatch(name, pattern)方法：测试name是否匹配pattern，返回true/false'''

from fnmatch import fnmatch,fnmatchcase

a = fnmatch('foo.txt','*.txt')

b= fnmatch('foo.txt','?.oo.txt')


names = ['Dat1.csv','Dat2.csv','config.ini','foo.py']
c = [name for name in names if fnmatch(name,'Dat*.csv')]

print(a,b,c)

#在windows中，fnmatch 调用了系统判断大小号匹配的规则
d = fnmatch('foo.txt','*.TXT')
print(d)

#如果我们需要精确的匹配，我们就要用fnmatchcase()方法，来完全根据我们提供的大小写来匹配

e = fnmatchcase('foo.txt','*.TXT')
print(e)

#街道地址
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

a = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print(a)

b = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
print(b)