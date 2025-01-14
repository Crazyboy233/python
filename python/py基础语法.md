# 基础语法

## 输入

~~~python
name = input("请输入姓名：") # input输入的类型默认为字符串
~~~

## 转义字符

~~~python
\r #回车，表示将当前位置移到本行开头
print("Hello\rworld")
#输出world

print(r"hello\tworld") #字符串前加r，表示字符串中的内容不进行转义
~~~

## if-else

~~~python
if age < 18:
    print("未成年禁止入内")
    
if a == 1 and b == 2:
    print(not 3 < 9) #not 表示取反

#if 条件:
#    print()
#else:
#	 print()

#三目运算
print("a小于等于b") if a < b else print("a大于b")

#if-elif
~~~

## 循环

~~~python
while True:
   print() 

#for 临时变量 in 可迭代对象:
#    循环体

#range函数
range(start, stop, step)

for i in range(1, 6) #从1开始，到6结束。包前不包后，打印1-5
	print(i)
~~~

## 字符串和编码解码

~~~python
a = "hello"
str1 = a.encode()
str2 = a.encode("utf-8")
str3 = a.decode

# *重复输出
print("hello" * 100) # 输出100遍hello

# 成员运算符
# in 如果包含了某个字符串，返回True，否则返回False
# not in 不包含的话。返回True，包含返回False
str = "hello" 
print('h' in str) # True

# 切片：指对操作的对象截取一部分的操作
# 语法：[开始位置:结束位置:步长]
# 包前不包后
str = "abcdefghijk"
print(str[0:3]) #输出abc
print(str[-1:]) #输出k
print(str[:-1]) #输出abcdefghij
print(str[-1:-5]) #无输出
# 步长：表示选取间隔，不写步长 默认为1
# 步长的绝对值大小决定切取的间隔，正负号决定切取方向
# 正数表示从左往右取值，负数表示从右往左取值
print(str[-1::-1]) #输出kjigfedcba
print(str[-1:-5:-1]) #输出kjih
print(str[0:7:2]) #输出aceg
~~~

## 字符串的查找

~~~python
# find :检测某个字符串是否包含在字符串中，如果在就返回这个字符串开始位置的下标，否则返回-1
# find（子字符串，开始位置下标，结束位置下标） //包前不包后
# 注意：开始和结束位置下标可以省略，表示在整个字符串中查找
name = 'bingbing'
print(name.find('i')) # 1
print(name.find('bing')) # 0
print(name.find('b', 3)) # 4
print(name.find('b', 5)) # -1
print(name.find('b', 3, 5)) # 0

# index():检测某个子字符串是否包含在字符串中，如果在，就返回这个字符串开始位置的下标，否则就会报错
# index(子字符串，开始位置下标，结束位置下标)

# count():返回某个子字符串在整个字符串中出现的次数，没有就返回0
# count(子字符串，开始位置下标，结束位置下标)

#lower() upper() 字母转大小写
str.lower()

# startwith():是否以某个字符串开头，是的话就返回True，不是的话就返回False。如果设置了开始位置和结束位置下标，则在指定范围内检查
# endwith():是否以某个字符串结尾，是的话就返回True，不是的话就返回False。如果设置了开始位置和结束位置下标，则在指定范围内检查

# replace():替换
# replace(旧内容，新内容，替换次数)
# 替换次数不写地话全部替换，否则替换前n个旧内容

# split():指定分隔符来切字符串
str.split(',')

# capitalize():第一个字符大写，其他都小写 算是对字符串的一个格式化
str.capitalize()
~~~

## 列表

可迭代对象（可以for循环迭代取值）：列表，字符串

~~~python
# 列表名 = [元素1， 元素2， 元素3...]
# 元素与元素之间用逗号隔开，元素的类型可以不同
li = [1, 2, 3]
# 列表也可以切片
print(li[0:2]) # [1, 2]
print(li[0:2]) # [1, 2]
# 列表的常见操作 append(), extend(), insert()
li.append("four")
li.extend("five") # 分散添加，将一个个元素添加
li.insert(2,"six") # 在指定下标位置插入元素
# li.extend(4) 会报错，extend里面的参数必须是可迭代对象
print(li)
# 可以通过下标直接修改
li[2] = 0
print(li)
# 查找元素
# in 存在返回True ，not in 不存在返回True
print(2 in li)

