import pygame
import random
from .resource_manager import load_image


class Pipeline(object):
    """定义一个管道类"""

    def __init__(self, window_width, window_height):
        """定义初始化方法"""
        self.window_width = window_width
        self.window_height = window_height
        self.wallx = window_width  # 管道所在X轴坐标，从窗口右侧开始
        self.pineUp = load_image("src/assets/top.png")
        self.pineDown = load_image("src/assets/bottom.png")
        
        # 初始化管道间隙位置
        self.gap_height = 150  # 管道间隙高度
        self.min_gap_y = 100   # 管道间隙最小Y坐标
        self.max_gap_y = window_height - 100 - self.gap_height  # 管道间隙最大Y坐标
        self.gap_y = random.randint(self.min_gap_y, self.max_gap_y)  # 随机设置管道间隙Y坐标
        
        # 管道速度（基础速度）
        self.base_speed = 3
        self.current_speed = self.base_speed

    def updatePipeline(self, score):
        """水平移动"""
        # 根据分数调整速度，每5分增加0.5速度
        self.current_speed = self.base_speed + (score // 5) * 0.5
        # 确保速度不会过快
        self.current_speed = min(self.current_speed, 8.0)
        
        # 管道X轴坐标递减，即管道向左移动
        self.wallx -= self.current_speed
        
        # 当管道运行到一定位置，重置管道
        if self.wallx < -self.pineUp.get_width():
            self.reset()

    def reset(self):
        """重置管道位置和间隙"""
        self.wallx = self.window_width  # 重置到窗口右侧
        # 随机设置新的管道间隙位置
        self.gap_y = random.randint(self.min_gap_y, self.max_gap_y)
        # 清除passed标记
        if hasattr(self, 'passed'):
            delattr(self, 'passed')

    def isCross(self):
        """判断管道是否已经完全通过屏幕左侧"""
        return self.wallx <= -self.pineUp.get_width()
        
    def get_pipe_positions(self):
        """获取上下管道的绘制位置"""
        # 上管道的Y坐标（底部对齐到间隙顶部）
        up_y = self.gap_y - self.pineUp.get_height()
        # 下管道的Y坐标（顶部对齐到间隙底部）
        down_y = self.gap_y + self.gap_height
        return (self.wallx, up_y), (self.wallx, down_y)
        
    def get_collision_rects(self):
        """获取用于碰撞检测的矩形区域"""
        up_pos, down_pos = self.get_pipe_positions()
        up_x, up_y = up_pos
        down_x, down_y = down_pos
        
        # 上方管子的矩形位置（进一步减小宽度和高度以提高精度）
        upRect = pygame.Rect(up_x + 8, up_y + 5, self.pineUp.get_width() - 16, self.pineUp.get_height() - 10)
        # 下方管子的矩形位置（进一步减小宽度和高度以提高精度）
        downRect = pygame.Rect(down_x + 8, down_y, self.pineDown.get_width() - 16, self.pineDown.get_height() - 10)
        
        return upRect, downRect