# 类型转换
# int(x) # 将x转换为一个整数
# float(x) # 将x转换为一个浮点数
# str(x) # 将x转换为一个字符串

# # eval(str) # 用来计算在字符串中的有效python表达式，并返回一个对象
# print(eval('10+10')) # 输出20
# # eval()可以实现list，dict，tuple，str之间的转换
# # eval() 不安全，容易恶意修改数据
# # str -> list
# # st1 = "[[1,2],[3,4],[5,6]]"
# # li = eval(st1)
# # print(type(li))

# # tuple(s) # 将序列s转换为一个元组
# # list(s) # 将序列s转换为一个列表
# # str -> list
# print(list('abcdefg'))
# #tuple -> list
# print(list((1,2,3,4)))
# # dict -> list
# print(list({'name' : 'mpt', 'age' : 18})) # 字典转列表只取键名
# # set -> list
# print(list({'a','b','c'})) # 先去重，在转换
# # chr(x) # 将一个整数转换为一个字符

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

# 可变对象：变量对应的值可以修改，但是内存地址不可以修改
# 可变类型：列表，字典，集合
# 不可变对象：变量对应的值不能修改，如果修改就会生成一个新的数值从而分配新的内存空间
# 不可变类型：数值类型：int，bool，float，complex。字符串:str，元组：tuple
n = 10
print(id(n))
n = 15
print(id(n)) # 地址值发生改变
# 注：深浅拷贝只针对可变对象，不可变对象没有拷贝的说法