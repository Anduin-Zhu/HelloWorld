# -*- coding:utf-8 -*-
__author__ = '朱永刚'

class Chain(object):

    def __init__(self, path='',age=12):
        self._path = path
        self._age = age
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __len__(self):
        return len(self._path)

    def __str__(self):
        return self._path

    __repr__ = __str__



# print(Chain().status.user.timeline.list)
#
# ccc = Chain("111",222)
# print(len(ccc))

class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1 # 初始化两个计数器

    def __iter__(self):
        return self # 实例本身就是迭代对象，所以返回自己

    def __next__(self):
        self.a,self.b = self.b,self.a + self.b # 计算下一个值
        if self.a > 1000: # 退出循环条件
            raise  StopIteration()
        return self.a

# for i in Fib():
#     print(i)


class Fib2(object):
    def __getitem__(self, n):
        if isinstance(n,int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            step = n.step
            if start is None:
                start = 0
            a,b = 1,1
            L = []
            for i in range(stop):
                if i >= start:
                    L.append(a)
                a,b = b,a + b
            return L

f = Fib2()
print(f[23:55])