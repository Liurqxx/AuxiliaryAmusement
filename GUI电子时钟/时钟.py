# _*_ coding:utf-8 _*_
# Author:liu
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QVBoxLayout, QDesktopWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
import sys

from PyQt5.QtWidgets import QDesktopWidget

'''
QLCDNumber:用于显示数字
QWidget:窗口的基类

'''


class MyTime(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init_timer()

    def update_time(self):
        '''更新时间'''
        self.lcd.display(time.strftime('%X', time.localtime()))

    def init_timer(self):
        '''时间的显示'''
        self.timer = QTimer()
        # 设置定时器时间,每一秒触发一次  触发timeout方法
        self.timer.setInterval(1000)

        # 启动定时器
        self.timer.start()

        # 定时器触发调用时间更新方法
        self.timer.timeout.connect(self.update_time)

    def initUI(self):
        '''窗口大小
        参数:高度,宽度

        '''
        self.resize(250, 150)
        # 标题
        self.setWindowTitle('电子时钟')
        self.move_center()
        # 显示组件
        self.lcd = QLCDNumber()

        # 要显示的数字个数
        self.lcd.setDigitCount(10)

        # 采用十进制模式
        self.lcd.setMode(QLCDNumber.Dec)

        # 设置平面模式
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        # 时间元组   time.localtime()设置本地时间
        self.lcd.display(time.strftime('%X', time.localtime()))

        # 构建一个盒子布局
        self.main_layout = QVBoxLayout()
        # 把上面的组件添加到盒子布局中
        self.main_layout.addWidget(self.lcd)
        # 设置组件的位置,设置居中
        self.main_layout.setAlignment(Qt.AlignCenter)

        # 设置给顶层布局
        self.setLayout(self.main_layout)

        # 设置颜色
        self.main_p = QPalette()
        # 设置背景色
        self.main_p.setColor(QPalette.Background, Qt.darkCyan)
        # 自动填充背景颜色
        self.setAutoFillBackground(True)
        # 颜色设置给住窗口
        self.setPalette(self.main_p)

        # 显示界面
        self.show()

    def move_center(self):
        '''设置矩形'''
        my_rect = self.frameGeometry()
        # 获取整个屏幕的中心
        w_center_point = QDesktopWidget().availableGeometry().center()
        my_rect.moveCenter(w_center_point)
        # # 从左上角开始移动,直到中间
        self.move(my_rect.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_time = MyTime()
    # 运行程序
    sys.exit(app.exec_())
