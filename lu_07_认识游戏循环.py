import pygame

pygame.init()

# 设置窗口 480*700
screen = pygame.display.set_mode((480,700))
# 第一个参数是元组，控制窗口大小，第二个是flag 即是是否可以全屏，默认不可以，第三个是参数表示颜色位数，默认自动匹配

# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0,0))
# pygame.display.update()

# 绘制英雄飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))  # 后面的数值代表放置的水平位置（水平， 垂直）

# 绘制完成后统一用update 更新
pygame.display.update()

#绘制时钟对象
clock = pygame.time.Clock()


i = 1

while True:
    clock.tick(1)
    # 可以指定循环体内部代码执行频率
    i+=1
    print(i)
    pass

pygame.quit()