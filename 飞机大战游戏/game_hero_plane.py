import pygame
import core_data
import game_bullet


# 英雄飞机类
class HeroPlane(object):
    def __init__(self):
        # 加载图片，创建图片对象
        self.hero_img = pygame.image.load("res/hero2.png")
        # 获取图片矩形对象，以后矩形对象移动到哪里，图片对象就绘制到那个地方
        self.hero_img_rect = self.hero_img.get_rect()
        # 修改矩形对象的位置
        self.hero_img_rect[0] = core_data.SCREEN_WIDTH / 2 - self.hero_img_rect[2] / 2
        self.hero_img_rect[1] = core_data.SCREEN_HEIGHT - self.hero_img_rect[3] - 20
        # 移动速度
        self.hero_speed = 5
        # 携带子弹列表
        self.bullet_list = [game_bullet.Bullet() for _ in range(5)]

    # 重置飞机位置
    def reset(self):
        # 修改矩形对象的位置
        self.hero_img_rect[0] = core_data.SCREEN_WIDTH / 2 - self.hero_img_rect[2] / 2
        self.hero_img_rect[1] = core_data.SCREEN_HEIGHT - self.hero_img_rect[3] - 20

    # 发射子弹
    def shot(self):
        # 遍历子弹，判断子弹的状态
        for bullet in self.bullet_list:
            if not bullet.is_shot:
                # 发射子弹
                # 修改子弹的状态
                bullet.is_shot = True
                bullet_x = self.hero_img_rect[0] + self.hero_img_rect[2] / 2 - bullet.bullet_img_rect[2] / 2
                # 修改子弹的位置到飞机头部
                bullet.bullet_img_rect[0] = bullet_x
                bullet.bullet_img_rect[1] = self.hero_img_rect[1] - bullet.bullet_img_rect[3]
                # 只发射一颗子弹，找到一颗未发射的子弹，把子弹状态进行修改然后跳出循环，不再修改后面子弹的状态
                break

    # 上
    def move_up(self):
        # y轴大于屏幕的顶部坐标（0）才能往上移动
        if self.hero_img_rect[1] > 0:
            self.hero_img_rect.move_ip(0, -self.hero_speed)

    # 下
    def move_down(self):
        # y轴小于屏幕的高度减去飞机高度才能往下移动
        if self.hero_img_rect[1] < core_data.SCREEN_HEIGHT - self.hero_img_rect[3]:
            self.hero_img_rect.move_ip(0, self.hero_speed)

    # 左
    def move_left(self):
        # x轴大于0表示可以往左边移动
        if self.hero_img_rect[0] > 0:
            self.hero_img_rect.move_ip(-self.hero_speed, 0)

    # 右
    def move_right(self):
        # x轴小于屏幕宽度减去自身的宽度才可以往右移动
        if self.hero_img_rect[0] < core_data.SCREEN_WIDTH - self.hero_img_rect[2]:
            self.hero_img_rect.move_ip(self.hero_speed, 0)
