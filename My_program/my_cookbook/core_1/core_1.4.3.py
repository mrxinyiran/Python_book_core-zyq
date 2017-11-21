import heapq

#8.5. heapq - 堆队列算法
# 源代码： Lib / heapq.py
# 该模块提供了堆队列算法的实现，也称为优先级队列算法。

nums = [1,8,2,23,7,-4,18,23,42,37,2]
heap = list(nums)

#将列表nums以堆的顺序排序
heapq.heapify(heap)

print(heap)     #打印出以堆排序的列表

# eapq.heappop(heap)
# 从heap中弹出并返回最小的项，保持堆不变。如果堆为空，则会引发IndexError。要访问最小的项，不需要弹出它，请使用heap [0]。

heap2=list(nums)

#从heap中弹出并返回最小的项，heap2中
print(heapq.heappop(heap2))
print(heap2)
