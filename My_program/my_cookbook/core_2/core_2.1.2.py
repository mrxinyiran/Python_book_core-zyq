#使用多个界定符分割字符串

'''string 对象的split() 方法只适应于非常简单的字符串分割情形，它并不允许有
多个分隔符或者是分隔符周围不确定的空格。当你需要更加灵活的切割字符串的时候，
最好使用re.split() 方'''

import re
line = 'asdf fjdk; afed, fjek,asdf,   foo'
parts = re.split(r'[;,\s]\s*',line)
print(parts)


fields = re.split(r'(;|,|\s)\s*',line)
print(fields)


values = fields[::2]
print(values)

delimiters = fields[1::2]
print(delimiters)


parts = re.split(r'(?:,|;|\s)\s*', line)
print(parts)