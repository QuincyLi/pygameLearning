import pygame
from .resource_manager import load_image


class Bird(object):
    def __init__(self):
        # 加载小鸟图片以获取实际尺寸
        self.bird_images = [
            load_image("src/assets/1.png"),
            load_image("src/assets/2.png"),
            load_image("src/assets/dead.png"),
        ]
        
        # 使用第一张图片的尺寸创建碰撞矩形
        bird_width = self.bird_images[0].get_width()
        bird_height = self.bird_images[0].get_height()
        
        # 创建更精确的碰撞矩形（显著小于图片尺寸以提高精度）
        self.birdRect = pygame.Rect(65, 50, bird_width - 20, bird_height - 20)
        self.birdStatus = self.bird_images
        self.status = 0  # 默认飞行状态
        self.birdX = 120  # 鸟所在X轴坐标,即是向右飞行的速度
        self.birdY = 350  # 鸟所在Y轴坐标,即上下飞行高度
        self.jump = False  # 默认情况小鸟自动降落
        self.jumpSpeed = 10  # 跳跃高度
        self.gravity = 5     # 重力
        self.dead = False  # 默认小鸟生命状态为活着

    def birdUpdate(self):
        if self.jump:
            # 小鸟跳跃
            self.jumpSpeed -= 1
            self.birdY -= self.jumpSpeed
        else:
            # 小鸟坠落
            self.gravity += 0.2
            self.birdY += self.gravity

        self.birdRect[1] = self.birdY
        # 同时更新X坐标以保持矩形与小鸟图像同步
        self.birdRect[0] = self.birdX + 10  # 进一步偏移以提高精度