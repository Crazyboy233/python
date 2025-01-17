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

`table` 永远是“匿名的(anonymous)”，一个持有 table 的变量与 table 自身之间没有固定的关联性。

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

当一个程序再也没有对一个 `table` 引用时，lua的垃圾收集器（garbage collector）最终会删除该 `table`。



`table` 库提供了一个函数 `table.sort()`，它接受一个`table`并对其中的元素排序。下面是一个示例：

```lua
network = {
    {name = "grauna", IP = "210.26.30.34"},
    {name = "aeeaial", IP = "210.26.30.23"},
    {name = "lua", IP = "210.26.23.12"},
    {name = "derain", IP = "210.26.23.20"},
}
-- 如果想以 name 字段、按反向的字符顺序来对这个 table 排序的话，只需这么写：
table.sort(network, function (a, b) return (a.name > b.name) end)  -- 匿名函数
```



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

## 具名实参

当一个函数拥有大量的参数，而其中大部分参数是可选的，最好使用具名实参。下面是一个简单示例：

```lua
w = Window { x = 0, y = 0, width = 300, height = 200, title = "Lua", background = "blue", border = true }
```

注意：函数传递参数时接的是一个 `table`，所以使用花括号。在参数只有一个 `table` 时，可以省略圆括号不写，上述代码就采用了这种写法。

# 六、深入函数

在 Lua 中，函数是一种“第一类值”，它们具有特定的词法域。

-   **第一类值**：在 Lua 中，函数与其他传统类型的值（例如：数字和字符串）具有相同的权利。函数可以存储到变量中（无论全局变量还是局部变量）或 `table` 中，可以作为实参传递给其他函数，还可以作为其他函数的返回值。
-   **词法域**：在 Lua 中，一个函数可以嵌套在另一个函数中，内部的函数可以访问外部函数中的变量。

总结：函数是值。

```lua
-- 函数为值的示例
function foo(x) return 2 * x end
foo = function(x) return 2 * x end
```

**匿名函数**：

```lua
-- 假如有一个table，按照姓名对table进行排序，可以这么写：
table.sort(network, function (a, b) return (a.name > b.name) end)  -- 匿名函数
```

像 `sort()` 这样的函数，接受另一个函数作为实参的，称其是一个“高阶函数”。应用匿名函数来创建高阶函数所需的实参则可以带来更大的灵活性。注意：高阶函数并没有什么特权，Lua 强调将函数视为“第一类值”，所以高阶函数只是一种基于该观点的应用体现而已。

下面是一个高阶函数的示例：

```lua
function derivative(f, delta)
    delta = delta or 1e-3  -- 科学技术法，等同于0.001
    return function(x) 
        return (f(x + delta) - f(x)) / delta
    end
end
-- 对于特定的函数 f 调用 derivative(f) 将（近似的）返回其导数，例如：
c = derivative(math.sin)
print(math.cos(10), c(10))  -- -0.83907152907645	-0.83879937869802
```

由于函数在 Lua 中是一种“第一类值”，所以不仅可以将其存储在全局变量中，还可以存储在局部变量甚至 `table` 的字段中。将函数存储在 `table` 字段中可以支持许多 Lua 的高级应用，例如模块（module）和面向对象编程。

## 非全局函数

在定义递归的局部函数时，要注意下面这种情况：

```lua
local fact = function(n)
    if n == 0 then 
        return 1
    else 
        return n * fact(n-1)  -- 错误
    end
end
```

当 Lua 编译到函数体中调用 `fact(n-1)` 的地方时，由于 `fact` 尚未定义完毕，因此这句表达式其实是调用了一个全局的 `fact`，而非此函数自身。为了解决这个问题，可以先定义一个局部变量，然后再定义函数本身：

```Lua
local fact
fact = function(n)
    if n == 0 then
        return 1
    else 
        return n * fact(n-1)
    end
end
```

同样也可以使用 Lua 的语法糖来定义递归函数：

