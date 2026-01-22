"""
现需要将一根长为正整数 bamboo_len 的竹子砍为若干段，每段长度均为正整数。请返回每段竹子长度的最大乘积是多少。

示例 1：
输入: bamboo_len = 12
输出: 81

提示：
2 <= bamboo_len <= 58
"""
class Solution:
    def cuttingBamboo(self, bamboo_len: int) -> int:
        if bamboo_len < 2:
            return 0
        if bamboo_len == 2:
            return 1
        if bamboo_len == 3:
            return 2
        x = bamboo_len // 3
        y = bamboo_len % 3
        if y == 0:
            return int(3 ** x)
        if y == 1:
            return 3 ** (x-1) * 4
        if y == 2:
            return int(3 ** x * 2)
        return -1

# 测试
solution = Solution()
bamboo_len = 10
print(solution.cuttingBamboo(bamboo_len=bamboo_len))