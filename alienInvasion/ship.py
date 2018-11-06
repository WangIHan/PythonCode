import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """初始化飞船设置其初始属性"""
        self.screen = screen
        """加载飞船图形并获取其全部外观图形"""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        """将每艘新飞船放在屏幕底部中央"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        """在飞船属性center中设置小数值"""
        self.center = float(self.rect.centerx)

        self.ai_settings = ai_settings

        """移动标志"""
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志调整飞船位置"""
        """更新飞船的center值，而不是rect"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            """self.rect.centerx += 1"""
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            """self.rect.centerx -= 1"""
            self.center -= self.ai_settings.ship_speed_factor
        """根据self.center 更新rect对象"""
        self.rect.centerx = self.center

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
