import os
import sys
import pygame


def resource_path(relative_path):
    """获取资源文件的绝对路径，兼容开发环境和打包环境"""
    try:
        # PyInstaller创建临时文件夹，并将路径存储在_MEIPASS中
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


def load_image(relative_path):
    """加载图片资源"""
    return pygame.image.load(resource_path(relative_path))


def load_font(relative_path, size):
    """加载字体资源"""
    try:
        return pygame.font.Font(resource_path(relative_path), size)
    except:
        # 如果无法加载指定字体，使用系统默认字体
        return pygame.font.Font(None, size)