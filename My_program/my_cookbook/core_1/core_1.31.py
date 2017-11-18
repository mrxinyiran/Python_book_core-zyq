from collections import deque

# 8.3. collections — 容器数据类型
# 源代码： Lib/collections/__init__.py
#
# 这个模块实现了专业的容器数据类型用来替代Python的通用内置容器，字典, 列表, 集合, 和 元组.
#
# deque(双向队列)	一个能在“队列”两端快速出队、入队的，类似于队列的（list-like）的容器 (译者注:就是双向队列)

def search(lines,pattern,history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line,prevlines in search(f, 'python',5):
            for pline in prevlines:
                print(pline,end='')
            print(line,end='')
            print('-',20)