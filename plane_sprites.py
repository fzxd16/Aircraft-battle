import random
import pygame

# 屏幕大小的常量, 类似宏定义
SCREEN_RECT = pygame.Rect(0,0,480,700)
# 刷新的帧率 FPS
FRAME_PER_SEC = 60
# 创建敌方机器出现定时器常量
CREAT_ENEMY_EVENT = pygame.USEREVENT
# 创建子弹发射定时器常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprit(pygame.sprite.Sprite):  # 第一个sprite是基类名称， 第二个Sprite是类的名称
    """飞机大战游戏精灵"""
    def __init__(self, image_name, speed = 1):
        #调用父类的初始化方法
        super().__init__()
        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()  #  get_rect可以获得图像
        self.speed = speed
        # y数值移动用
        self.speedy = 0


    def update(self):
        # 在屏幕的垂直方向移动
        self.rect.y += self.speed


class Background(GameSprit):
    """游戏背景精灵"""
    def __init__(self,is_alt = False):
        # 继承父类，实现精灵的创建image/rect/speed
        super().__init__("./images/background.png")
        # 判断是否是交替图像，如果是则要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1.调用父类方法实现
        super().update()
        # 2.判断是否超出屏幕，移动出屏幕，将图片设置到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprit):
    """敌机精灵"""
    def __init__(self):

        # 1.调用父类方法，创建敌机精灵，并且指定敌机图片
        super().__init__("./images/enemy1.png")
        # 2.指定敌机初始随机速度 1-3
        self.speed = random.randint(1, 3)
        # 3.指定敌机初始随机位置
        self.rect.bottom = 0  # bottom 等于0 - 物体长度 ，即是飞机头俄位置可以缓慢进入
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)

        pass

    def update(self):
        # 1.调用父类方法，保证垂直飞行
        super().update()
        # 2.判断是否飞出屏幕，如果飞出，从精灵组中删除
        if self.rect.y > SCREEN_RECT.height:
            # print("飞出屏幕 需要从精灵组中删除....")
            # kill方法可以将敌机精灵从所有精灵组中移除，敌机精灵便会被销毁 下面的__del__便会调用
            self.kill()

    def __del__(self):
        # print("敌机挂了 %s" % self.rect)

        pass



class Hero(GameSprit):
    """ 英雄精灵"""
    def __init__(self):
        # 1.调用父类方法，设置image 和speed
        super().__init__("./images/me1.png", 0)
        # 2. 设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 3.设置子弹的精灵组
        self.bullets =  pygame.sprite.Group()

    def update(self):
        #英雄水平方向移动
        self.rect.x += self.speed
        # 垂直方向移动
        # self.rect.y += self.speedy

        # 控制英雄不能离开屏幕
        if self.rect.x < -51:
            self.rect.x = -51
        elif self.rect.right > SCREEN_RECT.right + 51:
            self.rect.right = SCREEN_RECT.right + 51

    def fire(self):
        print("发射子弹。。。")
        for i in (0,1,2):
            # 1.创建子弹精灵
            bullet = Bullet()
            # 2. 设置精灵位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 3. 将子弹精灵添加到精灵组
            self.bullets.add(bullet)



class Bullet(GameSprit):
    """子弹精灵"""
    def __init__(self):
        # 调用父类方法，设置子弹图片与速度
        super().__init__("./images/bullet1.png", -2)


    def update(self):
        # 调用父类方法，让子弹垂直方向移动
        super().update()
        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹被销毁。。。")
