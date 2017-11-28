'''匹配或者搜索特定模式的文本'''

'''如果你想匹配的是字面字符串，那么你通常只需要调用基本字符串方法就行，比如
str.find() , str.endswith() , str.startswith() 或者类似的方法：'''

'''>>> text = 'yeah, but no, but yeah, but no, but yeah'
>>> # Exact match
>>> text == 'yeah'
False
>>> # Match at start or end
>>> text.startswith('yeah')
True
>>> text.endswith('no')
False
>>> # Search for the location of the first occurrence
>>> text.find('no')
10
>>>'''

'''------------------------------------------------------------------------'''

'''对于复杂的匹配需要使用正则表达式和re 模块'''

import re
test1 = '11/27/2012'
test2 = 'Nov 27,2012'

if re.match(r'\d+/\d+/\d+',test1):
    print('yes')
else:
    print('no')

if re.match(r'[A-Z][a-z][a-z]\s*\d+,\d',test2):
    print('yes')
else:
    print('no')


'''如果你想使用同一个模式去做多次匹配，你应该先将模式字符串预编译为模式对
象。比如：'''

datepat = re.compile(r'\d+/\d+/\d+')



'''match() 总是从字符串开始去匹配，如果你想查找字符串任意部分的模式出现位
置，使用findall() 方法去代替。'''

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
d = datepat.findall(text)
print(d)