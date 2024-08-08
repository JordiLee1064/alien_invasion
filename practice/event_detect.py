import sys
import pygame

class Event_detection:
    """管理资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()

        self.screen_width = 1200
        self.screen_height = 800

        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        pygame.display.set_caption("event detection")

    def run_game(self):
        """开始主循环"""
        while True:
            self._check_events()

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)

if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = Event_detection()
    ai.run_game()