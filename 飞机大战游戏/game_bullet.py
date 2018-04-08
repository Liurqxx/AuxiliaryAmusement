import random
import pygame


# 子弹类
class Bullet(object):
    def __init__(self):
        # 产生随机数字
        num = random.randint(8, 13)
        # 加载图片，创建图片对象
        self.bullet_img = pygame.image.load("res/bullet_%d.png" % num)

        # 获取图片的矩形对象
        # 提示： 子弹矩形对象不做调整，因为飞机的位置我们现在不能确定，等飞机发射子弹的时候获取飞机的位置，然后在设置子弹在飞机头部
        self.bullet_img_rect = self.bullet_img.get_rect()

        # 子弹状态
        self.is_shot = False
        # 子弹的移动速度
        self.bullet_speed = 5

    # 向上移动
    def move_up(self):
        self.bullet_img_rect.move_ip(0, -self.bullet_speed)
        # 判断子弹是否超出屏幕
        if self.bullet_img_rect[1] < -self.bullet_img_rect[3]:
            # 回收这颗子弹，把状态进行修改
            self.is_shot = False