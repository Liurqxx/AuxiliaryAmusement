import pygame
import core_data


def show(a=10):
    pass


# 地图类
class GameMap(object):
    def __init__(self):
        # 加载图片创建两个图片对象
        self.bg_img1 = pygame.image.load("res/img_bg_level_5.jpg")
        self.bg_img2 = pygame.image.load("res/img_bg_level_5.jpg")

        # 获取背景图片矩形对象
        self.bg_img1_rect = self.bg_img1.get_rect()
        self.bg_img2_rect = self.bg_img2.get_rect()

        # 修改矩形对象y坐标
        self.bg_img1_rect[1] = 0 - core_data.SCREEN_HEIGHT
        self.bg_img2_rect[1] = 0

        # 地图滚动速度
        self.map_speed = 3

    # 滚动图片
    def scroll_map(self):
        # 移动矩形对象
        self.bg_img2_rect.move_ip(0, self.map_speed)
        self.bg_img1_rect.move_ip(0, self.map_speed)
        # 判断矩形对象是否超出屏幕如果某个矩形对象超出屏幕设置到屏幕顶部的外面显示
        if self.bg_img2_rect[1] >= core_data.SCREEN_HEIGHT:
            print("第二个图片超出屏幕啦")
            # 重置位置到屏幕的外面
            self.bg_img2_rect[1] = -core_data.SCREEN_HEIGHT

        if self.bg_img1_rect[1] >= core_data.SCREEN_HEIGHT:
            print("第一个图片超出屏幕啦")
            # 重置位置到屏幕的外面
            self.bg_img1_rect[1] = -core_data.SCREEN_HEIGHT

