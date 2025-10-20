# 打包说明

本文档详细说明了如何将Flappy Bird游戏项目打包为可在不同平台上运行的可执行文件。

## 打包工具

本项目使用 [PyInstaller](https://www.pyinstaller.org/) 作为打包工具，它可以将Python应用程序及其所有依赖项打包为独立的可执行文件。

## 打包配置

项目根目录下有针对不同平台的spec文件：
- `flappy_bird.spec` - macOS/Linux打包配置
- `flappy_bird_windows.spec` - Windows打包配置

配置内容包括：
1. 入口文件：`src/start.py`
2. 资源文件：`src/assets/` 目录下的所有图片文件
3. 输出设置：
   - 无控制台窗口（GUI模式）
   - 可执行文件名为 `flappy_bird`

## 打包步骤

### 1. 准备环境

确保系统已安装Python 3和pip工具。

### 2. 创建虚拟环境（推荐）

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. 安装依赖

```bash
pip install pyinstaller
pip install pygame
```

注意：如果项目有requirements.txt文件，也可以使用：
```bash
pip install -r requirements.txt
```

### 4. 执行打包

#### macOS/Linux打包

```bash
pyinstaller flappy_bird.spec
```

或者使用项目提供的便捷脚本：
```bash
./build_exe.sh
```

#### Windows打包

在Windows系统上执行：
```cmd
pyinstaller flappy_bird_windows.spec
```

或者使用项目提供的批处理脚本：
```cmd
build_windows.bat
```

## 输出文件

打包完成后，将在项目根目录下生成以下目录：

- `build/` - 构建过程中产生的临时文件
- `dist/` - 最终生成的可执行文件
  - `flappy_bird` - 主可执行文件（Linux/macOS）
  - `flappy_bird.exe` - 主可执行文件（Windows）

## 注意事项

### 资源文件路径

由于打包后资源文件的路径会发生变化，代码中使用了相对路径来加载图片资源。请确保：
1. 所有资源文件都已正确添加到spec文件的datas列表中
2. 代码中的资源路径是相对于项目根目录的

### 平台兼容性

- 在哪个平台打包的可执行文件只能在该平台运行
- 如需在多个平台分发，需要在各目标平台分别打包
- Windows版本需要在Windows系统上打包生成

### 文件大小

打包后的可执行文件可能较大（通常几十MB），这是因为包含了Python解释器和所有依赖库。

### 权限问题（Linux/macOS）

在Linux和macOS系统上，可能需要为可执行文件添加执行权限：

```bash
chmod +x dist/flappy_bird
```

## 交叉编译说明

由于PyInstaller不支持交叉编译，因此无法在macOS上直接生成Windows可执行文件。要在macOS上为Windows平台打包，您需要使用以下方法之一：

### 方法1：使用虚拟机
1. 在macOS上安装Windows虚拟机（如Parallels Desktop、VMware Fusion或VirtualBox）
2. 在虚拟机中安装Python和所需依赖
3. 使用PyInstaller在Windows虚拟机中打包项目

### 方法2：使用Docker（Windows容器）
1. 在macOS上安装Docker Desktop
2. 启用Windows容器支持
3. 创建Windows容器并安装所需环境
4. 在容器中执行打包操作

### 方法3：使用GitHub Actions
1. 配置GitHub Actions工作流
2. 设置多平台构建任务
3. 利用GitHub的Windows运行器生成Windows可执行文件

## 故障排除

### 打包失败

1. 检查是否所有依赖库都已正确安装
2. 确认spec文件中的路径配置是否正确
3. 查看控制台输出的错误信息

### 运行时错误

1. 确认所有资源文件都已正确包含在打包文件中
2. 检查代码中加载图片的路径是否正确
3. 查看是否缺少某些隐藏的依赖库

### 图片无法加载

1. 确认图片文件已添加到spec文件的datas配置中
2. 检查代码中加载图片的路径是否正确

## 自定义配置

如需修改打包配置，可以直接编辑对应的spec文件：

- 修改可执行文件名：更改 `name` 参数
- 切换控制台模式：设置 `console=True` 或 `console=False`
- 添加额外资源：在 `datas` 列表中添加更多文件
- 排除不需要的模块：在 `excludes` 列表中添加模块名

更多信息请参考 [PyInstaller官方文档](https://pyinstaller.readthedocs.io/en/stable/)