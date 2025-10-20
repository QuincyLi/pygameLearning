@echo off
REM Flappy Bird游戏重新打包脚本

echo 开始重新打包Flappy Bird游戏...

REM 使用最新的spec文件打包
echo 正在使用flappy_bird_final_fixed.spec打包项目...
python -m PyInstaller flappy_bird_final_fixed.spec

if %errorlevel% neq 0 (
    echo 打包过程中出现错误，请检查上面的错误信息
    pause
    exit /b 1
)

echo 打包完成！

REM 显示生成的文件信息
if exist "dist\flappy_bird_final_fixed.exe" (
    echo 生成的可执行文件信息：
    dir dist\flappy_bird_final_fixed.exe
    echo.
    echo 可执行文件已成功生成在 dist\flappy_bird_final_fixed.exe
    echo 您可以直接运行该文件来启动游戏
) else (
    echo 错误：未找到生成的可执行文件，请检查上面的错误信息
)

pause