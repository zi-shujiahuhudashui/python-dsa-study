# -----python从入门到精通-----

# -----------------------------

# 输入输入
# a=float(2.67)
# print(a)
# a=input('输入一个数字')
# print(a)
# a=range(1,100,20)
# print(a[0])
# s='qwe'
# its=iter(s)
# print(its)
import json

# -------------------------------

# 列表
# list=[1,23,45,6,7]
# print(list[1::2])
# newlist=list[:]
# print(newlist)
# newlist=newlist*2
# print(newlist)
# a=1 in newlist
# print(a)
# # b=list[1] is newlist[1]
# # print(b)
# # for i in (newlist):
# #  print(i)
# list.sort(reverse=True)
# print(list)
# # 多维列表
# list=[[1,2,2],[2,34,5],[3,4,5]]
# list2=[elem for num in list for elem in num]
# print(list2)

# ---------------------------------

# 元组
# t1=(12,234,4,5.2j,7)
# print(t1)
# t2=(6,)
# print(t1[2])
# del t1

# ---------------------------------

# 集合
# set1={1,2,3,4,6}
# set1.add(4)
# set1.update({4,5,6})
# set1.update([9,8])
# set1.discard(5)
# set1.remove(1)
# set2={1,2,3,4,5}
# print(set1&set2)
# print(set1|set2)
# print(set1^set2)
# print(set2-set1)
# print(1 in set1)
# print(set1.issubset(set2))
# print(len(set1))
# issuperset

# ----------------------------------------

# 字典
# dict0={'a':1,'b':2,'c':3}
# print(dict0)
# dict1={1:'a',2:'b',3:[1,2,3]}
# print(dict1)
# list1=[1,2,3]
# list2=['a','b','c']
# dict2=dict(zip(list1,list2))
# print(dict2)
# print(len(dict2))
# print(dict2[3])
# dict2[3]='abn'
# dict2[4]='qq'
# del dict2[3]
# print(dict2)
# print(dict1)
# print(2 in dict1)
# str1=str(dict1)
# print(str1)
# print(dict0.get('g'))
# print(dict0['a'])
# print(dict0.keys())
# print(dict0.items())
# print(dict0.values())
# dict2={1:'a',2:'b',3:[1,2,4]}
# print(dict1)
# print(dict2)
# dict1.update(dict2)
# print(dict1.pop(2))
# print(dict1)
# dict1=dict2
# dict2.clear()
# print(dict1)
# print(dict2)
# dict1=dict2.copy()
# print(dict1)
# import copy
# dict1=copy.deepcopy(dict2)
# print(dict1)
# for i in dict1:
# print(f"{i}:{dict1[i]}",end=',')
# print(dict2)
# for i in dict2.items(): #遍历的是值键对
#     print(i,end=',')
# for j in dict2.values(): #遍历的是值
#     print(j, end=',')
# for k in dict2: #遍历的是键
#     print(k)
# list1=['1','2','3']
# print(str(list1))
# print(''.join(list1))

# -------------------------------------------

# 数组
# import numpy as np
# a1=np.array([[1,2],[3,4]])
# print(a1)
# a2=np.zeros(shape=(2,2))
# print(a2)
# a2=np.zeros(6)
# print(a2)
# a2=np.ones(shape=(2,2))
# print(a2)
# a2=np.empty((2,3))
# print(a2)
# a2=np.arange(2,6,2)
# a2=np.linspace(1,5,4)
# print(a2)
# a2=np.array([[5,6],[7,8]])
#b6 a0=np.hstack((a1,a2))
# a0=np.vstack((a1,a2))
# a0=a2+a1
# print(a0.ndim)
# print(a0.size)
# print(a0.dtype)
# a1=np.delete(a1,1,axis=0)
# print(a1)
# b1=np.ones((3,2))
# b1=b1*a1
# b1=b1+a1
# print(b1)

# ----------------------------

# 矩阵
# import numpy as np
# import random
# m=np.mat('1 2;'
#          '3 4')
# n=np.mat('3 4;'
#          '5 6')
# print(m)
# a=np.random.randint(2,10,size=(3,3))
# print(a)
# c=np.ones((3,3),dtype=int)
#
# print(c)
# c=a*c
# print(c)
# c=c@a
# print(c)
# print(6666)
# c=np.multiply(a,c)
# print(c)
# # 矩阵的转置
# c=c.T
# print(c)
# # 矩阵的逆
# c=np.linalg.inv(c)
# print(c)
# # 矩阵的共轭
# c=np.conjugate(c)
# print(c)
# sum=np.sum(m[1,:])
# print(sum)
# print(np.max(m))
# print(m.max())
# print(np.argmax(m[1,:]))
# print(m.shape)
# print(m.max())
# print(m*n)
# print(m@n)
# m=np.array([[1,2],
#            [3,4]])
# n=np.array([[3,4],
#            [5,6]])
# print(m*n)
# print(m@n)

