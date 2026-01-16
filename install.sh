#!/bin/bash

# 定义虚拟环境名称和需要检查的库名
VENV_NAME="my_venv"
REQUIRED_PACKAGE="decorator"

# 检查虚拟环境目录是否存在
if [ ! -d "$VENV_NAME" ]; then
    echo "虚拟环境 $VENV_NAME 不存在，正在创建..."
    # 创建虚拟环境（优先用python3，适配不同系统）
    if command -v python3 &> /dev/null; then
        python3 -m venv "$VENV_NAME"
    else
        echo "错误：未找到 Python 环境，无法创建虚拟环境！"
        exit 1
    fi
    echo "虚拟环境 $VENV_NAME 创建成功！"
else
    echo "虚拟环境 $VENV_NAME 已存在"
fi

# ========== 新增：检查并安装指定第三方库 ==========
echo "检查 $REQUIRED_PACKAGE 库是否已安装..."
# pip show 命令检查库是否存在，屏蔽输出仅保留状态码
if ! my_venv/bin/python -m pip show "$REQUIRED_PACKAGE" &> /dev/null; then
    echo "$REQUIRED_PACKAGE 未安装，正在通过 pip 安装..."
    my_venv/bin/python -m pip install "$REQUIRED_PACKAGE" --index-url https://pypi.org/simple
    # 检查安装是否成功
    if [ $? -eq 0 ]; then
        echo "$REQUIRED_PACKAGE 安装成功！"
    else
        echo "错误：$REQUIRED_PACKAGE 安装失败，请检查网络或 pip 源！"
        exit 1
    fi
fi

echo "脚本执行完成，当前虚拟环境已就绪！"