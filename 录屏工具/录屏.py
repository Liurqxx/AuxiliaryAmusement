# _*_coding:utf-8_*_
# Author:liu
'''
    windows下录屏工具
	仅限于Windows系统

'''
import threading, os, time, sys
from PIL import ImageGrab
from moviepy.editor import ImageSequenceClip


def get_pictures():
    global recordTime
    t = time.time()
    while recording:
        # 抓取当前屏幕的快照，返回一个模式为“RGB”的图像
        image = ImageGrab.grab()
        # 将多个路径组合后返回  此处是路径+文件名
        imageName = os.path.join(fileName, '%s.jpg' % int(time.time() * 1e3))
        print("imageName=%s" % imageName)
        # 保存快照
        image.save(imageName)
        imageList.append(imageName)
        # 以时间差作图片名
        recordTime = time.time() - t


if __name__ == '__main__':

    fileName = input('请输入保存文件的文件夹: ')
    # 创建文件夹
    if not os.path.isdir(fileName):
        os.mkdir(fileName)

    # 用于控制是否结束程序
    recording = True
    # 图像列表
    imageList = []
    # 时间差
    recordTime = 0

    # 创建线程
    t = threading.Thread(target=get_pictures, daemon=True)
    t.start()
    print('Recording screen to %s.mp4, press Ctrl-C to stop' % fileName)

    try:
        while 1:
            input()
    except Exception as e:
        recording = False
        # ImageSequenceClip 用于合成图像 fps:每秒中填充图像的帧数(帧/秒),数值越大，图像越清晰
        print("imageList:%s----fps=%d" % (imageList, int(len(imageList) / recordTime)))
        clip = ImageSequenceClip(imageList, fps=int(len(imageList) / recordTime))
        # 保存图像
        clip.write_videofile('%s.mp4' % fileName)
