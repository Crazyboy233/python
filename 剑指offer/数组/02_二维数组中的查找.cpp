/*
m*n 的二维数组 plants 记录了园林景观的植物排布情况，具有以下特性：

每行中，每棵植物的右侧相邻植物不矮于该植物；
每列中，每棵植物的下侧相邻植物不矮于该植物。

请判断 plants 中是否存在目标高度值 target。

示例 1：
输入：plants = [[2,3,6,8],[4,5,8,9],[5,9,10,12]], target = 8
输出：true

示例 2：
输入：plants = [[1,3,5],[2,5,7]], target = 4
输出：false

提示：
0 <= n <= 1000
0 <= m <= 1000
*/
#include <vector>
#include <iostream>
class Solution {
public:
    bool findTargetIn2DPlants(std::vector<std::vector<int>>& plants, int target) {
        for (int i = 0; i < plants.size(); ++i) {
            for (int j = 0; j < plants[i].size(); ++j) {
                if (plants[i][j] == target) {
                    return true;
                }
            }
        }
        return false;
    }
};

// 测试
int main() {
    Solution solution;
    std::vector<std::vector<int>> plants = {{2,3,6,8},{4,5,8,9},{5,9,10,12}};
    int target = 8;
    // 启用boolalpha：显示true/false
    std::cout << std::boolalpha;  // 开启布尔值的文本输出模式
    std::cout << solution.findTargetIn2DPlants(plants, target) << std::endl;

    return 0;
}