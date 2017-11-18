#!/usr/bin/env python

from time import ctime, sleep

def tsfunc(func):
    def wrappedFunc():
        print '[%s] %s() called' % (
            ctime(), func.__name__)
        return func()
    return wrappedFunc

@tsfunc
def foo():
    pass

foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()



def w1(func):
    def inner():
        # 验证1
        # 验证2
        # 验证3
        return func()

    return inner


@w1
def f1():
    print 'f1'