# -*- coding:utf-8 -*-
__author__ = '朱永刚'


class Student(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


class Student2(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


class Screen(object):
    @property
    def width(self):
        # 此处使用self._width
        # 一是设为私有变量。二是表示这个是个属性，而非方法。
        return self._width

    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width


s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

s = Student()
s.set_score(60)
print(s.get_score())

s2 = Student2()
s2.score = 99
print(s2.score)

class A(object):
    @property
    def S(self):
        return self._S

    @S.setter
    def S(self,value):
        self._S = value

a = A()

a.S = 22
print(a.S)