#列表同样适用index和count
# index():检测某个子字符串是否包含在字符串中，如果在，就返回这个字符串开始位置的下标，否则就会报错
# index(子字符串，开始位置下标，结束位置下标)
# count():返回某个子字符串在整个字符串中出现的次数，没有就返回0
# count(子字符串，开始位置下标，结束位置下标)

# 删除元素
# del li # 删除列表
del li[2]
# pop ：删除指定下标的元素，Python3默认删除最后一个元素
li.pop() # 删除最后一个元素
li.pop(2) # 删除下标为2的元素
print(li)
# remove : 根据元素的值删除元素
li.remove('f') # 默认删除最开始出现的第一个元素，如果列表中不存在该元素则报错
print(li)

# 排序
# sort() 默认从小到大排序
li1 = [1, 2, 3, 4, 5, 4, 7, 2, 11, 10]
li1.sort()
li1.reverse() # 倒序
print(li1)

# 列表推导式
# [表达式 for 变量 in 列表]
# in后面不仅可以放列表，还可以放range函数或者可迭代对象
li2 = [1, 2, 3, 4, 5]
[print(i * 2) for i in li2] # 前面的i是表达式
[li2.append(1) for i in range(1,6)]
print(li2)
# [表达式 for 变量 in 列表 if 条件]

# 列表嵌套
li4 = [1, 2, [3, 4, 5]] # [3,4,5] 是内层列表
print(li4[2][0])
~~~

## 元组

~~~python
# 元组
# 元组名 = (元素1, 元素2...)
tua = (1, 2, 3, 'b', 'a')
tua1 = (1,) # 只有一个元素要加逗号
tua2 = () # 空元组
print(type(tua))

# count(元素)该元素出现的次数 index(元素)该值的下标 len(元组名)元组的长度 和列表的用法相同
# 元组同样支持切片操作
print(tua[2:])
# 应用场景：函数的参数和返回值，
# 格式化输出后面的()本质上就是一个元组

# 字典 存放键值对，键具有唯一性，值可以重复
# 字典名 = [键1:值1, 键2:值2]
dict = {'hello': '1', 'world' : 2} # 类型为dict
print(dict['hello'])

# 查看元素 变量名[键名]
# 不可以根据下标
print(dict['world']) #键名不存在时报错
# 变量名.get()
print(dict.get('nihao', '不存在'))

# 修改元素
dict['hello'] = 20
print(dict['hello'])

# 新增元素
# 有键名就修改，不存在就新增
dict['你好'] = 22
print(dict['你好'])

# 删除元素
# del
# del dict # 删除整个字典
del dict['hello'] # 删除时没有指定的键就报错
print(dict)

# clear 清空字典内容，但是保留字典
# dict.clear()
# print(dict)

# pop() 删除指定键值对
dict.pop('你好')
print(dict)
# dict.pop() # 没有指定键名报错
dict.popitem() # 默认删除最后一个键值对 3.7之前的版本是随机删除一个键值对

# # 求长度 len(字典名)
# dic = {'hello': '1', 'world' : 2}
# print(len(dic))
# # 返回字典里面包含所有键名的列表 keys()
# print(dic.keys())
# for key in dic.keys(): # 只取出键名
#     print(key)
# # 返回字典里面包含所有值的列表 values()
# print(dic.values())
# for value in dic.values(): print(value)
# # 返回字典里面包含所有键值对（元组类型）的列表 items()
# print(dic.items())
# for i in dic.items():
#     print(i)

# # 集合 s1 = {1, 2, 3}
# # 1、集合是无序的（涉及hash表），里面的元素是唯一的 2、可以用于元组和列表去重
# s1 = {} # 定义空字典
# s2 = set() # 定义空集合
# # python中int类型的hash值就是它本身，在hash表中的位置不会改变。
# print(hash(1))
# # 用引号括起来整型变成了字符串类型，所以hash值会改变
# print(hash('a'))
#
# # 集合常用操作
# # 添加的是一个整体 add()
# s = {1,2,3,4}
# s.add('a')
# s.add((5,6))
# print(s)
# # 把传入的元素拆分，个个放入集合中 update() 参数必须是可迭代对象
# s.update((7,8,9))
# print(s)
# # 选择数字有就删除，没有就报错 remove()
# s.remove('a')
# print(s)
# # 进行无需排列，然后将左边第一个元素删除 pop()
# s.pop()
# print(s)
# # 选择元素删除，有就删，没有不进行任何操作 discard()
# s.discard(8)
# print(s)

