from urllib.request import urlopen


#读写以json格式编码的数据

import json
data = {
    'name':'ACME',
    'shares':100,
    'price':542.23
}
json_str = json.dumps(data)
print(json_str)
print(type(json_str))

data = json.loads(json_str)
print(type(data))



