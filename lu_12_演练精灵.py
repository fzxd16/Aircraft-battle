import pygame
# import plane_sprites
from plane_sprites import *  # from导入不用和import导入一样，使用 模块名.方法 导入，可以直接使用

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
screen.blit(hero, (150, 300))  # 后面的数值代表放置的水平位置（水平， 垂直）

# 绘制完成后统一用update 更新
pygame.display.update()

#绘制时钟对象
clock = pygame.time.Clock()

# 定义rect的最初位置
hero_rect = pygame.Rect(150, 300, 102, 126)


# 创建敌机精灵
enemy = GameSprit("./images/enemy1.png")
enemy1 = GameSprit("./images/enemy1.png", 2)
# 创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)




while True:
    # 可以指定循环体内部代码执行频率
    clock.tick(60)

    # 创建监听
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            print("游戏退出。。。。")
            # quit卸载所有模块
            pygame.quit()
            # exit()
            exit()

    # 2. 修改飞机位置
    hero_rect.y -= 1
    # 判断是否飞出背景
    if hero_rect.y <= -126:
        hero_rect.y = 700
    # 3. 使用blit绘制图形
    screen.blit(bg, (0,0))
    screen.blit(hero, hero_rect)



    # 让精灵组调用两个方法
    # update - 让组中所有精灵更新位置
    enemy_group.update()
    # draw - 在screen 上更新所有位置
    enemy_group.draw(screen)


    # 4. 调用update方法更新
    pygame.display.update()



pygame.quit()