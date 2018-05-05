# _*_ coding:utf-8 _*_
# Author:liu

'''
    把一张图片切成9张图片
'''
from PIL import Image
import sys


# 将图片填充为正方形
def fill_image(image):

if __name__ == '__main__':
    file_path = "img.jpg"
    image = Image.open(file_path)
    # image.show()
    image = fill_image(image)
    # image.show()
    image_list = cut_image(image)
    save_images(image_list)