```lua
local function fact(n)
    if n == 0 then
        return 1
    else 
        return n * fact(n-1)
    end
end 
```

## 正确的尾调用

在 Lua 中支持“尾调用消除”。所谓的“尾调用”就是一种类似于 `goto` 的函数调用。当一个函数调用是另一个函数的最后一个动作时，该调用才算是一条“尾调用”。举个例子：以下代码中对 g 的调用就是一条“尾调用”：

```lua
function f(x) 
    return g(x) 
end
```

”尾调用“不会耗费栈空间，所以一个程序可以拥有无数嵌套的“尾调用”。举例来说，在调用以下函数时，传入任何数字作为参数都不会造成栈溢出：

```lua
function foo(n)
    if n > 0 then
        return foo(n-1)
    end
end
```

**易错**：下面的代码不是尾调用

```lua
function f(x)
    g(x)  -- 当g调用完后，f不能立即返回，它还需丢弃g返回的临时结果
end
-- 类似的，以下也不是尾调用
return g(x) + 1  -- 必须做一次加法
return x or g(x)  -- 必须调整为一个返回值
return (g(x))  -- 必须调整为一个返回值
```

### 尾调用和状态机

在 Lua 中，“尾调用”的一大应用就是编写“状态机”。这种程序通常以一个函数来表示一个的状态，改变状态就是 goto 到另一个特定的函数。举一个简单的例子来说明这个问题。

例如：一个迷宫中有几间房间，每间房间中最多有东南西北4扇门。用户在每一步移动中都需要输入一个移动的方向。如果在某个方向上有门，那么用户可以进入相应的房间；不然，程序就打印一条警告。游戏目标就是让用户从最初的房间走到最终的房间。

这个游戏就是一种典型的状态机，其中当前房间就是一个状态。可以将迷宫中的每间房间实现为一个函数，并使用“尾调用”来实现从一间房间移动到另一间房间。在以下代码中，实现一个具有4间房间的迷宫。

```lua
function room1()
    local move = io.read()
    if move == "south" then 
        return room3()
    elseif move == "east" then 
        return room2()
    else 
        print("invalid move") 
        return room1()  -- stay in the same room
    end
end

function room2()
    local move = io.read()
    if move == "south" then
        return room4()
    elseif move == "west" then
        return room1()
    else
        print("invalid move")
        return room2()
    end
end

function room3()
    local move = io.read()
    if move == "north" then
        return room1()
    elseif move == "east" then
        return room4()
    else
        print("invalid move")
        return room3()
    end
end

function room4()
    print("You win!")
end

room1()  -- 启动游戏
```

如果没有“尾调用消除”的话，每次用户的移动都会创建一个新的栈层，移动若干步之后就有可能会导致栈溢出。而“尾调用消除”则对用户移动的次数没有任何限制。这是因为每次移动实际上都只是完成一条 `goto` 语句到另一个函数，而非传统的函数调用。

# 七、迭代器与泛型for

## 迭代器与closure

在 Lua 中，通常将**迭代器**表示为**函数**。每调用一次函数，即返回集合中的“下一个元素”。

每个迭代器都需要在每次成功调用之间保持一些状态，这样才能知道它所在的位置及如何步进到下一个位置。closure 对于这类任务提供了极佳的支持，一个 closure 就是一种可以访问其外部嵌套环境中的局部变量的函数。对于 closure 而言，这些变量就可用于在成功调用之间保持状态值，从而使 closure 可以记住它在一次遍历中所在的位置。当然，为了创建一个新的 closure，还必须创建它的这些“非局部变量”。因此一个 closure 结构通常涉及到两个函数：closure 本身和一个用于创建该 closure 的工厂（factory）函数。

下面是一个迭代器的简单示例：

```lua
-- 与 ipairs 不同的是该迭代器并不是返回每个元素的索引，而是返回元素的值：
function values(t)
    local i = 0
    return function()
        i = i + 1
        return t[i]
        end
end
```

