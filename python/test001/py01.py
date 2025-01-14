# 列表名 = [元素1， 元素2， 元素3...]
# 元素与元素之间用逗号隔开，元素的类型可以不同
from os import remove

li = [1, 2, 3]
# 列表也可以切片
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