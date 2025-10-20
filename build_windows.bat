@echo off
REM Flappy Bird游戏Windows打包脚本
REM 作者: Assistant
REM 日期: 2025-10-17

echo 开始打包Flappy Bird游戏Windows版本...

REM 检查是否存在虚拟环境，如果不存在则创建
if not exist "venv" (
    echo 创建虚拟环境...
    python -m venv venv
)

REM 激活虚拟环境
echo 激活虚拟环境...
call venv\Scripts\activate

REM 检查是否已安装pyinstaller
python -c "import PyInstaller" >nul 2>&1
if %errorlevel% neq 0 (
    echo 安装pyinstaller...
    pip install pyinstaller
)

REM 检查是否已安装pygame
python -c "import pygame" >nul 2>&1
if %errorlevel% neq 0 (
    echo 安装pygame...
    pip install pygame
)

REM 使用pyinstaller打包项目为Windows可执行文件
echo 正在打包项目为Windows可执行文件...
pyinstaller flappy_bird_windows.spec

echo 打包完成！Windows可执行文件位于 dist/flappy_bird.exe

REM 显示生成的文件信息
if exist "dist\flappy_bird.exe" (
    echo 生成的可执行文件信息：
    dir dist\flappy_bird.exe
) else (
    echo 错误：未找到生成的可执行文件
)

pause