#基本框架
import pygame,sys,random               #sys是Python的内置函数，提供与python解释器及其环境相关的函数和变量。
from pygame.locals import *     #获取pygame所有方法
from block import *
import const 
from blockGroup import *
import game

#初始化Pygame库函数
pygame.init()

#显示游戏框界面大小
DISPLAYSURF = pygame.display.set_mode((const.GAME_WIDTH_SIZE,const.GAME_HEIGHT_SIZE))
game = Game(DISPLAYSURF)

while True:     #创建Pygame无限循环
    for event in pygame.event.get():    #获取当前发生的所有事件
        if event.type == QUIT:  #检测到quit事件
            pygame.quit()   #调用pygame.quit()退出程序执行
            sys.exit()      #用于退出当前程序的执行。sys.exit([arg])
    game.update()
    DISPLAYSURF.fill((0,0,0))   #原始代码(0,0,0)将代码颜色填充为黑色，二元组(0,0,0)是用RGB颜色值表示颜色，分别代表红绿蓝，范围0-255，渲染后会保留原来的渲染结果，所以每次渲染前要把图像涂黑
    game.draw()
    pygame.display.update()
