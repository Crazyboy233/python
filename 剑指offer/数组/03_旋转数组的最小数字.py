"""
仓库管理员以数组 stock 形式记录商品库存表。stock[i] 表示商品 id，可能存在重复。原库存表按商品 id 升序排列。
现因突发情况需要进行商品紧急调拨，管理员将这批商品 id 提前依次整理至库存表最后。
请你找到并返回库存表中编号的 最小的元素 以便及时记录本次调拨。

示例 1：
输入：stock = [4,5,8,3,4]
输出：3

示例 2：
输入：stock = [5,7,9,1,2]
输出：1

提示：
1 <= stock.length <= 5000
-5000 <= stock[i] <= 5000
"""
class Solution:
    def inventoryManagement(self, stock: list[int]) -> int:
        for i in range(len(stock)):
            if stock[i] > stock[i+1]:
                return stock[i+1]
        return -1

# 测试
solution = Solution()
stock = [4,5,8,3,4]
stock2 = [5,7,9,1,2]
print(solution.inventoryManagement(stock=stock))
print(solution.inventoryManagement(stock=stock2))