在本例中，values 就是一个工厂。每当调用这个工厂时，他就会创建一个一个新的 closure （即迭代器本身）。这个 closure 将它的状态保存在其外部变量 `t` 和 `i` 中。每当调用这个迭代器时它就从列表 `t` 中返回下一个值。知道最后一个元素返回后，迭代器就会返回 nil，以此表示迭代器的结束。

可以在一个 `while` 循环中使用这个迭代器：

```lua
t = {10, 20, 30}
iter = values(t)  -- 创建迭代器
while true do 
    local element = iter()  -- 调用迭代器
    if element == nil then 
        break
    end
	print(element)
end
```

然而使用泛型for则更简单。它正是为这种迭代而设计的：

```lua
t = {10, 20, 30}
for element in values(t) do
    print(element)
end
```

其他迭代器：

-   allwords	-- 可以遍历当前输入文件中所有单词

## 泛型for的语义

泛型 for 在循环过程中保存了迭代器函数。实际上它保存着3个值：一个迭代器函数、一个恒定状态和一个控制变量。

泛型 for 的语法如下：

```lua
for <var-list> in <exp-list> do
    <body>
end
```

其中，`<var-list>` 是一个或多个变量名的列表，以逗号分隔； `<exp-list>` 是一个或多个表达式的列表，同样以逗号分隔。通常表达式列表只有一个元素，即一句对迭代器工厂的调用。例如：

```lua
for k, v in pairs(t) do print(k, v) end  -- pairs用来遍历table
```

其中变量列表是 `k, v`，表达式列表只有一个元素 `pairs(t)`。一般来说变量列表中也只有一个变量，例如：

```lua
for line in io.lines() do
    io.write(line, "\n")
end
```

变量列表的第一元素称为“控制变量”。在循环过程中该值决不会为 nil，因为当它为 nil 时循环就结束了。

for 做的第一件事情是对 in 后面的表达式求值。这些表达式应该返回3个值供for 保存：迭代器函数、恒定状态和控制变量的初值。

## 迭代器

-   **无状态迭代器**，就是自身不保存任何状态的迭代器。

​	典型例子 `ipairs`（工厂），它可以用来迭代一个数组的所有元素：		

```lua
a = {"one", "two", "three"}
for i, v in ipairs(a) do  -- 要遍历的 table 是一个恒定状态，它不会在循环中改变
    print(i, v)
end
```

-   **具有复杂状态的迭代器**示例：将重写 `allwords` 迭代器，这个迭代器可以遍历当前输入文件中的所有单词。这次将它的状态保存到一个 `table` 中，这个 `table` 具有两个字段：`line` 和 `pos`。

```lua
-- 迭代器的起始函数只需返回迭代器函数和初始状态
local iterator  -- 在后面定义
function allwords()
    local state = {line = io.read(), pos = 1}
    return iterator, state
end
-- iterator 函数才开始真正的工作：
function iterator(state)
    while state.line do  -- 若为有效的行内容就进入循环
        local s, e = string.find(state.line, "%w+", state.pos)
        if s then  -- 知道了一个单词？
            state.pos = e + 1  -- 更新下一个位置（找到这个单词后）
            return string.sub(state.line, s, e)
        else  -- 没找到单词
            state.line = io.read()  -- 读取下一行
            state.pos = 1  -- 从第一个位置开始
        end
	end
    return nil
end
```

后面会看到使用协同程序编写迭代器的方式，这种方式是功能最强的，但稍微有一点开销。

# 九、协同程序

**概念**：协同程序与线程差不多，就是一条执行序列，拥有自己独立的栈、局部变量和指令指针，同时又与其他协同程序共享全局变量和其他大部分东西。

**协同程序与线程的区别**：

-   一个具有多个线程的程序可以同时运行几个线程，而协同程序却需要彼此协作的运行。（也就是说，一个具有多个协同程序的程序在任意时刻只能运行一个协同程序，并且正在运行的协同程序只会在其显示地要求挂起时，它的执行才会暂停。）

