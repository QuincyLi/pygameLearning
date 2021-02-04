import pygame
import sys

from model.pipeLine import Pipeline
from model.bird import Bird
from utils import utils


pygame.init()  # 初始化pygame
pygame.font.init()  # 初始化字体
size = width, height = 400, 650  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口
color = (255, 255, 255)

font = pygame.font.SysFont("Arial", 50)  # 设置字体和大小
background = pygame.image.load(
    utils.resource_path("./assets/background.png"))
clock = pygame.time.Clock()  # 设置时钟
FPS = 30

score = 0
Pipeline = Pipeline()                    # 实例化管道类
Bird = Bird()                            # 实例化鸟类


def createMap():
    global score
    screen.fill(color)
    screen.blit(background, (0, 0))  # 填入到背景

    # 显示管道
    screen.blit(Pipeline.pineUp, (Pipeline.wallx, -300))   # 上管道坐标位置
    screen.blit(Pipeline.pineDown, (Pipeline.wallx, 500))  # 下管道坐标位置
    Pipeline.updatePipeline()
    if Pipeline.isCross():
        score += 1

    if Bird.dead:
        Bird.status = 2
    else:
        Bird.status = 1

    screen.blit(Bird.birdStatus[Bird.status],
                (Bird.birdX, Bird.birdY))  # 设置小鸟的坐标
    Bird.birdUpdate()          # 鸟移动

    # 显示分数
    screen.blit(font.render('Score:' + str(score), -1,
                            (255, 255, 255)), (100, 50))  # 设置颜色及坐标位置

    pygame.display.update()  # 更新显示


def checkDead():
    # 上方管子的矩形位置
    upRect = pygame.Rect(Pipeline.wallx, -300,
                         Pipeline.pineUp.get_width() - 10,
                         Pipeline.pineUp.get_height())
    # 下方管子的矩形位置
    downRect = pygame.Rect(Pipeline.wallx, 500,
                           Pipeline.pineDown.get_width() - 10,
                           Pipeline.pineDown.get_height())

    # 检测小鸟与上下方管子是否碰撞
    if upRect.colliderect(Bird.birdRect) or downRect.colliderect(Bird.birdRect):
        Bird.dead = True

    # 检测小鸟是否飞出上下边界
    if not 0 < Bird.birdRect[1] < height:
        Bird.dead = True
        return True
    else:
        return False


def reset():
    global score
    score = 0
    Bird.dead = False
    Bird.status = 0
    Bird.birdX = 120
    Bird.birdY = 350
    Bird.birdRect = pygame.Rect(65, 50, 50, 50)


def getResutl():
    final_text1 = "Game Over"
    final_text2 = "Your final score is:  " + str(score)
    # 设置第一行文字字体
    ft1_font = pygame.font.SysFont("Arial", 70)
    ft1_surf = font.render(final_text1, 1, (242, 3, 36)
                           )                             # 设置第一行文字颜色
    # 设置第二行文字字体
    ft2_font = pygame.font.SysFont("Arial", 50)
    ft2_surf = font.render(final_text2, 1, (253, 177, 6)
                           )                            # 设置第二行文字颜色
    screen.blit(ft1_surf, [screen.get_width() / 2 -
                           ft1_surf.get_width() / 2, 100])  # 设置第一行文字显示位置
    screen.blit(ft2_surf, [screen.get_width() / 2 -
                           ft2_surf.get_width() / 2, 200])  # 设置第二行文字显示位置
    pygame.display.flip()


while True:  # 死循环确保窗口一直显示
    clock.tick(FPS)  # 每秒执行60次
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()
        if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN):
            if hasattr(event, "key") and event.key == pygame.K_RETURN and Bird.dead:
                reset()
            if not Bird.dead:
                Bird.jump = True  # 跳跃
                Bird.gravity = 5  # 重力
                Bird.jumpSpeed = 10  # 跳跃速度

    if checkDead():                      # 检测小鸟生命状态
        getResutl()                      # 如果小鸟死亡，显示游戏总分数
    else:
        createMap()                      # 创建地图

pygame.quit()  # 退出pygame
