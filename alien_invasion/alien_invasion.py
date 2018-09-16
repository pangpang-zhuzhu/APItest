import sys
import pygame
from setting import Setting
from ship import Ship

def run_game():

    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(screen)

    #开始游戏的主循环
    while True:

        #监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        ship.blitme()
        #每次循环都会重绘屏幕
        screen.fill(ai_settings.bg_color)

        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game()