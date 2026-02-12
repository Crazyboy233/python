/*
某班级 n 位同学的学号为 0 ~ n-1。点名结果记录于升序数组 records。假定仅有一位同学缺席，请返回他的学号。

示例 1：
输入：records = [0,1,2,3,5]
输出：4

示例 2：
输入：records = [0, 1, 2, 3, 4, 5, 6, 8]
输出：7

提示：
1 <= records.length <= 10000
*/

#include <vector>
#include <iostream>

class Solution {
public:
    int takeAttendance(std::vector<int>& records) {
        if (records.size() == 0) {
            return 0;
        }
        for (int i = 0; i < 10000; ++i) {
            if (records[i] != i) {
                return i;
            }
        }
        return -1;
    }
};

int main() {
    Solution solution;
    std::vector<int> records = {0, 1, 2, 3, 4, 5, 6, 8};
    int res = solution.takeAttendance(records);
    std::cout << res << std::endl;
    return 0;
}