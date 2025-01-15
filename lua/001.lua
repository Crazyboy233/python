-- print("Hello, World!")

-- function fact(n)
--     if n == 0 then
--         return 1
--     else
--     return n * fact(n - 1)
--     end
-- end

-- print("输入一个数字：")
-- a = io.read("*number") -- 读取一个数字
-- print("阶乘为 ", fact(a))

-- a = {} -- 创建一个table，并将它的引用存储到a
-- k = "x"
-- a[k] = 10 -- 新条目，key="x"，value=10
-- a [20] = "great"  -- 新条目，key=20，value="great"
-- -- for k in pairs(a) do print(k) end
-- -- for i, v in pairs(a) do print(v) end

-- function add(...)
--     local s = 0
--     for i, v in ipairs{...} do
--         s = s + v
--     end
--     return s
-- end

-- print(add(3, 4, 10, 25, 12))  -- 54

-- function derivative(f, delta)
--     delta = delta or 1e-3  -- 科学技术法，等同于0.001
--     return function(x) 
--         return (f(x + delta) - f(x)) / delta
--     end
-- end
-- -- 对于特定的函数 f 调用 derivative(f) 将（近似的）返回其导数，例如：
-- c = derivative(math.sin)
-- print(math.cos(10), c(10))  -- -0.83907152907645	-0.83879937869802

--[[
    尾调用和状态机：
    例如：一个迷宫中有几间房间，每间房间中最多有东南西北4扇门。
    用户在每一步移动中都需要输入一个移动的方向。
    如果在某个方向上有门，那么用户可以进入相应的房间；不然，程序就打印一条警告。
    游戏目标就是让用户从最初的房间走到最终的房间。

    这个游戏就是一种典型的状态机，其中当前房间就是一个状态。
    可以将迷宫中的每间房间实现为一个函数，并使用“尾调用”来实现从一间房间移动到另一间房间。
    在以下代码中，实现一个具有4间房间的迷宫。
]]
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