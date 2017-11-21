# 在字典中将键映射到多个值上

'''一个字典就是一个键对应一个单值的映射。如果你想要一个键映射多个值，那么你
就需要将这多个值放到另外的容器中，比如列表或者集合里面。比如，你可以像下面
这样构造这样的字典：'''

d = {
    'a':[1,2,3],
    'b':[4,5]
}

e = {
    'a':{1,2,3},
    'b':{4,5}
}

'''如果你想保持元素的插入顺序就应该
使用列表，如果想去掉重复元素就使用集合（并且不关心元素的顺序问题）。'''

'''可以很方便的使用collections 模块中的defaultdict 来构造这样的字典。
defaultdict 的一个特征是它会自动初始化每个key 刚开始对应的值，所以你只需要
关注添加元素操作'''

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)

e = defaultdict(set)
e['a'].add(1)
e['a'].add(2)
e['b'].add(4)

print(e)
