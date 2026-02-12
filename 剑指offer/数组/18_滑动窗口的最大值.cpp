/*
科技馆内有一台虚拟观景望远镜，它可以用来观测特定纬度地区的地形情况。\
该纬度的海拔数据记于数组 heights ，其中 heights[i] 表示对应位置的海拔高度。请找出并返回望远镜视野范围 limit 内，可以观测到的最高海拔值。

示例 1：
输入：heights = [14,2,27,-5,28,13,39], limit = 3
输出：[27,27,28,28,39]
解释：
  滑动窗口的位置                最大值
---------------               -----
[14 2 27] -5 28 13 39          27
14 [2 27 -5] 28 13 39          27
14 2 [27 -5 28] 13 39          28
14 2 27 [-5 28 13] 39          28
14 2 27 -5 [28 13 39]          39

提示：
你可以假设输入总是有效的，在输入数组不为空的情况下：
1 <= limit <= heights.length
-10000 <= heights[i] <= 10000
*/

#include <vector>
#include <iostream>
#include <algorithm>

class Solution {
public:
    std::vector<int> maxAltitude(std::vector<int>& heights, int limit) {
        std::vector<int> temp;
        std::vector<int> res;
        int l = 0, r = limit;
        while(1) {
            for (int i = l;i < r; ++i) {
                temp.push_back(heights[i]);
            }
            res.push_back(*std::max_element(temp.begin(), temp.end()));
            
            temp.clear();
            l++;
            r++;
            if (r > heights.size()) {
                break;
            }
        }
        return res;
    }
};

int main() {
    Solution solution;
    std::vector<int> height = {14,2,27,-5,28,13,39};
    int limit = 3;
    std::vector<int> res = solution.maxAltitude(height, limit);
    for (int &num : res) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}