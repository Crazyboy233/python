# 异常模块与包
# 抛出异常
# 创建一个Exception('xxx')对象，xxx--异常提示信息
# raise抛出这个对象(异常对象)
# raise Exception('抛出了一个异常')

# # 密码输入长度不对，就报异常
# def login():
#     pwd = input('请输入你的密码:')
#     if len(pwd) >= 6:
#         return '密码输入成功'
#     raise Exception('长度不足6位，密码输入失败')
# # print(login())
# try:
#     print(login())
# except Exception as e:
#     print(e)
# # 捕获异常是为了代码遇到异常时可以继续进行下去

# 模块
# 含义：在python中，一个py文件就是一个模块，里面定义了一些函数和变量，需要的时候可以导入并使用这些模块。
# 分类：
# 1、内置模块：random，time，os，logging，直接导入即可使用 # import time
# 2、第三方模块（第三方库）
# 下载：cmd窗口输入pip install 模块名 # 卸载为uninstall
# 3、自定义模块
# 即在自己的项目中定义模块
# 注意：命名要遵循标识符规定以及变量的命名规范，并且不要与内置模块冲突，否则将导致模块功能无法使用
# 执行步骤：
# 1、在Python模块加载路径中查找响应的模块文件
# 2、将模块文件编译成中间代码
# 3、执行模块文件中的代码

# 导入模块：import
# 1、import 模块名
# 模块名.功能名
# import test
# test.name
# test.func()
# 2、from 模块名 import 功能1 功能2。。。
# from test import func
# func() # 此时就不要写模块.
# print(name) # 此时没有导入name，使用name就会报错
# 3、form 模块名 import *
# from test import * # 把模块中所有的内容导入
# 不建议过多使用，可能会导致命名冲突

