# _*_coding:utf-8_*_
# Author:liu
import random
from tkinter import *

'''
    生成抽象图画
'''


def random_rectangle(width, height, myColor):
    # 随机生成一个偶数,保证y>x
    x = random.randrange(width)
    y = x + random.randrange(width)
    x1 = random.randrange(height)
    y1 = x1 + random.randrange(height)
    # 绘制矩形
    canvas.create_rectangle(x, y, x1, y1, fill=myColor)


if __name__ == '__main__':
    # 创建窗口
    tk = Tk()
    # 设置标题
    tk.title('抽象绘制')
    # 创建画布,指定宽高和背景颜色,
    canvas = Canvas(tk, width=500, height=500, bg='white')
    # 显示画布
    canvas.pack()
    # 颜色列表
    myColor = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']


    # 循环绘制两百个矩形
    for num in range(0, 200):
	# 绘制每个图形
        random_rectangle(350, 280, myColor[num % 7])

    tk.mainloop()