# ---------------------------------------

# 字符串
# '''这是注释吗'''
# print('''这是注释吗\nduide''')
# print('')
# print('duied')
# import string
# print(string.digits)
# print(string.printable)
# print('这个是字符串:%sduiba'%'zifuchuang')
# print('这个也是字符串:%sduiba'%2)
# print('这个也是字符串:%dduiba'%-1)
# print('这个也是字符串:%iduiba'%2)
# print('Hello wer2vtorld'>'hello world')

# ------------------------------------

# 函数
# def hanshuming(a,b):
#     return a+b
# print(hanshuming(1,2))
#
# def funbefore(func):
#     def test(*args1,**args2):
#         print('Before')
#         result = func(*args1,**args2)
#         return result
#     return test
# def funafter(func):
#     def test(*args1,**args2):
#         result = func(*args1, **args2)
#         print('After')
#         return result
#     return test
# @funbefore
# @funafter
# def hanshuming(a,b):
#     print(a+b)
#     return a+b
# print(hanshuming(1,2))
#
# lst=[1,-2,3,-4]
# def func(val):
#     if val%2==0:
#         val=val*2
#     else:
#         val=val*3
#     return val
# print([func(val)+1 for val in lst if val>0])
# def poutkx(**x):
#     for items in x.items():
#         print(items)
# poutkx(a=1,b=2)
# def dout(d):
#     for items in d.items():
#         print(items)
# d={'a':1,'b':2}
# dout(d)
# def fact2(n):
#     if n==0:
#         return 1
#     else:
#         s=n*fact2(n-1)
#         print('s=',s)
#         return s
# num=int(input('n='))
# print(f"{num}!={fact2(num)}")
# print(fact2)

# -----------------------------------------

# 类与对象（简化版）
# 1. 定义“类”（画那张空表）
# class Patient:
#     # __init__ 就是“初始化”，相当于把表格发给新病人让他填
#     def __init__(self, name, age, illness):
#         self.name = name      # 填姓名
#         self.age = age        # 填年龄
#         self.illness = illness # 填病因
#
#     # 类里还可以定义“动作”（方法），比如：
#     def introduce(self):
#         return f"我是{self.name}，得了{self.illness}"
#
# # 2. 创建“对象”（让小明和小红各自填表）
# xiaoming = Patient("小明", 20, "骨折")  # 现在 xiaoming 就是一个对象
# xiaohong = Patient("小红", 22, "感冒")
#
# # 3. 用起来
# print(xiaoming.name)      # 输出：小明
# print(xiaohong.introduce()) # 输出：我是小红，得了感冒

# -----------------------------

# 文件操作
# file：文件的路径  mode:文件的打开模式  buffering：文件缓冲
# encoding：对应的文件数据流的编码
# errors：在文件的读/写问题过程中出现编码问题时，该以什么样的方式进行处理，errors参数只能在文本模式下使用
# r:读取
# w:写入,如果文件不存在，则创建一个新文件，如已存在，使用w打开文件时，会清空文件的内容
# x:创建一个新文件
# a:打开文件时不会清空文件的内容，在文件尾部追加内容
# b:二进制模式，读/写的是二进制数据
# t:读/写的是文本数据，文件默认的打开类型为文本文件类型

# file_stream = open("test.txt","w")
# file_stream.write("hello world")
# file_stream.close()
# file_stream = open("test.txt","r")
# file_content = file_stream.read()
# file_stream.seek(0,0)
# print(file_stream.read())
# file_stream.close()
# print(file_content)
# print("file_content is:{}".format(file_content))
# file_stream = open("test.txt","r")
# for line in file_stream:   # 逐行读取
#     print(line)

# 在python中使用open()函数来获取一个文件流对象，如果打开失败，会引发一个IOError异常
# python文件的默认读/写方式为文本模式

# --------------------------------

# json文件序列化
# JOSN 是一种轻量的数据交换格式，采用完全独立于编程语言的文本格式来存储和表示数据。是理想的数据交换语言
# JSON文件是一种文本文件
# JSON格式中的键名必须是字符串类型，键名要用双引号引起来
# JSON格式用{}来表示一个对象。语法类似python的字典结构，只不过对象中的键名必须是字符串类型
# import json
# {"age":18}
# a=1
# print(json.dumps(a))    # python数据对象转换为json字符串
# print(json.loads('1'))     # json字符串转换为python数据对象
# print(a)
# a=json.dumps(a)
# print(json.dumps(a))

