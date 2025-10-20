@echo off
REM 新的Flappy Bird游戏Windows打包脚本

echo 开始打包Flappy Bird游戏Windows版本...

REM 安装依赖
echo 安装依赖...
pip install pygame==2.5.2 pyinstaller==6.16.0

REM 使用pyinstaller打包项目为Windows可执行文件
echo 正在打包项目为Windows可执行文件...
python -m PyInstaller flappy_bird_windows.spec

echo 打包完成！

REM 显示生成的文件信息
if exist "dist\flappy_bird.exe" (
    echo 生成的可执行文件信息：
    dir dist\flappy_bird.exe
    echo.
    echo 可执行文件已成功生成在 dist\flappy_bird.exe
    echo 您可以直接运行该文件来启动游戏
) else (
    echo 错误：未找到生成的可执行文件，请检查上面的错误信息
)

pause