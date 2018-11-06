class Settings():
    """"存储 所有设置信息的类"""
    def __init__(self):
        """初始化游戏设置"""
        """屏幕设置"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        """飞船设置"""
        self.ship_speed_factor = 1.0
        self.ship_limit = 3

        """子弹设置"""
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 7

        """外星人设置"""
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        """fleet_direction 1 表示右移， 否则是左"""
        self.fleet_direction = 1
