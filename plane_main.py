#! /usr/bin/python3

import pygame
from plane_sprites import *

class PlaneGame(object):
    """ 飞机大战主游戏"""
    def __init__(self):
        print("游戏初始化。。。")
        # 1.创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3.调用私有方法，精灵与精灵组的创建
        self.__creat_sprites()
        # 4.设置定时器事件 -创建敌机 1s
        pygame.time.set_timer(CREAT_ENEMY_EVENT, 1000) # 后面数字以毫秒为单位
        pygame.time.set_timer(HERO_FIRE_EVENT, 500) # 子弹发射事件

    def __creat_sprites(self):  # __名称__    私有方法
        # 创建背景精灵与背景精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵与精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)



    def start_game(self):
        print("游戏开始。。。")
        while True:
            # 1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2.事件监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新/绘制精灵组
            self.__update_sprites()
            # 5.更新显示
            pygame.display.update()
            pass

    def __event_handler(self):
        for event in pygame.event.get():
            # 判断是否点击退出
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()  #  静态方法调用
            elif event.type == CREAT_ENEMY_EVENT:
                # print("敌机出场。。。")
                #  创建敌机精灵
                enemy = Enemy()
                #  添加到敌机精灵组
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

            # 此种方式按下弹起算是一个按键事件
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右边移动。。。")

            # 使用键盘提供的方法获取键盘按键  - 按键元组
            # 可以按下某个按键不放，一直使用按键事件
            keys_pressed = pygame.key.get_pressed()
            # 判断元组中按键索引值 1
            if keys_pressed[pygame.K_RIGHT]:
                self.hero.speed = 2

            elif keys_pressed[pygame.K_LEFT]:
                self.hero.speed = -2

            # elif keys_pressed[pygame.K_DOWN]:
            #     self.hero.speedy = 2
            #
            # elif keys_pressed[pygame.K_UP]:
            #     self.hero.speedy = -2

            else:
                self.hero.speed = 0

    def __check_collide(self):
        # 1. 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True,True)
        # 2. 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        # 判断列表时候有内容
        if len(enemies) > 0:
            # 让英雄牺牲
            self.hero.kill()
            # 结束游戏
            PlaneGame.__game_over()


    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)


        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        # 子弹
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    # 静态方法
    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()



if __name__ == '__main__':    # 表明只在本模块内实现，其他的调用也不会是实现
    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()