# 交集和并集 &
a = {1,2,3,4}
b = {3,4,5,6}
print(a & b) # 交集
print(a | b) # 并集
~~~



### 元组和列表的区别

元组只有1个元素时需要加逗号，列表不需要

元组只支持查询操作，不支持增删改操作。

## 类型转换

~~~python
# 类型转换
# int(x) # 将x转换为一个整数
# float(x) # 将x转换为一个浮点数
# str(x) # 将x转换为一个字符串

# eval(str) # 用来计算在字符串中的有效python表达式，并返回一个对象
print(eval('10+10')) # 输出20
# eval()可以实现list，dict，tuple，str之间的转换
# eval() 不安全，容易恶意修改数据
# str -> list
# st1 = "[[1,2],[3,4],[5,6]]"
# li = eval(st1)
# print(type(li))

# tuple(s) # 将序列s转换为一个元组
# list(s) # 将序列s转换为一个列表
# str -> list
print(list('abcdefg'))
#tuple -> list
print(list((1,2,3,4)))
# dict -> list
print(list({'name' : 'mpt', 'age' : 18})) # 字典转列表只取键名
# set -> list
print(list({'a','b','c'})) # 先去重，在转换
# chr(x) # 将一个整数转换为一个字符
~~~

## 深浅拷贝

```python
# ！！！！！！！！！！！赋值：完全共享资源，一个值的改变会影响其他值的改变！！！！！！！！
# 浅拷贝 拷贝外层的对象，内部元素只拷贝一个引用
# 会创建新的对象，拷贝第一层的数据，嵌套会指向原来的内存地址
# import copy # 导入copy模块
# li = [1,2,3,[4,5,6]] # 嵌套列表
# li2 = copy.copy(li)
# print('li:',li)
# print('li2:',li2)
# # 查看内存地址 id()
# print(id(li),id(li2)) # 地址不同，浅拷贝
# li.append(7)
# print('li:',li)
# print('li2:',li2)
# print(id(li[3]),id(li2[3])) # 外层地址不同，内层地址相同

# 深拷贝 外层对象和内部元素都拷贝一遍
# 数据完全不共享，外层对象和内部元素都拷贝一遍
# import copy # 导入copy模块
# li = [1,2,3,[4,5,6]] # 嵌套列表
# li2 = copy.deepcopy(li)
# print('li:',li)
# print('li2:',li2)
# print(id(li),id(li2)) # 地址不同，深拷贝
# li.append(7)
# print('li:',li)
# print('li2:',li2)
# print(id(li[3]),id(li2[3])) # 外层地址不同，内层地址不同
```

浅拷贝优点：拷贝速度快，占用空间少，拷贝效率高

### （不）可变对象

~~~python
# 可变对象：变量对应的值可以修改，但是内存地址不可以修改
# 可变类型：列表，字典，集合
# 不可变对象：变量对应的值不能修改，如果修改就会生成一个新的数值从而分配新的内存空间
# 不可变类型：数值类型：int，bool，float，complex。字符串:str，元组：tuple
n = 10
print(id(n))
n = 15
print(id(n)) # 地址值发生改变
~~~

**注：深浅拷贝只针对可变对象，不可变对象没有拷贝的说法**

## 函数

