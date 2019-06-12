# -*- coding:utf-8 -*-
__author__ = '朱永刚'

#内置作用域是通过一个名为 builtin 的标准模块来实现的，但是这个变量名自身并没有放入内置作用域内，
#所以必须导入这个文件才能够使用它。在Python3.0中，可以使用以下的代码来查看到底预定义了哪些变量
import builtins
print(dir(builtins))
