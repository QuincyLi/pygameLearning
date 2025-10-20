# pygameLearning

这是一个使用Pygame开发的Flappy Bird游戏项目。

## 项目结构

- `src/` - 源代码目录
  - `model/` - 游戏模型类
    - `bird.py` - 鸟类实现
    - `pipeLine.py` - 管道类实现
  - `assets/` - 游戏资源文件（图片等）
  - `start.py` - 游戏主入口文件

## 如何运行

### 开发环境运行

1. 确保已安装Python 3和pygame库
2. 运行以下命令启动游戏：

```
python src/start.py
```

### 打包为可执行文件

项目已配置好打包脚本，可将游戏打包为独立的可执行文件。

#### macOS/Linux自动打包（推荐）

运行打包脚本：

```
./build_exe.sh
```

打包完成后，可执行文件将位于 `dist/flappy_bird`

#### Windows自动打包

在Windows系统上运行批处理脚本：

```
build_windows.bat
```

打包完成后，可执行文件将位于 `dist/flappy_bird.exe`

#### 手动打包

1. 创建并激活虚拟环境：
   ```bash
   # Linux/macOS
   python3 -m venv venv
   source venv/bin/activate
   
   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```
2. 安装依赖：
   ```bash
   pip install pyinstaller pygame
   ```
3. 执行打包命令：
   ```bash
   # Linux/macOS
   pyinstaller flappy_bird.spec
   
   # Windows
   pyinstaller flappy_bird_windows.spec
   ```

#### 运行打包后的程序

##### macOS/Linux
```
./dist/flappy_bird
```

##### Windows
```
dist\flappy_bird.exe
```

## 跨平台打包说明

由于PyInstaller不支持交叉编译，因此需要在目标平台上进行打包：

- macOS/Linux可执行文件只能在对应的系统上生成
- Windows可执行文件只能在Windows系统上生成

如需为不同平台打包，可以：
1. 在各目标平台分别执行打包操作
2. 使用虚拟机或容器技术
3. 使用CI/CD服务（如GitHub Actions）进行多平台构建

## 游戏操作说明

- 点击鼠标左键或按下任意键控制小鸟飞行
- 避开管道障碍物
- 每通过一个管道获得1分
- 碰撞或飞出边界游戏结束
- 游戏结束后按回车键重新开始