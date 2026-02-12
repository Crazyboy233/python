/*
某班级考试成绩按非严格递增顺序记录于整数数组 scores，请返回目标成绩 target 的出现次数。

示例 1：
输入: scores = [2, 2, 3, 4, 4, 4, 5, 6, 6, 8], target = 4
输出: 3

示例 2：
输入: scores = [1, 2, 3, 5, 7, 9], target = 6
输出: 0

提示：
0 <= scores.length <= 105
-109 <= scores[i] <= 109
scores 是一个非递减数组
-109 <= target <= 109
*/

#include <vector>
#include <iostream>

class Solution {
public:
    int countTarget(std::vector<int>& scores, int target) {
        int count = 0;
        for(int i = 0; i < scores.size(); ++i) {
            if (scores[i] == target) {
                count++;
            }
        }
        return count;
    }
};

int main() {
    Solution solution;
    std::vector<int> scores = {2, 2, 3, 4, 4, 4, 5, 6, 6, 8};
    int target = 4;
    int res = solution.countTarget(scores, target);
    std::cout << res << std::endl;
    return 0;
}