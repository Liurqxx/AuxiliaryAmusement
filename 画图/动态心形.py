# _*_ coding:utf-8 _*_
# Author:liu

from turtle import *


def line(size):
    speed(1)
    forward(51 * size)


def heart(x, y, size):
    go_to(x, y)
    left(150)
    begin_fill()
    line(size)

    arrow()
    arrowHead()
    go_to(400, -300)
    write('author:夏沫烟雨', move=True,
          align='left', font=('宋体', 30, 'normal'))
    done()


main()
