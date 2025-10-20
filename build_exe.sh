#!/bin/bash

# Flappy Bird游戏打包脚本
# 作者: Assistant
# 日期: 2025-10-17

echo "开始打包Flappy Bird游戏..."

# 检查是否存在虚拟环境，如果不存在则创建
if [ ! -d "venv" ]; then
    echo "创建虚拟环境..."
    python3 -m venv venv
fi

# 激活虚拟环境
echo "激活虚拟环境..."
source venv/bin/activate

# 检查是否已安装pyinstaller
if ! command -v pyinstaller &> /dev/null
then
    echo "安装pyinstaller..."
    pip install pyinstaller
fi

# 使用pyinstaller打包项目
echo "正在打包项目..."
pyinstaller flappy_bird.spec

echo "打包完成！可执行文件位于 dist/flappy_bird"

# 显示生成的文件信息
if [ -f "dist/flappy_bird" ]; then
    echo "生成的可执行文件信息："
    file dist/flappy_bird
    echo "文件大小："
    ls -lh dist/flappy_bird
else
    echo "错误：未找到生成的可执行文件"
fi