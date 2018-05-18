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



@time_it
def vertical_cut(img):
    """纵向切割"""
    _, height = img.size
    px = list(np.sum(np.array(img) == 0, axis=0))
    # 列表保存像素累加值大于0的列
    x0 = []
    for x in range(len(px)):
        if px[x] > 1:
            x0.append(x)

    # 找出边界
    cut_list = [x0[0]]
    for i in range(1, len(x0)):
        if abs(x0[i] - x0[i - 1]) > 1:
            cut_list.extend([x0[i - 1], x0[i]])
    cut_list.append(x0[-1])

    cut_imgs = []
    # 切割顺利的话应该是整对
    if len(cut_list) % 2 == 0:
        for i in range(len(cut_list) // 2):
            cut_img = img.crop([cut_list[i * 2], 0, cut_list[i * 2 + 1], height])
            cut_imgs.append(cut_img)
        return cut_imgs
    else:
        print('Vertical cut failed.')
        return


@time_it
def horizontal_cut(img):
    """横向切割"""
    width, _ = img.size
    px = list(np.sum(np.array(img) == 0, axis=1))
    # 列表保存像素累加值大于0的行
    y0 = []
    for y in range(len(px)):
        if px[y] > 1:
            y0.append(y)

    # 找出边界
    cut_list = [y0[0]]
    for i in range(1, len(y0)):
        if abs(y0[i] - y0[i - 1]) > 1:
            cut_list.extend([y0[i - 1], y0[i]])
    cut_list.append(y0[-1])

    # 切割顺利的话应该是长度为4的list
    if len(cut_list) == 4:
        cut_img1 = img.crop([0, cut_list[0], width, cut_list[1]])
        cut_img2 = img.crop([0, cut_list[2], width, cut_list[3]])
        return [cut_img1, cut_img2]
    else:
        print('Horizontal cut failed.')
        return


def hashing(img):
    """计算哈希值"""
    img = img.resize((20, 30), Image.LANCZOS).convert("L")
    px = np.array(img).flatten()
    hash_val = (px > px.mean()).astype(int)
    hash_val = ''.join(str(e) for e in hash_val)
    return hash_val


def hamming(hash1, hash2):
    """计算汉明距离"""
    if len(hash1) != len(hash2):
        # print('hash1: ', hash1)
        # print('hash2: ', hash2)
        raise ValueError("Undefined for sequences of unequal length")

    return sum(i != j for i, j in zip(hash1, hash2))


@time_it
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
    # 将图片信息保存到图片中
    # with open('test.png', 'wb') as f:
    #     f.write(screenshot)
    # time.sleep(0.2)

    # 将图片信息写入到内存中
    img_fb = BytesIO()
    img_fb.write(screenshot)
    # # 处理图片
    img = Image.open(img_fb)
    return img


# 判断结果
def is_show(text_info):
    # (9 - 5 = 6)
    result_fuhao = re.findall('([-,+])', text_info)
    # print(result_fuhao[0])
    # print(result[0])
    num1 = text_info.split(result_fuhao[0])[0]
    num2 = text_info.split(result_fuhao[0])[1].split('=')[0]
    result = text_info.split(result_fuhao[0])[1].split('=')[1]
    # print(num1, num2, result)
    if result_fuhao[0] == '-':
        if int(num1) - int(num2) == int(result):
            return True
        return False
    else:
        if int(num1) + int(num2) == int(result):
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
    while True:
        input('输入回车进行操作:')
        # 获取手机屏幕截图
        scr = get_screenshot()
        # print(type(scr))
        scr = scr.crop([0, 750, 1080, 1150])

        # # print(scr)
        # # 获取图片内文字 (9-5=6)
        result = recognize(scr)
        # print(result)
        print(recognize(scr))
        is_show_result = is_show(result)
        print(is_show_result)
        if is_show_result:
            # 结果正确
            click(config['点击参数']['point'][0])
        else:
            # 结果错误
            click(config['点击参数']['point'][1])