## 协同程序基础

Lua 将所有关于协同程序的函数放置在一个名为 `coroutine` 的 `table` 中。函数 `create` 用于创建新的协同程序，它只有一个函数作为参数。该函数的代码就是协同程序所需执行的内容。`create` 会返回一个 thread 类型的值，用以表示新的协同程序。通常 `create` 的参数是一个匿名函数，例如：

```lua
co = coroutine.create(function () print("hello") end)
print(co)  -- 打印thread: 0x600003f44008
```

**协同程序状态**：一个协同程序可以处于4种不同的状态：挂起（suspended）、运行（running）、死亡（dead）和正常（normal）。

当创建一个协同程序时，它处于挂起状态。也就是说，协同程序不会在创建它时自动执行其内容。可以通过函数 `status` 来检查协同程序的状态：

```lua
 print(coroutine.status(co))  -- 打印suspended
```

函数 `coroutine.resume()` 用于启动或再次启动一个协同程序的执行，并将其状态由挂起改为运行：

```lua
coroutine.resume(co) -- 打印hello
```

在本例中，协同程序的内容只是简单地打印了 “hello” 后便终止了，然后它就处于死亡状态，也就再也无法返回了：

```lua
 print(coroutine.status(co))  -- 打印dead
```

### `yield` 函数

`yield` 函数可以让一个运行中的协同程序挂起，而之后可以在恢复它的运行。示例：

```lua
co = coroutine.create(function ()
    for i = 1, 10 do
        print("co", i)
        coroutine.yield()
    end
end)
```

现在当唤醒这个协同程序时，它就会开始执行，直到第一个 `yield`：

```lua
coroutine.resume(co) -- 打印co 1
```

如果此时检查其状态，会发现协同程序处于挂起状态，因此可以再次恢复其运行：

```lua
print(coroutine.status(co))  -- 打印suspended
```

从协同程序的角度看，所有在它挂起时发生的活动都发生在 `yield` 调用中。当恢复协同程序时，对于 `yield` 的调用才最终返回。然后协同程序继续它的执行，直到下一个 `yield` 调用或执行结束：

```lua
coroutine.resume(co)  -- co 2
coroutine.resume(co)  -- co 3
...
coroutine.resume(co)  -- co 10
coroutine.resume(co)  -- 什么都不打印
```

在最后一次调用 `resume` 时，协同程序的内容已经执行完毕并已经返回。因此，这时协同程序处于死亡状态。如果试图再次恢复它的执行，`resume` 将返回 false 及一条错误消息：“false cannot resume dead coroutine”

**注意**：`resume` 是在保护模式中运行的。因此，如果在一个协同程序的执行中发生任何错误，Lua 是不会显示错误消息的，而是将执行权返回给 `resume` 调用。

放一个协同程序 A 唤醒另一个协同程序 B 时，协同程序 A 就处于一个特殊状态，既不是挂起状态（无法继续 A 的执行），也不是运行状态（是 B 在运行）。所以将这时的状态称为“正常”状态。

 

------

Lua 的协同程序可以通过一对 `resume-yield` 来交换数据。在第一次调用 `resume` 时，并没有对应的 `yield` 在等待它，因此所有传递给 `resume` 的额外参数都将视为协同程序主函数的参数：

```lua
co = coroutine.create(function (a, b, c)
    print("co", a, b, c)
	end)
coroutine.resume(co, 1, 2, 3)  -- 打印co 1 2 3
```

## 管道与过滤器

在 Lua 中，协同程序的经典示例是“生产者——消费者”的问题。示例：

```lua
-- 生产者
function producer ()
    while true do
        local x = io.read()  -- 产生新的值
        send(x)              -- 发送给消费者
    end
end

-- 消费者
function consumer()
    while true do
        local x = recive()  -- 从生产者接受值
        io.write(x, "\n")  -- 消费新的值
    end
end
```

