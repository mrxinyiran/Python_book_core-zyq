#编写一个只接受关键字参数的函数

def recv(maxsize,*,block):
    'Receives a message'
    pass

# recv(1024,True)      --------->由于此项无关键字参数，所以在运行时则会抛出TypeError的错误

recv(1024,block=True)

# 利用这种技术，我们还能在接受任意多个位置参数的函数来指定关键字参数。比如：
def mininum(*values,clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m
a=mininum(1,5,2,-5,10)
b=mininum(1,5,2,-5,10,clip=0)
print(a,'\n',b)

funcs = [lambda x: x+n for n in range(5)]
for f in funcs:
    print(f(0))