```python
# 函数：
# 定义函数：
# def 函数名():
#     函数体
# 调用函数：函数名()
# 返回值：
# def func(a):
#     if a % 2 == 0:
#         return 1
#     else:
#         return 'abc'
# return 可以返回多个值，以元组的形式返回给调用者
# 如果一个函数没有返回值，返回结果是None

# 函数的参数
# 必备参数（位置参数）
# 传递和定义的参数循序，个数必须一致

# 默认参数：为参数提供默认值，调用函数时可以不传默认参数的值
# 注意：所有的位置参数必须在默认参数前，包含定义和调用
# def func(a = 12)

# 可变参数
# 传入的参数的数量可以改变，可以传入多个，也可以不传
# def func(*args) # 以元组的形式接收

# 关键字参数
# 属于可变参数
# def func(**kwargs): # 以字典形式接收
#     print(kwargs)
# func() # 传的是空字典，打印的是集合
# func(name = 'mpt', age = 18)
# 可以扩展函数的功能

# 函数嵌套
# 嵌套定义：在一个函数中定义另外一个函数
# def study():
#     print('晚上在学习')
#     def course(): # 内函数
#         print('Python')
#     course() # 定义完调用一下 ，注意层级
# study()
```

### 匿名函数

```python
# 匿名函数：lambda函数,lambda函数没有返回值，表达式本身就是返回值
# 函数名 = lambda 形参 : 返回值
# 函数名 = lambda: 返回值 # 对应无参情况
# 函数名 = lambda age = 18: 返回值 # 参数默认值
# 调用： 结果 = 函数名（实参）
# add = lambda x, y : x + y
# print(add(1,2))
# # 关键字参数
# fund = lambda **kwargs : kwargs
# print(fund(a=1,b=2))
# lambda结合if判断
# a = 1
# b = 2
# print('a > b') if a > b else print('a < b') # 三目运算
# comp = lambda a, b : 'a > b' if a > b else 'a < b'
# print(comp(1, 2))
```

### 内置函数

```python
# 内置函数
# 查看所有内置函数
# import builtins
# print(dir(builtins))
# 大写字母开头一般为内置常量名，小写字母开头一般为内置函数名
# set() list() tuple()

# abs() # 返回绝对值
# print(abs(-10))

# sum() # 求和,参数必须为可迭代对象,且只能求数字和
# print(sum([1,2,3]))
# print(sum((1,2,3)))
# print(sum({1,2,3}))
# print(sum(range(10)))

# min() max()
# print(min(-2,1,key=abs)) # 先求绝对值，在比大小

# zip() # 将可迭代对象作为参数，将对象中对应的元素打包成一个个元组
# li = [1, 2, 3]
# li2 = ['a', 'b', 'c']
# print(zip(li,li2))
# # 通过for打印
# for i in zip(li,li2): # i在这里为元组类型
#     print(i)
# # 注：如果li和li2的元素个数不同，就按照长度最短的返回
# # 转换成列表打印
# print(list(zip(li,li2)))

# map() # 可以对可迭代对象中的每一个元素进行映射，分别去执行
# map(func, iter1): func--自己定义的函数，iter--要放进去的可迭代对象
# 说人话：对象中的每一个元素都会去执行以下这个函数
# li = [1,2,3]
# def funa(x):
#     return x * 5
# mp = (map(funa, li))
# print(mp)
# # 第一种方法：通过for循环取出数据。注：执行完for循环mp会变为空
# # for i in mp:
# #     print(i)
# # 第二种方法：转换成列表打印
# print(list(mp))

# reduce() # 先把对象中的两个元素取出，计算出一个值然后保存着，接下来把这个计算值跟第三个元素进行计算
# from functools import reduce
# # reduce(functools, sequence) # function--函数：必须是有两个参数的函数，sequence--序列：可迭代对象
# li = [1, 2, 3, 4, 5]
# def add(x,y):
#     return x+y
# res = reduce(add, li) # 把函数的返回值作为函数的第一个参数
# print(res)
```

## 作用域

```python
# 作用域
# 声明全局变量 global 变量名
# global a # 此处不能赋值
# a = 120
# nonlocal # 将变量声明为外层变量（外层函数的局部变量，而且不能是全局变量）
```

## 拆包

~~~python
# 拆包：对于函数中的多个返回数据，去掉元组，列表或者字典，直接获取里面数据的过程
tua = (1,2,3,4)
# 方法1：
a,b,c,d = tua # 要求元组内的个数与接受的变量数量相同
print(a,b,c,d) # 一般在获取元组值的时候使用
# 方法2
a,*b = tua
print(a,b) # 一般在函数调用时使用
~~~













