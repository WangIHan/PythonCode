import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button

def run_game():
    """始化游戏创建屏幕对象"""
    pygame.init()
    """设置类实例化"""
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    """传入的是一个向量而非两个参数"""
    pygame.display.set_caption("Alien Invasion")
    """创建按钮Play"""
    play_button = Button(ai_settings, screen, "Play")

    """创建一个用于统计游戏信息的实例"""
    stats = GameStats(ai_settings)
    """设置背景色"""
    bg_color = (230, 230, 230)
    """创建飞船"""
    ship = Ship(ai_settings, screen)
    """创建存储子弹的编组"""
    bullets = Group()
    """创建外星人"""
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    """开始游戏主循环"""
    while True:
        """监视键盘鼠标操作"""
        """for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)
        绘制飞船
        ship.blitme()"""

        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)
        """最近屏幕显示可见"""
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, bullets, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)


        """bullets.update()
        
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
            print(len(bullets))"""

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


run_game()
