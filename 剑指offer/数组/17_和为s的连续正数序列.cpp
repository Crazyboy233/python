/*
待传输文件被切分成多个部分，按照原排列顺序，每部分文件编号均为一个 正整数（至少含有两个文件）。
传输要求为：连续文件编号总和为接收方指定数字 target 的所有文件。请返回所有符合该要求的文件传输组合列表。

注意，返回时需遵循以下规则：

每种组合按照文件编号 升序 排列；
不同组合按照第一个文件编号 升序 排列。
 

示例 1：
输入：target = 12
输出：[[3, 4, 5]]
解释：在上述示例中，存在一个连续正整数序列的和为 12，为 [3, 4, 5]。

示例 2：
输入：target = 18
输出：[[3,4,5,6],[5,6,7]]
解释：在上述示例中，存在两个连续正整数序列的和分别为 18，分别为 [3, 4, 5, 6] 和 [5, 6, 7]。

提示：
1 <= target <= 10^5

url = https://leetcode.cn/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/description/
*/

#include <iostream>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> fileCombination(int target) {
        std::vector<std::vector<int>> vec;
        std::vector<int> res;
        for (int l = 1, r = 2; l < r;) {
            int sum = (l + r) * (r - l + 1) / 2;
            if (sum == target) {
                res.clear();
                for (int i = l; i <= r; ++i) {
                    res.push_back(i);
                }
                vec.push_back(res);
                l++;
            } else if (sum < target) {
                r++;
            } else {
                l++;
            }
        }
        return vec;
    }
};

int main() {
    Solution solution;
    int target = 18;
    std::vector<std::vector<int>> res = solution.fileCombination(target);
    for (auto & arr : res) {
        for (auto &num : arr) {
            std::cout << num << " ";
        }
        std::cout << std::endl;
    }
    return 0;
}