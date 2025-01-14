## **类型与值**

在lua中，有8种基础类型。

- nil(空)
- boolean(布尔)。false和nil是假，其他都是真。数字零和空字符串也是真。
- number(数字)。32位
- string(字符串)。
- userdata (自定义类型)
- function (函数)。是的，函数是一种类型。你可以把函数赋值给变量（a = print），也可以把函数作为参数传递给另一个函数。
- thread (线程)
- table (表)

在lua 5.1中，可以在字符串前加 # 来计算一个字符串的长度

一些函数：

- tonumber 显示的将一个字符串转为数字
- tostring 数字->字符串

## table（表）

在 Lua 中，`table` 是一个对象。`table` 中的元素可以是任意类型。

```Lua
a = {} -- 创建一个table，并将它的引用存储到a
k = "x"
a[k] = 10 -- 新条目，key="x"，value=10
a [20] = "great"  -- 新条目，key=20，value="great"
print(a["x"])  -- 10
k = 20
print(a[k])  -- "great"
```

table永远是“匿名的(anonymous)”，一个持有 table 的变量与 table 自身之间没有固定的关联性。

```Lua
a = {}
a["x"]= 10
b = a  -- b 与 a 引用同一个table
print (b["x"])  -->10
b["x"]= 20
print (a["x"] )  -->20
a = nil -- 现在只有b还在引用table
b = nil -- 再也没有对table的引用了
```

当一个程序再也没有对一个table引用时，lua的垃圾收集器（garbage collector）最终会删除该table。

# 表达式

## 逻辑操作符

所有逻辑操作符将 false 和 nil 视为假，将其他任何东西视为真。

-   `and`：对于操作符 and 来说，如果它的第一个操作数为假， 就返回第一个操作数 ，不然返回第 二个操作数。
-   `or`：对于操作符 or 来说，如果它的第一个操作数为真，就返回第一个操作数，不然返回第二个操作数。

## 字符串连接

在 Lua 中，“..”字符串连接操作符。当直接在一个数字后面输入它的时候，必须要用一个空格来分隔它们。

Lua 的字符串是不可修改的值，连接操作符只会创建一个新的字符串，不会对原来字符串进行修改。

## 优先级

在二元操作符中，除了指数操作符 “^” 和连接操作符 “..” 是右结合的，所有其他操作符都是左结合的。

## 控制语句

### repeat

repeat-until。相当于do-while

```lua
-- 打印输入的第一行不为空的内容
repeat
    line = io.read()
until line ~= ""
print(line)
```

注：一个声明在循环体中的局部变量的作用域包括了条件测试。

### 数字型for

```lua
-- 语法：
for var = exp1, exp2, exp3 do
    <执行体>
end
```

`var` 从 `exp1` 变化到 `exp2`，每次都以 `exp3` 作为步长（step）递增 `var`，并执行一次”执行体“。第三个表达式 `exp3` 是可选的，若不指定的话，Lua 会将步长默认为1.

如果不想给循环设置上限，可以使用常量 `math.huge`。在 Lua 中，`math.huge` 表示无穷大，它是一个特殊的常量值。

### 泛型for

泛型 for 循环通过一个迭代器（`itreator`）函数来遍历所有值。

```lua
-- 打印数组 a 的所有值
for i, v in ipairs(a) do print(v) end
```

解释：Lua 的基础库提供了 `ipairs`，这是一个用于遍历数组的迭代器函数。在每次循环中，`i` 会被赋予一个索引值，同时 `v` 被赋予一个对应于该索引的数组元素值。下面是另一个示例演示了如何遍历一个 `table` 中所有的 Key：

```lua
-- 打印 table t 中所有的key
for k in pairs(t) do print(k) end
```

标准库提供了几种迭代器：

-   迭代文件每行的（`io.lines`）
-   迭代 `table` 元素的（`pairs`）
-   迭代数组元素的（`ipairs`）
-   迭代字符串中单词的（`string.gmatch`）

# 五、函数

## 多重返回值

示例：

```lua
-- 在字符串中定位一个模式（pattern）的函数string。find。
-- 该函数若在字符串中找到了指定的模式，将返回匹配的起始字符和结尾字符的索引
s, e = string.find("hello Lua users", "Lua")
print(s, e)  -- 7 9
```

**特殊函数**：`unpack()`，它接受一个数组作为参数，并从下标1开始返回该数组的所有元素。下面是一个示例：

```lua
print(unpack{10, 20, 30})  -- 10 20 30
a, b = unpack{10, 20, 30}  -- a=10, b=20, 30被丢弃
```

## 变长参数

一个简单示例，这个函数返回了所有参数的总和：

```lua
function add(...)
    local s = 0
    for i, v in ipairs{...} do
        s = s + v
    end
    return s
end

print(add(3, 4, 10, 25, 12))  -- 54
```

解释：参数表中的3个点（...）表示该函数可接受不同数量的实参。一个函数要访问它的变长参数时，仍需用到三个点（...）。但不同的是，此时这3个点是作为一个表达式来使用的。

表达式“...”的行为类似于一个具有多重返回值的函数，它返回的是当前函数的所有变长参数。

