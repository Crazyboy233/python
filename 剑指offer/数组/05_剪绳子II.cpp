/*
现需要将一根长为正整数 bamboo_len 的竹子砍为若干段，每段长度均为 正整数。请返回每段竹子长度的 最大乘积 是多少。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
输入：bamboo_len = 12
输出：81

提示：
2 <= bamboo_len <= 1000
*/
#include <iostream>
class Solution {
public:
    int cuttingBamboo(int bamboo_len) {
        if (bamboo_len < 2) {
            return 0;
        }
        if (bamboo_len == 2) {
            return 1;
        }
        if (bamboo_len == 3) {
            return 2;
        }
        int x = bamboo_len / 3;
        int y = bamboo_len % 3;
        int sum = 1;
        for (int i = 0; i < x; ++i) {
            sum = sum % 1000000007 * 3;
        }
        if (y == 0) {
            return sum;
        }
        if (y == 1) {
            sum = sum / 3 % 1000000007 * 4 % 1000000007;
            return sum;
        }
        if (y == 2) {
            sum = sum % 1000000007 * 2 % 1000000007;
            return sum;
        }
        return -1;
    }
};

// 测试
int main() {
    Solution solution;
    int bamboo_len = 10;
    std::cout << solution.cuttingBamboo(bamboo_len) << std::endl;

    return 0;
}