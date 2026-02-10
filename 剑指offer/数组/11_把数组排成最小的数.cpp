/*
闯关游戏需要破解一组密码，闯关组给出的有关密码的线索是：

一个拥有密码所有元素的非负整数数组 password
密码是 password 中所有元素拼接后得到的最小的一个数
请编写一个程序返回这个密码。

示例 1：
输入：password = [15, 8, 7]
输出："1578"

示例 2：
输入：password = [0, 3, 30, 34, 5, 9]
输出："03033459"

提示：
0 < password.length <= 100

说明:
输出结果可能非常大，所以你需要返回一个字符串而不是整数
拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
*/

// 题解思路：
// 若 x + y > y + x 则 x > y。按照这个方式排序即可
#include <string>
#include <vector>
#include <iostream>
bool compare2(const int& a, const int& b) {
        std::string x = std::to_string(a) + std::to_string(b);
        std::string y = std::to_string(b) + std::to_string(a);
        if (std::stoi(x) > std::stoi(y)) {
            return false;
        }
        return true;
}

class Solution {
public:
    std::string crackPassword(std::vector<int>& password) {
        std::sort(password.begin(), password.end(), compare2);
        std::string res;
        for (int& num : password) {
            res += std::to_string(num);
        }
        return res;
    }
};

int main() {
    Solution solution;
    std::vector<int> password = {15, 8, 7};
    std::vector<int> password2 = {0, 3, 30, 34, 5, 9};
    std::cout << solution.crackPassword(password) << std::endl;
    std::cout << solution.crackPassword(password2) << std::endl;
    return 0;
}