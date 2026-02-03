/*
仓库管理员以数组 stock 形式记录商品库存表。stock[i] 表示商品 id，可能存在重复。请返回库存表中数量大于 stock.length / 2 的商品 id。

示例 1：
输入：stock = [6, 1, 3, 1, 1, 1]
输出：1

提示：
1 <= stock.length <= 50000
给定数组为非空数组，且存在结果数字
*/
#include <vector>
#include <iostream>
class Solution {
public:
    int inventoryManagement(std::vector<int>& stock) {
        std::sort(stock.begin(), stock.end());
        return stock[stock.size()/2];
    }
};

int main() {
    Solution solution;
    std::vector<int> stock = {6, 1, 3, 1, 1, 1};
    int res = solution.inventoryManagement(stock);
    std::cout << res << std::endl;
    return 0;
}