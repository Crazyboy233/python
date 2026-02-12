/*
给你一个整数 n ，请你找出并返回第 n 个 丑数 。

说明：丑数是只包含质因数 2、3 和/或 5 的正整数；1 是丑数。

示例 1：
输入: n = 10
输出: 12

解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。

提示： 
1 <= n <= 1690

url = https://leetcode.cn/problems/chou-shu-lcof/description/
*/

#include <iostream>
#include <vector>

class Solution {
public:
    int nthUglyNumber(int n) {
        std::vector<int> dp(n+1);
        dp[1] = 1;
        int p2 = 1;
        int p3 = 1;
        int p5 = 1;
        for (int i = 2; i <= n; ++i) {
            int num2 = p2 * 2;
            int num3 = p3 * 3;
            int num5 = p5 * 5;
            int min = std::min(std::min(num2, num3), num5);
            dp[i] = min;
            if (num2 == min) {
                p2++;
            }
            if (num3 == min) {
                p3++;
            }
            if (num5 == min) {
                p5++;
            }
        }
        return dp[n];
    }
};

int main() {
    Solution solution;
    int n = 10;
    int res = solution.nthUglyNumber(n);
    std::cout << res << std::endl;
    return 0;
}