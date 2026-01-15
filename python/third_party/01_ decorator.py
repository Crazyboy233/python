"""
该库的主要价值是简化装饰器的编写。
解决原生 Python 装饰器在保留函数元信息（如名称、文档字符串）、处理参数、嵌套装饰等场景下的痛点

安装： pip install decorator
"""

# 示例 1
# 原生写法 vs decorator 库写法对比：
import time
from functools import wraps

def time_raw(fun):
    @wraps(fun) # # 必须加，否则 func.__name__ 会变成 wrapper
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fun(*args, **kwargs)
        end = time.time()
        print(f"{fun.__name__} 执行耗时：{end - start::4f} 秒")
        return result
    return wrapper

# 使用 decorator 库的写法
import time 
from decorator import decorator

@decorator
def time_deco(fun, *args, **kwargs):
    start = time.time()
    result = fun(*args, **kwargs)
    end = time.time()
    print(f"{fun.__name__} 执行耗时：{end - start::4f} 秒")
    return result

# 测试装饰器
print("=======示例1:测试简单装饰器=======")
@time_deco
def test_fun(n):
    """测试函数：计算 1 到 n 的和"""
    return sum(range(n))

# 验证元信息是否保留
print(test_fun.__name__)
print(test_fun.__doc__)
test_fun(1000)
print("=======示例1:测试结束=======")


# 示例2：带参数的装饰器
def time_witf_args(enable=True):
    @decorator
    def wrapper(func, *args, **kwargs):
        if not enable:
            return func(*args, **kwargs)
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{fun.__name__} 执行耗时：{end - start::4f} 秒")
        return result
    return wrapper

print("=======示例2:测试带参数的装饰器=======")

@time_witf_args
def test_func2(n):
    return sum(range(n))

test_func2(1000)
print("=======示例2:测试结束=======")

# 示例3:decorator 库的 FunctionMaker TODO
# 示例4:异步装饰器 TODO