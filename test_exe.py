import os
import subprocess
import time

def test_executable():
    """测试打包的可执行文件是否能正常运行"""
    exe_path = os.path.join("dist", "flappy_bird_final.exe")
    
    if not os.path.exists(exe_path):
        print(f"错误：找不到可执行文件 {exe_path}")
        return False
    
    print(f"找到可执行文件: {exe_path}")
    print(f"文件大小: {os.path.getsize(exe_path)} 字节")
    
    try:
        # 尝试运行可执行文件5秒钟然后终止
        print("正在启动可执行文件进行测试...")
        process = subprocess.Popen([exe_path])
        
        # 等待5秒
        time.sleep(5)
        
        # 检查进程是否仍在运行
        if process.poll() is None:
            print("可执行文件成功启动，正在运行中...")
            # 终止进程
            process.terminate()
            try:
                process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                process.kill()
            print("测试完成，可执行文件已终止。")
            return True
        else:
            print(f"可执行文件已退出，返回码: {process.returncode}")
            return process.returncode == 0
    except Exception as e:
        print(f"运行可执行文件时出错: {e}")
        return False

if __name__ == "__main__":
    success = test_executable()
    if success:
        print("\n测试成功！打包的可执行文件应该可以正常工作。")
    else:
        print("\n测试失败！可执行文件可能仍有问题。")