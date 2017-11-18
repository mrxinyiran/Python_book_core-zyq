# records = [('foo,1,2'),
#            ('bar','hello'),
#            ('foo',3,4),
#            ]
# def do_foo(x,y):
#     print ('foo',x,y)
#
# def do_bar(s):
#     print ('bar',s)
#
# for tag, *args in records:
#     if tag == 'foo':
#         do_foo(*args)
#     elif tag == 'bar':
#         do_bar(*args)



# 递归算法

# sum(iterable[, start])
# 将start以及iterable的元素从左向右相加并返回总和。start默认为0。iterable的元素通常是数字，start值不允许是一个字符串。


items = [1,10,7,4,5,9]
head,*tail = items

def sum(items):
    head,*tail = items
    return head + sum(tail) if tail else head
print(sum(items))


