import pygame

pygame.init()

# 设置窗口 480*700
screen = pygame.display.set_mode((480,700))
# 第一个参数是元组，控制窗口大小，第二个是flag 即是是否可以全屏，默认不可以，第三个是参数表示颜色位数，默认自动匹配

# 绘制背景图像
# <1.加载图像
bg = pygame.image.load("./images/background.png")
# <2.blit绘制图像
screen.blit(bg, (0,0))
# <3.update 更新屏幕
pygame.display.update()
while True:
    pass

pygame.quit()