# -----------------------------------
#
# 面向对象/类
# 对象是一个宽泛的对象，一切你能想到的都可以称为对象
# 在面向对象中，抽象后的数据类型就叫做类
# 面向对象具备三大特征：封装，继承和多态
#
# 类是将具有共同特征的事物进行抽象，是用户定义的数据类型。对象是该数据类型的一个具体实现
# 类相当于 “自带数据的函数集合”
#
# 定义一个Computer类
# class Computer:
#     modules={'cpu','内存'}     # 类属性
# print(Computer.modules)
#     @classmethod     #这是 Python 的一个内置装饰器。加上它，就代表这个方法是“属于类的”
#     def output_modules(cls):         # 普通方法：第一个参数是 self（指向具体的实例对象）
#         for modules in cls.modules:# 类方法：第一个参数是 cls（指向类本身）
#             print(modules)
# Computer.output_modules()
#
# python通过在类的成员方法中声明一个self形参来表示当前方法是一个对象方法
# 定义对象方法，对象方法的第一个形参必须指明为self
#     def sum(self,number1,number2):
#        sum=number1+number2
#        return sum
# 对类Computer进行实例化，获得computer对象
# computer=Computer()
# print(computer.sum(1,2))
# 类的构造方法，用来对对象执行初始化
#     def __init__(self,name):
#         # 定义对象属性并初始化
#         # self.__name=name
#         self.name=name
#     def name1(self):
#         print(self.name)
# computer=Computer("小明")
# computer.name1()
# 静态方法的修饰符是@staticmethon
'''
定义类方法的时候须指明cls形参，定义对象方法时需要指明self形参。
静态方法与类方法不同之处在于，定义静态方法时无需指明任何描述类的形参。
'''
'''
静态方法就是你放在类里面的“普通函数”
'''
# 类的继承
# class Dog:
#     # 定义类属性
#     spacies='Canidae'
#     @classmethod
#     def gnaw(cls):
#         print('now starting gnaw the bone!')
#     # 定义对象方法
#     def cry(self):
#         print('dong never cry!')
# class Alaska(Dog):  #继承
#     pass
# alaska=Alaska()  # 实例化
# # alaska 能访问父类的类方法gnaw()以及对象方法cry()
# alaska.gnaw()
# alaska.cry()
# print(issubclass(Dog, Alaska))  # 判断Dog是否是Alaska的子类
# print(issubclass(Alaska, Dog))  # 判断Alaska是否是Dog的子类
'''
1，在python中通过class关键字来定义一个类
2，类属性与方法为所有实例对象所共享
3，使用@classmethod修饰符来定义一个类方法，使用@staticmethod来定义一个静态方法
4，在python中通过__init__()构造方法来对对象进行实例化
5，子类对继承的父类方法进行定义以后，会覆盖父类的方法，可以通过super类来访问父类的方法
6，super类实质是在类型的MRO中查找特定的类型，然后以代理的方式来调用父类的方法
'''
# 属性装饰器
# 代码对比
# class Person:
#     def __init__(self, birth):
#         self.birth = birth
#     # 不加 @property 的情况（普通方法）
#     def get_age(self):
#         return 2026 - self.birth
# p = Person(2000)
# print(p.get_age())  # 必须加括号，像在“执行动作”
# class Person:
#     def __init__(self, birth):
#         self.birth = birth
#     @property
#     def age(self):  # 名字叫 age，不再是 get_age
#         return 2026 - self.birth
# p = Person(2000)
# print(p.age)  # 不用括号！像取变量一样干净
#
# # 定义一个类装饰器（接收类，返回类）
# def add_version(cls):
#     cls.version = "1.0"   # 给这个类贴上一个类属性
#     return cls
# # 使用：放在 class 定义上面
# @add_version
# class MyStack:
#     def __init__(self):
#         self.data = []
# print(MyStack.version)  # 输出：1.0 （自动被添加上了！）
#
# ---------------------
#
# # git
# origin:表示远程仓库
# master:表示主分支
# HEAD:表示指向当前工作分支的当前版本(最新)
# git pull # 拉取 合并远程和当前分支
# git push # 推送 合并远程和当前分支
# git branch # 查看分支列表
# git log # 查看版本的提交历史
# git add . # 将当前目录的所有修改添加至暂存区
# git commit -m"" # 将暂存区的文件提交至git中
# git checkout: # 切换到主分支

# -------------------------

# python异常处理
# Python中的异常是一种数据类型，可以理解为将各种异常进行了抽象
# try:
#     # 可能发生的异常的代码块
#     # 注意代码的缩进规则
#     pass
# except Exception :
#     # except语句负责捕捉异常，语句下方的代码块用来对异常进行处理
#     pass
# except:
#     # 此时的except语句表示捕捉任何异常类型
#     pass
# else:
#     # else语句不是必须的
#     pass
# # python 提供来简化写法，可以将多个异常作为元祖类型，使得except语句中可以同时对多个
# # 异常进行捕获，对元组类型也可以起别名
# try:
#     pass
# except(NameError,ValueError,Exception)as e:
#     print(e)

# ----------------------------------

# python模块
# 一个python文件可以称为是一个模块

# Python包
# 是一种目录结构，相当于模块的集合，每一个包中一定要有__init__.py这样一个文件