这里有一个问题是如何将 `send` 与 `receive` 匹配起来。这是一个典型的 “谁具有主循环”的问题。由于生产者和消费者都处于活动状态，它们各自具有一个主循环，并且都将对方视为一个可调用的服务。对于这个特定的示例，可以很容易地修改其中一个函数的结构，展开它的循环，使其成为一个被动调用的函数，不过这样的结构改动可能会使某些真实的应用情况变得复杂。

**协同程序**被称为是一种匹配生产者和消费者的理想工具，一对 `resume-yield` 完全一改典型的调用者与被调用者之间的关系。当一个协同程序调用 `yield` 时，它不是进入了一个新的函数，而是从一个悬而未决的 `resmue` 调用中返回。同样地，对于 `resume` 的调用也不会启动一个新函数，而是从一次 `yield` 调用中返回。这项特性正可以用于匹配 `send` 和 `receive`，这两者都认为自己是主动方，对方式被动方。`receive` 唤醒生产者的执行，`send` 产出一个新值返还给消费者：

```lua
-- 消费者
function receive()
    local status, value = coroutine.resume(producer)
    return value
end

function send(x)
    coroutine.yield(x)
end

-- 生产者现在一定是一个协同程序：
producer = coroutine.creat(
	function ()
    	while true do
        	local x = io.read()  -- 产生新值
        	send(x)
        end
    end)
```

**执行顺序**：

-   调用 `receive` 函数时，它会调用 `coroutine.resume(producer)`，这会开始或继续执行 `producer` 协程。
-   `producer` 协程中的 `io.read()` 会等待用户输入，一旦用户输入了一行文本，它会调用 `send(x)` 函数。
-   `send(x)` 函数会调用 `coroutine.yield(x)`，这会暂停 `producer` 协程，并将 `x` 作为结果返回给 `receive` 函数，`receive` 函数会得到 `x` 并返回。
-   每次调用 `receive` 函数，都会继续 `producer` 协程的执行，使其继续等待下一个输入并暂停，如此循环。

程序通过调用消费者来启动。这种设计称为“消费者驱动”。

还可以扩展上述设计，实现“**过滤器**”。过滤器是一种位于生产者和消费者之间的处理功能，可用于对数据的一些变换。过滤器既是一个消费者又是一个生产者，它唤醒一个生产者促使其产生新值，然后又将变换后的值传递给消费者。例如可以在前面代码中添加一个过滤器，在每行起始处插入一个行号。代码如下：

```lua
function receive(prod)
    local status, value = coroutine.resume(prod)
    return value
end

function send(x)
    coroutine.yield(x)
end

function producer ()
    return coroutine.creat(function()
        while true do
            local x = io.read()  -- 产生新值
            send(x)
        end
    end)
end

function filter(prod)
    return coroutine.creat(function ()
        for line = 1, math.huge do
            local x = receive(prod)  -- 获取新值
            x = string.format("%5d %s", line, x)
            send(x)  -- 将新值发送给消费者
        end
    end)
end

function consumer(prod)
    while true do
        local x = receive(prod)  -- 获取新值
        io.write(x, "\n")  --消费新值
    end
end

-- 运行
p = producer
f = filter(p)
consumer(f)
-- 或者更简单地写为：
-- consumer(filter(producer()))
```

协同程序也是一种（非抢先的）多线程。在 `pipe` 中每项任务都在各自独立的进程中运行，而在协同程序中每项任务都在各自独立的协同程序中运行。`pipe` 在 `writer` (消费者)与 `reader` (生产者)之间提供一 个缓冲器，因此它们的运行速度允许存在一定差异。值得注意的是，在 `pipe` 中进程间的切换代价很高。而在协同程序中，切换代价则小得多，因此 `writer` 和 `reader` 可以彼此协作地运行。

## 以协同程序实现迭代器

## 非抢先式的多线程
