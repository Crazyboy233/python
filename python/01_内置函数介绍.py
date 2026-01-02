"""
python 中的关键字：
[
    del,
]

python 中的内置函数：
[
    iter(),
]

类的内置函数：
[
    __new__, __init__, __del__, 
    __call__, 
    __hash__, __eq__, 
    __lt__, __le__, __gt__, __ge__, __ne__,
    __getattr__, __getattribute__, __setattr__, __delattr__,
    __len__, __getitem__, __setitem__, __delitem__, __iter__, __next__,
    __add__, __sub__, __mul__, __truediv__, 
    __iadd__, __isub__,
    __str__, __repr__
]
高优函数：[__init__, __call__, __new__, __str__, __repr__]
"""

"""
笔记参考格式：
__str__(self)
- 作用：控制print(实例)的输出，面向用户
- return：返回值
- 示例：def __str__(self): return f"用户：{self.name}"
"""

# python 中的关键字：

# 1. del
# 作用：删除引用关系(并非直接删除内存中的对象)，触发垃圾回收机制(当对象无任何引用时，python 自动回收内存)
"""
核心场景：
1. 删除变量引用
2. 删除对象的属性（触发 __delattr__ 方法）
3. 删除列表 / 字典的元素（触发 __delitem__ 方法）。
"""
# 注意：del 不直接调用 __del__ 方法（ __del__ 是对象被垃圾回收时触发，而非 del 关键字触发）。
# 简单示例：
a = 10
print(a)  # 输出：10
del a
# print(a)  # 抛出 NameError: name 'a' is not defined



# python 中的内置函数：

# 1. iter()
# 作用：将一个 【可迭代对象】 转换为 【迭代器对象】 ，是实现 for 循环，列表推导式等迭代操作的底层基础。
# 语法： iter(iterable[, sentinel])
# iterable: 必须是可迭代对象（如列表、字符串、自定义实现 __iter__ 方法的类实例）
# sentinel（可选）：哨兵值，若传入， iterable 必须是可调用对象（如函数），迭代时每次调用该对象，返回值等于哨兵值则停止。
# 底层逻辑：调用 iter(obj) 本质是执行 obj.__iter__()，返回一个迭代器；迭代器必须实现 __next__() 方法。
# 示例如下：
lst = [1, 2, 3]
it = iter(lst)  # 等价于 lst.__iter__()
# 迭代器通过 next() 取值（每次取一个，直到耗尽）
print(next(it))  # 输出：1（等价于 it.__next__()）
print(next(it))  # 输出：2
print(next(it))  # 输出：3
# print(next(it))  # 抛出 StopIteration 异常（迭代器耗尽）



# 类的内置函数：

# 一、对象创建与初始化（生命周期）
# 注：这类方法控制对象从创建到销毁的全过程，是最基础的魔术方法。

# 1. __new__(cls, ...)
# 作用：静态方法(无需装饰器)，在创建实例(分配内存)之前被调用，核心职责就是“创建实例”(分配内存)。
# return：返回实例对象(决定 __init__ 是否执行)
# 示例，这里采用 【单例模式】 介绍：
class Singleton:
    _instance = None  # 类属性保存唯一实例

    def __new__(cls):   # cls 这里是指类本身
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# 2. __init__(self, ...)
# 作用：实例方法，初始化实例属性（接收 __new__ 创建的对象）。
# return：无
# 示例：
def __init__(self, name):
    self.name = name

# 3. __del__(self)
# 作用：实例方法，对象被销毁时触发(垃圾回收、程序结束)，用于释放资源。
# return：无
# 注： __del__ 的执行时机不太好预测，推荐使用 with 语句。
# 示例：
def __del__(self):
    print(f"{self.name} 被销毁")



# 二、对象可调用 / 可哈希 / 可比较
# 注：这类方法赋予对象特殊行为(如调用、比较、哈希)

# 1. __call__(self, ...)
# 作用：实例方法，让实例可像函数一样调用(实例())
# return：根据需求决定返回值
# 示例：
def __call__(self, x):
    return x*2

# 2. __hash__(self)
# 作用：返回对象的哈希值(用于字典键/集合元素)，需与 __eq__ 配套实现。
# return：对象的哈希值
# 示例：
def __hash__(self):
    return hash(self.name)

