import sys
import os

# 添加src目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    print("正在测试模块导入...")
    
    # 测试pygame导入
    import pygame
    print("✓ pygame导入成功")
    
    # 测试model模块导入
    from model.bird import Bird
    print("✓ Bird类导入成功")
    
    from model.pipeLine import Pipeline
    print("✓ Pipeline类导入成功")
    
    from model.resource_manager import load_image
    print("✓ resource_manager导入成功")
    
    # 测试start.py中的导入
    from model.pipeLine import Pipeline
    from model.bird import Bird
    from model.resource_manager import load_image
    print("✓ start.py中的导入测试成功")
    
    print("\n所有模块导入测试通过！")
    
except Exception as e:
    print(f"导入测试失败: {e}")
    import traceback
    traceback.print_exc()