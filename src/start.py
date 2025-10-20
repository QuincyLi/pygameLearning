import pygame
import random
import sys
import os

# 将当前目录添加到Python路径中
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from model.pipeLine import Pipeline
from model.bird import Bird
from model.resource_manager import load_image


pygame.init()  # 初始化pygame
pygame.font.init()  # 初始化字体
size = width, height = 800, 650  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口
color = (255, 255, 255)

# 使用支持中文的字体文件或系统字体
def get_chinese_font(size):
    """获取支持中文的字体"""
    # 字体文件路径
    font_paths = [
        "src/fonts/simsun.ttc",  # 宋体
        "src/fonts/msyh.ttc",    # 微软雅黑
        "src/fonts/simhei.ttf",  # 黑体
    ]
    
    # 检查字体文件是否存在
    for font_path in font_paths:
        if os.path.exists(font_path):
            try:
                return pygame.font.Font(font_path, size)
            except:
                continue
    
    # 如果没有字体文件，使用系统字体
    if os.name == 'nt':  # Windows
        # 尝试使用系统中文字体
        try:
            return pygame.font.SysFont("Microsoft Yahei", size)
        except:
            try:
                return pygame.font.SysFont("SimSun", size)
            except:
                return pygame.font.Font(None, size)
    else:
        return pygame.font.Font(None, size)

# 创建默认字体
font = get_chinese_font(50)

# 加载背景图片并调整大小以适应窗口
background = load_image("src/assets/background.png")
background = pygame.transform.scale(background, (width, height))  # 调整背景图片大小以适应窗口

clock = pygame.time.Clock()  # 设置时钟
FPS = 30

score = 0
# 创建多个管道实例
pipes = []
for i in range(3):  # 创建3个管道
    pipe = Pipeline(width, height)
    # 将管道错开分布
    pipe.wallx = width + i * 300
    pipes.append(pipe)

Bird = Bird()  # 实例化鸟类


def createMap():
    global score
    screen.fill(color)
    screen.blit(background, (0, 0))  # 填入到背景

    # 显示管道
    for pipe in pipes:
        # 获取管道位置
        up_pos, down_pos = pipe.get_pipe_positions()
        # 绘制上下管道
        screen.blit(pipe.pineUp, up_pos)
        screen.blit(pipe.pineDown, down_pos)
        # 更新管道位置
        pipe.updatePipeline(score)
        # 检查小鸟是否通过管道（得分）
        # 当管道的右侧边缘小于小鸟的x坐标时，表示小鸟已经通过了该管道
        if not hasattr(pipe, 'passed') and pipe.wallx + pipe.pineUp.get_width() < Bird.birdX:
            score += 1
            pipe.passed = True  # 标记该管道已被通过
            print(f'得分！当前分数: {score}')  # 调试信息
        # 当管道移出屏幕左侧时，重置管道
        if pipe.wallx < -pipe.pineUp.get_width():
            pipe.reset()
            # 确保清除passed标记
            if hasattr(pipe, 'passed'):
                delattr(pipe, 'passed')

    if Bird.dead:
        Bird.status = 2
    else:
        Bird.status = 1

    screen.blit(Bird.birdStatus[Bird.status],
                (Bird.birdX, Bird.birdY))  # 设置小鸟的坐标
    Bird.birdUpdate()          # 鸟移动

    # 显示分数
    screen.blit(font.render('菜鸡分:' + str(score), -1,
                            (255, 255, 255)), (100, 50))  # 设置颜色及坐标位置

    pygame.display.update()  # 更新显示


def checkDead():
    # 检测小鸟与所有管道是否碰撞
    for pipe in pipes:
        upRect, downRect = pipe.get_collision_rects()
        # 检测小鸟与上下方管子是否碰撞
        if upRect.colliderect(Bird.birdRect) or downRect.colliderect(Bird.birdRect):
            Bird.dead = True
            return True

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
    
    # 重置所有管道
    for i, pipe in enumerate(pipes):
        pipe.reset()
        pipe.wallx = width + i * 300


def getResutl():
    final_text1 = "Game Over(小芝芝真菜)"
    final_text2 = "Your final score is:  " + str(score)
    # 使用支持中文的字体
    ft1_font = get_chinese_font(70)
    ft1_surf = ft1_font.render(final_text1, 1, (242, 3, 36))  # 设置第一行文字颜色
    
    # 设置第二行文字字体
    ft2_font = get_chinese_font(50)
    ft2_surf = ft2_font.render(final_text2, 1, (253, 177, 6))  # 设置第二行文字颜色
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