Morden CMake

### **Step 1：了解基础语法**
学习以下最基础的命令即可：
- `project()`：定义项目名和支持的语言。
- `add_executable()` 和 `add_library()`：定义目标。
- `target_include_directories()`：为目标添加头文件路径。
- `target_compile_features()` 和 `target_compile_options()`：设置目标编译选项。
- `target_link_libraries()`：链接目标依赖的库。

简单示例：
```cpp
// main.cpp
#include <iostream>
int main() {
    std::cout << "Hello, Modern CMake!" << std::endl;
    return 0;
}
```

```cmake
# CMakeLists.txt
cmake_minimum_required(VERSION 3.20)
project(ModernExample LANGUAGES CXX)

add_executable(my_app main.cpp)
target_compile_features(my_app PRIVATE cxx_std_17)
```

构建命令：
```bash
mkdir build && cd build
cmake ..
make
```

---

### **Step 2：学习模块化与子目录管理**
将项目分解成多个模块，利用 `add_subdirectory()` 管理独立模块，将功能与逻辑隔离。

---

### **Step 3：学习第三方库集成**
重点掌握以下两种形式：
1. 使用已安装的第三方库（`find_package()`）。
2. 使用 `FetchContent` 下载和配置第三方库。

---

### **Step 4：学习接口库、公共选项**
使用 **INTERFACE** 目标集中管理编译选项和公共配置：
```cmake
add_library(common_settings INTERFACE)
target_compile_features(common_settings INTERFACE cxx_std_20)
target_compile_options(common_settings INTERFACE -Wall -Wextra)

add_executable(my_app main.cpp)
target_link_libraries(my_app PRIVATE common_settings)
```

---