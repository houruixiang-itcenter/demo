#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：Demo.py

'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

"""
python 格式  输入输出
"""


class hallo:
    def __init__(self):
        pass

    if True:
        print "Answer"
        print "True"
        import sys;
        x = 'runoob';
        sys.stdout.write(x + '\n')
    else:
        print "Answer"
        # 没有严格缩进，在执行时会报错
    print "False"
    x = 'a'
    y = 'b'
    # python默认输出是换行的, 如果不换行需要在末尾加”, ”
    print x
    print y
    print x, y
    print x,
    print y,
    print "------------------------"
    if x.__eq__(y):
        print "==="
    else:
        print "!="
    print "LALO"
    # 像if、while 、def和class这样的复合语句，首行以关键字开始，以冒号(: )
    #     结束，该行之后的一行或多行代码构成代码组。
    #
    # 我们将首行及后面的代码组称为一个子句(clause)。
    expression = True
    uint = False
    if expression:
        print "expression"
    elif uint:
        print "uint"
    else:
        print "life is short i use python"
    print "你好你好"

    # -*- coding: UTF-8 -*-
    print "你好，世界";
    print('100 + 200 =', 100 + 200);
    name = input()
    print('hello,', name)
