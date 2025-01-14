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
import functools
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


# 作用域
# 声明全局变量 global 变量名
# global a # 此处不能赋值
# a = 120
# nonlocal # 将变量声明为外层变量（外层函数的局部变量，而且不能是全局变量）

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

# # 拆包：对于函数中的多个返回数据，去掉元组，列表或者字典，直接获取里面数据的过程
# tua = (1,2,3,4)
# # 方法1：
# a,b,c,d = tua # 要求元组内的个数与接受的变量数量相同
# print(a,b,c,d) # 一般在获取元组值的时候使用
# # 方法2
# a,*b = tua
# print(a,b) # 一般在函数调用时使用