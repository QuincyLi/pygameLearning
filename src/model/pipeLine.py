import pygame

from utils import utils


class Pipeline(object):
    """定义一个管道类"""

    def __init__(self):
        """定义初始化方法"""
        self.wallx = 400  # 管道所在X轴坐标
        self.pineUp = pygame.image.load(
            utils.resource_path("./assets/top.png"))
        self.pineDown = pygame.image.load(
            utils.resource_path("./assets/bottom.png"))

    def updatePipeline(self):
        """水平移动"""
        """"管道移动方法"""
        self.wallx -= 5  # 管道X轴坐标递减，即管道向左移动
        # 当管道运行到一定位置，即小鸟飞越管道，分数加1，并且重置管道
        if self.wallx < -80:
            self.wallx = 400

    def isCross(self):
        return self.wallx <= -80
