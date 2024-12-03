import pygame
import logging
from featuretoggles import TogglesList


# 定義功能開關類
class ReleaseToggles(TogglesList):
    feature1: bool
    feature2: bool
    feature3: bool


# 初始化功能開關
toggles = ReleaseToggles('toggles.yaml')


# 初始化 Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Feature Toggles Example")

# 顏色定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)

# 字體
font = pygame.font.Font(None, 36)

# 按鈕的矩形區域
button_rect = pygame.Rect(250, 250, 300, 50)


# 主函數
def main():
    running = True
    while running:
        # 填充背景
        screen.fill(WHITE)

        # 處理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 畫按鈕（如果 feature1=True）
        if toggles.feature1:
            pygame.draw.rect(screen, GRAY, button_rect)  # 畫矩形按鈕
            button_text = font.render("FT1 is activated.", True, BLACK)
            screen.blit(button_text, button_rect.move(50, 10))  # 按鈕文字

        # 顯示文字（如果 feature2=True）
        if toggles.feature2:
            if toggles.feature3:
                text_content = "FT2 is activated, and FT3 is, too."
            else:
                text_content = "FT2 is activated, but FT3 is deactivated."
            text = font.render(text_content, True, BLUE)
            screen.blit(text, (200, 150))  # 調整文字顯示位置

        # 更新畫面
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
