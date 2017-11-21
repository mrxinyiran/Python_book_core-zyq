prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

min_price = min(zip(prices.values(),prices.keys()))
max_price = max(zip(prices.values(),prices.keys()))

print(min_price)
print(max_price)

#对数组进行排序

sorted_price = sorted(zip(prices.values(),prices.keys()))

print(sorted_price)


prices_and_names = zip(prices.values(),prices.keys())

#z需要注意的是zip() 函数创建的是一个只能访问一次的迭代器。

print(min(prices_and_names))
# print(max(prices_and_names))