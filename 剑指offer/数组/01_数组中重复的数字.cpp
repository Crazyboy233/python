/*
设备中存有 n 个文件，文件 id 记于数组 documents。若文件 id 相同，则定义为该文件存在副本。请返回任一存在副本的文件 id。

示例 1：

输入：documents = [2, 5, 3, 0, 5, 0]
输出：0 或 5

提示：
0 ≤ documents[i] ≤ n-1
2 <= n <= 100000
*/

# include <iostream>
# include <vector>
class Solution {
public:
    int findRepeatDocument(std::vector<int> documents) {
        for (int i = 0; i < documents.size() - 1; ++i){
            for (int j = i + 1; j < documents.size(); ++j) {
                if (documents[i] == documents[j]) {
                    return documents[i];
                }
            }
        }
        return -1;
    }

};

// 测试
int main() {
    std::vector<int> documents = {2, 5, 3, 0, 5, 0};
    Solution solution = Solution();
    int result = solution.findRepeatDocument(documents);
    std::cout << "存在副本的 id 为：" << result << std::endl;

    return 0;
}