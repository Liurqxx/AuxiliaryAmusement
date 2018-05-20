# _*_ coding:utf-8 _*_
# Author:liu
from PIL import Image
import numpy as np
import subprocess
from io import BytesIO
import random
import os
import json
import time
import re

'''
    需要安装的库:
        1:PIL 安装方式:https://blog.csdn.net/xiamoyanyulrq/article/details/80375449
        2:numpy  安装方式:https://blog.csdn.net/xiamoyanyulrq/article/details/80375544
    基本操作:
        1:手机打开usb调试模式连接电脑,电脑需安装adb驱动,同时连接电脑
        2:手机端运行游戏
        3:运行该程序,按下回车即可开始
    基本思路:
        1:执行adb shell命令获取屏幕截图
        2:对截图进行二值化,并且进行纵向和横向切割,得到包含关键数据的图片
        3:对初次处理后的图片进行文字提取
        4:计算图片中的公式是否正确,得到答案
        5:程序根据结果自动点击对应的按钮

'''

# 点击屏幕的参数,根据手机分辨率调整
config = {
    # 不同的手机分辨率不同,参数也就不同
    '点击参数': {
        'point': [
            (100, 1450, 450, 1800),
            (600, 1450, 1000, 1800),
        ]
    }
}


# 图片二值化
def binarize(img, threshold=200):
    """二值化"""
    img = img.convert('L')
    table = []
    for i in range(256):
        if i > threshold:
            table.append(0)
        else:
            table.append(1)
    bin_img = img.point(table, '1')
    return bin_img



# 图片横向切割
def horizontal_cut(img):
    """横向切割"""
    # width:1000
    width, _ = img.size
    px = list(np.sum(np.array(img) == 0, axis=1))
    # 列表保存像素累加值大于0的行
    y0 = []
    for y in range(len(px)):
        # print(type(px[y]), px[y])
        if px[y] > 1:
            y0.append(y)

    # 找出边界
    cut_list = [y0[0]]
    # print('边界:', cut_list)
    for i in range(1, len(y0)):
        # 后一个数大于前一个数
        if abs(y0[i] - y0[i - 1]) > 1:
            # 添加两个数
            cut_list.extend([y0[i - 1], y0[i]])
    cut_list.append(y0[-1])
    # print('处理后cut_list:', cut_list)

    # 切割顺利的话应该是长度为4的list
    if len(cut_list) == 4:
        # 0  248  1000  372
        # 0  424  1000  539
        cut_img1 = img.crop([0, cut_list[0], width, cut_list[1]])
        cut_img2 = img.crop([0, cut_list[2], width, cut_list[3]])
        return [cut_img1, cut_img2]
    else:
        print('第一次失败,再一次...')
        # 重新截图
        scr = get_screenshot()
        scr = scr.crop([0, 700, 1080, 1200])
        width, _ = scr.size
        px = list(np.sum(np.array(scr) == 0, axis=1))
        # print(px)
        # 列表保存像素累加值大于0的行
        y0 = []
        for y in range(len(px)):
            # print(type(px[y]), px[y])
            if px[y] > 1:
                y0.append(y)

        print('y0==', y0)

        # 找出边界
        cut_list = [y0[0]]
        # print('边界:', cut_list)
        for i in range(1, len(y0)):
            # 后一个数大于前一个数
            if abs(y0[i] - y0[i - 1]) > 1:
                # 添加两个数
                cut_list.extend([y0[i - 1], y0[i]])
        cut_list.append(y0[-1])
        print('处理后cut_list:', cut_list)
        if len(cut_list) == 4:
            # 0  248  1000  372
            # 0  424  1000  539
            cut_img1 = img.crop([0, cut_list[0], width, cut_list[1]])
            cut_img2 = img.crop([0, cut_list[2], width, cut_list[3]])
            return [cut_img1, cut_img2]
        return


# 计算哈希值
def hashing(img):
    """计算哈希值"""
    img = img.resize((20, 30), Image.LANCZOS).convert("L")
    px = np.array(img).flatten()
    hash_val = (px > px.mean()).astype(int)
    hash_val = ''.join(str(e) for e in hash_val)
    return hash_val


