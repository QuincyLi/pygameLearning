import pygame


class Bird(object):
    def __init__(self):
        self.birdRect = pygame.Rect(65, 50, 50, 50)
        self.birdStatus = [
            pygame.image.load("./src/assets/1.png"),
            pygame.image.load("./src/assets/2.png"),
            pygame.image.load("./src/assets/dead.png"),
        ]
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
