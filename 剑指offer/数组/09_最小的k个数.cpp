/*
仓库管理员以数组 stock 形式记录商品库存表，其中 stock[i] 表示对应商品库存余量。请返回库存余量最少的 cnt 个商品余量，返回 顺序不限。

示例 1：
输入：stock = [2,5,7,4], cnt = 1
输出：[2]

示例 2：
输入：stock = [0,2,3,6], cnt = 2
输出：[0,2] 或 [2,0]

提示：
0 <= cnt <= stock.length <= 10000
0 <= stock[i] <= 10000
*/

#include <vector>
#include <algorithm>
#include <iostream>
class Solution {
public:
    std::vector<int> inventoryManagement(std::vector<int>& stock, int cnt) {
        std::sort(stock.begin(), stock.end());
        std::vector<int> res(cnt);
        for (int i = 0; i < cnt; ++i) {
            res[i] = stock[i];
        }
        return res;
    }
};

int main() {
    Solution solution;
    std::vector<int> stock = {2,5,7,4};
    std::vector<int> stock2 = {0,2,3,6};
    std::vector<int> res = solution.inventoryManagement(stock, 1);
    std::vector<int> res2 = solution.inventoryManagement(stock2, 2);
    for (auto & num : res) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    for (auto & num : res2) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    return 0;
}