# 3. __eq__(self, other)
# 作用：定义 == 比较规则
# return：布尔值
# 示例：
def __eq__(self, other):
    return self.age == other.age

# 4. 比较运算符 
# __lt__(self, other) 作用：定义 < 比较规则
# __le__(self, other) 作用：定义 <= 比较规则
# __gt__(self, other) 作用：定义 > 比较规则
# __ge__(self, other) 作用：定义 >= 比较规则
# __ne__(self, other) 作用：定义 != 比较规则
# return：返回比较规则
# 示例，这里只对 __lt__ 函数举例说明，其他同理：
def __lt__(self, other):
    return self.age < other.age



# 三、属性访问控制
# 注：这类方法控制对象属性的 “读、写、删”，是封装的核心。

# 1. __getattr__(self, name)
# 作用：访问不存在的属性时触发(兜底)
# 示例：
def __getattr__(self, name):
    return f"属性{name}不存在"

# 2. __getattrbute__(self, name)
# 作用：访问任意属性时都触发(优先级高于 __getattr__)
# 示例：
def __getattrbute__(self, name):
    return super().__getattrbute__(name)

# 3. __setattr(self, name, value)
# 作用：给属性赋值时触发(如 self.name = "张三")
# 示例：
def __setattr__(self, name, value):
    super().__setattr__(name, value)

# 4. __delattr__(self, name)
# 作用：删除属性时触发(如 del self.name)
# 示例：
def __delattr__(self, name):
    super().__delattr__(name)



# 四、容器 / 序列行为（模拟列表 / 字典）
# 注：如果想让自定义类像列表、字典一样支持索引、切片、长度等操作，需实现这类方法。

# 1. __len__(self)
# 作用：定义 len(实例) 的返回值(容器长度)
# return：实例长度
# 示例：
def __len__(self):
    return len(self.data)   # self.data 是内部列表

# 2. __getitem__(self, key)
# 作用：定义 实例[key] (索引/切片访问)
# return： key 对应的 value, 或者是下标 idx 对应的 值 
# 示例：
def __getitem__(self, key):
    return self.data[key]

# 3. __setitem__(self, key, value)
# 作用：定义 实例[key] = value (赋值)
# 示例：
def __setitem__(self, key, value):
    self.data[key] = value

# 4. __delitem__(self, key)
# 作用：定义 del 实例[key] (删除元素)
# 示例：
def __delitem__(self, key): # key 同 idx
    del self.data[key]

# 5. __iter__(self)
# 作用：让对象可迭代(支持 for 循环)
# return：返回迭代器
# 示例：
def __iter__(self):
    return iter(self.data)

# 6. __next__(self)
# 作用：迭代器的核心方法
# return：返回下一个元素(配合 __iter__)
# 示例，通常在迭代器类中实现：
def __next__(self):
    ...



# 五、运算符重载（算术 / 赋值）
# 注：让自定义对象支持+、-、*等算术运算符，或+=、-=等赋值运算符。

# 1. 算术运算符
# __add__(self, other) 作用：定义 self + other
# __sub__(self, other) 作用：定义 self - other
# __mul__(self, other) 作用：定义 self * other
# __truediv__(self, other) 作用：定义 self / other
# 示例，这里只对 __add__ 函数举例说明，其他函数同理：
def __add__(self, other):
    return self.num + other.num

# 2. 赋值运算符
# __iadd__(self, other) 作用：定义 self += other
# __isub__(self, other) 作用：定义 self -= other
# 示例，这里只对 __iadd__ 函数举例说明，其他函数同理：
def __iadd__(self, other):
    self.num += other.num
    return self



# 六、字符串表示（打印 / 调试）
# 注：这类方法控制对象的 “字符串形态”，方便调试和展示。

# 1. __str__(self)
# 作用：定义 str(实例)/print(实例) 的输出(面向用户)
# 示例：
def __str__(self):
    return f"Person({self.name})"

# 2. __repr__(self)
# 作用：定义 repr(实例) 的输出(面向开发者，优于 __str__)
# 示例：
def __repr__(self):
    return f"Person(name='{self.name}',age='{self.age}')"