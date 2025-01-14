# # 元组
# # 元组名 = (元素1, 元素2...)
# tua = (1, 2, 3, 'b', 'a')
# tua1 = (1,) # 只有一个元素要加逗号
# tua2 = () # 空元组
# print(type(tua))
#
# # count(元素)该元素出现的次数 index(元素)该值的下标 len(元组名)元组的长度 和列表的用法相同
# # 元组同样支持切片操作
# print(tua[2:])
# # 应用场景：函数的参数和返回值，
# # 格式化输出后面的()本质上就是一个元组
#
# # 字典 存放键值对，键具有唯一性，值可以重复
# # 字典名 = [键1:值1, 键2:值2]
# dict = {'hello': '1', 'world' : 2} # 类型为dict
# print(dict['hello'])
#
# # 查看元素 变量名[键名]
# # 不可以根据下标
# print(dict['world']) #键名不存在时报错
# # 变量名.get()
# print(dict.get('nihao', '不存在'))
#
# # 修改元素
# dict['hello'] = 20
# print(dict['hello'])
#
# # 新增元素
# # 有键名就修改，不存在就新增
# dict['你好'] = 22
# print(dict['你好'])
#
# # 删除元素
# # del
# # del dict # 删除整个字典
# del dict['hello'] # 删除时没有指定的键就报错
# print(dict)
#
# # clear 清空字典内容，但是保留字典
# # dict.clear()
# # print(dict)
#
# # pop() 删除指定键值对
# dict.pop('你好')
# print(dict)
# # dict.pop() # 没有指定键名报错
# dict.popitem() # 默认删除最后一个键值对 3.7之前的版本是随机删除一个键值对

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