# 计算汉明距离
def hamming(hash1, hash2):
    """计算汉明距离"""
    if len(hash1) != len(hash2):
        # print('hash1: ', hash1)
        # print('hash2: ', hash2)
        raise ValueError("Undefined for sequences of unequal length")

    return sum(i != j for i, j in zip(hash1, hash2))


# 文字提取
def recognize(img):
    """输入：经过裁剪的含有等式的区域图像"""
    img = img.convert('L')
    img = binarize(img)

    h_cut_imgs = horizontal_cut(img)
    chars1 = vertical_cut(h_cut_imgs[0])
    chars2 = vertical_cut(h_cut_imgs[1])

    with open('HashFiles/hash.json', 'r') as fp:
        hash_vals = json.load(fp)

    # 相近度列表
    nearness1 = {}
    expr = ''
    for char in chars1:
        hash_val = hashing(char)
        for h in hash_vals:
            nearness1[h] = hamming(hash_val, hash_vals[h])
        expr += sorted(nearness1.items(), key=lambda d: d[1])[0][0]

    nearness2 = {}
    for char in chars2:
        hash_val = hashing(char)
        for h in hash_vals:
            nearness2[h] = hamming(hash_val, hash_vals[h])
        expr += sorted(nearness2.items(), key=lambda d: d[1])[0][0]

    expr = expr.replace('subtract', '-').replace('plus', '+').replace('equal', '=')
    # print(len(expr))
    return expr


# 获取手机截图
def get_screenshot():
    # 执行该命令获取手机的图片
    process = subprocess.Popen("adb shell screencap -p", shell=True, stdout=subprocess.PIPE)
    screenshot = process.stdout.read()
    # 格式化
    screenshot = screenshot.replace(b"\r\r\n", b"\n")
    # 将图片信息保存到图片中,此处用于测试
    # with open('test.png', 'wb') as f:
    #     f.write(screenshot)
    # 创建内存对象
    img_fb = BytesIO()
    # 将图片信息写入到内存中
    img_fb.write(screenshot)
    # 处理图片
    img = Image.open(img_fb)
    return img


# 判断结果
def is_show(text_info):
    # (9 - 5 = -6)
    # 获取加减符号
    result_fuhao = re.findall('([-,+])', text_info)

    # 获取 - + 的索引值
    index1 = text_info.find(result_fuhao[0])

    # 获取 = 的索引值
    index2 = text_info.find('=')

    # 由于不确定数字是几位数,所以使用切片获取三部分
    num1 = text_info[:index1]  # 第一个数字
    num1 = num1.strip()
    num2 = text_info[index1 + 1:index2]  # 第二个数字
    num2 = num2.strip()
    num3 = text_info[index2 + 1:]  # 最后的结果
    num3 = num3.strip()

    # print(num1, num2, result)
    if result_fuhao[0] == '-':
        if int(num1) - int(num2) == int(num3):
            return True
        return False
    else:
        if int(num1) + int(num2) == int(num3):
            return True
        return False


# 点击屏幕
def click(point):
    """点击屏幕"""
    cmd = "adb shell input swipe %s %s %s %s %s" % (
        point[0],
        point[1],
        point[0] + random.randint(0, 3),
        point[1] + random.randint(0, 3),
        100
    )
    os.system(cmd)


if __name__ == '__main__':
    input('输入回车进行操作:')
    while True:
        # 获取手机屏幕截图
        scr = get_screenshot()
        # crop() : 从图像中提取出某个矩形大小的图像。它接收一个四元素的元组作为参数，
        # 各元素为（left, upper, right, lower），坐标系统的原点（0, 0）是左上角。
        scr = scr.crop([0, 700, 1080, 1200])
        # # 获取图片内文字 (9-5=6)
        result = recognize(scr)
        is_show_result = is_show(result)
        print(result, is_show_result)
        # print(is_show_result)
        if is_show_result:
            # 结果正确
            click(config['点击参数']['point'][0])
        else:
            # 结果错误
            click(config['点击参数']['point'][1])
            # time.sleep(0.02)

