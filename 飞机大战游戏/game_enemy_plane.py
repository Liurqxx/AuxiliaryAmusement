import random
import pygame
import core_data


# 定义敌机类
class EnemyPlane(object):
    def __init__(self):
        # 产生随机数字 1-7
        num = random.randint(1, 7)
        # 加载图片，创建图片对象
        self.enemy_img = pygame.image.load("res/img-plane_%d.png" % num)
        # 获取敌机的矩形对象，以后根据矩形对象的位置绘制敌机显示的位置
        self.enemy_img_rect = self.enemy_img.get_rect()
        # 修改敌机矩形对象的位置
        self.enemy_img_rect[0] = random.randint(0, core_data.SCREEN_WIDTH - self.enemy_img_rect[2])
        self.enemy_img_rect[1] = -self.enemy_img_rect[3]

        # 随机产生移动速度
        self.enemy_speed = random.randint(4, 6)
        # self.reset()

    # 敌机绘制重置
    def reset(self):
        self.enemy_img_rect[0] = random.randint(0, core_data.SCREEN_WIDTH - self.enemy_img_rect[2])
        self.enemy_img_rect[1] = -self.enemy_img_rect[3]

        # 随机产生移动速度
        self.enemy_speed = random.randint(4, 6)

    # 向下移动
    def move_down(self):
        self.enemy_img_rect.move_ip(0, self.enemy_speed)
        if self.enemy_img_rect[1] > core_data.SCREEN_HEIGHT:
            # 重置敌机位置
            self.reset()