/*
教练使用整数数组 actions 记录一系列核心肌群训练项目编号。
为增强训练趣味性，需要将所有奇数编号训练项目调整至偶数编号训练项目之前。
请将调整后的训练项目编号以 数组 形式返回。

示例 1：
输入：actions = [1,2,3,4,5]
输出：[1,3,5,2,4] 
解释：为正确答案之一

提示：
0 <= actions.length <= 50000
0 <= actions[i] <= 10000
*/
#include <vector>
#include <iostream>
class Solution {
public:
    std::vector<int> trainingPlan(std::vector<int>& actions) {
        int left = 0;
        int right = actions.size() - 1;
        while(left < right) {
            while(left < right) {
                if (actions[left] % 2 == 0) {
                    break;
                } else {
                    left++;
                }
            }
            while(left < right) {
                if (actions[right] % 2 == 1) {
                    break;
                } else {
                    right--;
                }
            }
            if (left < right) {
                int temp = actions[left];
                actions[left] = actions[right];
                actions[right] = temp;
                left++;
                right--;
            }
        }
        return actions;
    }
};

int main() {
    Solution solution;
    std::vector<int> vec = {1,2,3,4,5};
    solution.trainingPlan(vec);
    for(auto & num : vec) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    return 0;
}