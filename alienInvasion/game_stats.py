class GameStats():
    """跟踪游戏统计游戏信息"""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        """令游戏一开始处于非活跃状态,添加按钮开始游戏"""
        self.game_active = True

    def reset_stats(self):
        """初始化游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
