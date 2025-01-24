# 第11章 数据结构

Lua 中的 `table` 不是一种简单的数据结构，它可以作为其他数据结构的基础。其他语言提供的数据结构，如数组、记录、线性表、队列、集合等，在 Lua 中都可以通过 `table` 来表示。此外，用Lua 的 `table` 来实现这些结构的效率高。

## 数组

使用 `table` 实现数组就是用整数索引 `table` 。

## 矩阵与多维数组

在 Lua 中，有两种方式来表示矩阵。第一种是使用一个“数组的数组”，也就是一个 `table` 中的每个元素是另一个 `table` 。例如，使用以下代码来创建 N✖️M 的零矩阵：

```lua
mt = {}  -- 创建矩阵
for i = 1, N do
    mt[i] = {}
    for j = 1, M do
        mt[i][j] = 0
    end
end
```

由于在 Lua 中 `table` 是一种对象，因此在创建矩阵时，必须显示地创建每一行。

在 Lua 中表示矩阵的第二种方式是将两个索引合并为一个索引。如果两个索引是整数，可以将第一个索引乘以一个适当的常量，并加上第二个索引。以下代码就使用这种方法来创建 N✖️M 的零矩阵：

```lua
mt = {}  -- 创建矩阵
for i = 1, N do
    for j = 1, M do
        mt[(i-1)*M + j] = 0
    end
end
```

对于稀疏矩阵的遍历，一般使用 `pairs` 且只遍历那些非 `nil` 的元素。例如，要将一行与一个常量相乘，可以使用以下代码：

```lua
function mult(a, rowindex, k)
    local row = a[rowindex]
    for i, v in pairs(row) do
        row[i] = v * k
    end
end
```

**注意**：`table` 中的 `key` 是无序的，所以使用 `pairs` 的迭代并不保证会按递增次序来访问元素。对于一些特殊任务而言，可能要采用另外的方法，比如链表。

## 链表

由于 `table` 是动态的实体，所以在 Lua 中实现链表是很方便的。每个结点以一个 `table` 来表 示 ， 一个“链接”只 是结点 `table` 中的一个字段 ， 该字段包含了对其他 `table` 的引用。 例如，要实现一个基础的列表，其中每个结点具有两个字段：`next` 和 `value`，先创建一个用作列表头结点的变量：

```lua
list = nil
-- 在表头插入一个元素，元素值为v：
list = {next = list, value = v}
-- 遍历此列表：
local l = list
while l do 
    -- <访问 l.value>
    l = l.next
end
```



