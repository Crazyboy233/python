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

function add(...)
    local s = 0
    for i, v in ipairs{...} do
        s = s + v
    end
    return s
end

print(add(3, 4, 10, 25, 12))  -- 54