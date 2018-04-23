import pyautogui
import time


#
# print('Press Ctrl-C to quit')
#
# try:
#     # while True:
#     # ToDo: Get and print the mouse coordinates
#     x, y = pyautogui.position()
#     positionStr = 'X: ' + str(x) + ' Y: ' + str(y)
#     time.sleep(5)
#     # pyautogui.click(button='left') # 点击鼠标左键
#     # pyautogui.doubleClick() #双击
#     print(positionStr + '  check')
#     pyautogui.click()
#     distance = 200
#     while distance > 0:
#         pyautogui.dragRel(distance, 0, duration=0.2)  # move right
#         distance = distance - 5
#         pyautogui.dragRel(0, distance, duration=0.2)  # move down
#         pyautogui.dragRel(-distance, 0, duration=0.2)  # move down
#         distance = distance - 5
#         pyautogui.dragRel(0, -distance, duration=0.2)  # move up
#
# except KeyboardInterrupt:
#     print('end' + positionStr)
#     # print('\nDone')

# time.sleep(5)
# distance = 200
# while distance > 0:
#     pyautogui.dragRel(distance, 0, duration=0.5)  # move right
#     distance -= 5
#     pyautogui.dragRel(0, distance, duration=0.5)  # move down
#     pyautogui.dragRel(-distance, 0, duration=0.5)  # move left
#     distance -= 5
#     pyautogui.dragRel(0, -distance, duration=0.5)  # move up


def func():
    time.sleep(8)
    # 每个函数执行的间隔时间
    pyautogui.PAUSE = 0.2

    pyautogui.FAILSAFE = True
    # 当前坐标
    width, height = pyautogui.size()
    print(width, height)

    '''
    # moveTo函数，绝对坐标(移动), duration 移动时间不能太短，可能有些系统吃不消
    # moveRel函数，相对坐标(移动)
    # dragTo(x, y, duration=0.25)  用法与move一样，功能为拖拽
    pyautogui.click(x=cur_x, y=cur_y, button='') 三个按键可选:left, middle, right
    pyautogui.doubleClick()
    pyautogui.rightClick()
    pyautogui.middleClick()
    
    pyautogui.scroll() # 接收一个整数，整数往上，负数往下
    
    '''

    # for i in range(10):
    #     pyautogui.moveTo(300, 300, duration=0.25)
    #     pyautogui.moveTo(400, 300, duration=0.25)
    #     pyautogui.moveTo(400, 400, duration=0.25)
    #     pyautogui.moveTo(300, 400, duration=0.25)

    # pyautogui.moveTo(600, 250, duration=0.25)
    # pyautogui.dragTo(600, 250, duration=0.25)
    # pyautogui.dragTo(600, 150, duration=0.25)
    # pyautogui.dragTo(700, 150, duration=0.25)
    # pyautogui.dragTo(700, 250, duration=0.25)
    # pyautogui.dragTo(600, 250, duration=0.25)
    # pyautogui.moveTo(650, 250, duration=0.25)
    # pyautogui.dragTo(650, 250, duration=0.25)

    pyautogui.moveTo(600, 250, duration=0.25)
    pyautogui.dragRel(0, -90, duration=0.25)
    pyautogui.dragRel(100, 0, duration=0.25)
    pyautogui.dragRel(0, 90, duration=0.25)
    pyautogui.dragRel(-100, 0, duration=0.25)

    pyautogui.moveRel(50, 0, duration=0.25)
    pyautogui.dragRel(0, -90, duration=0.25)
    pyautogui.moveRel(-50, 30, duration=0.25)
    pyautogui.dragRel(25, 0, duration=0.25)
    pyautogui.moveRel(50, 0, duration=0.25)
    pyautogui.dragRel(0, 30, duration=0.25)
    pyautogui.moveRel(-25, 0, duration=0.25)
    pyautogui.dragRel(-25, 0, duration=0.25)

    pyautogui.moveRel(0, 30, duration=0.25)
    pyautogui.dragRel(0, 90, duration=0.25)
    pyautogui.dragRel(-50, 0, duration=0.25)
    pyautogui.dragRel(0, -90, duration=0.25)
    pyautogui.dragRel(25, 0, duration=0.25)

    pyautogui.moveRel(0, 30, duration=0.25)
    pyautogui.dragRel(50, 0, duration=0.25)
    pyautogui.moveRel(-25, 60, duration=0.25)
    pyautogui.dragRel(100, 0, duration=0.25)
    pyautogui.dragRel(0, -90, duration=0.25)
    pyautogui.dragRel(-50, 0, duration=0.25)
    pyautogui.dragRel(0, 90, duration=0.25)

    pyautogui.moveRel(25, -60, duration=0.25)
    pyautogui.dragRel(0, 30, duration=0.25)
    pyautogui.moveRel(-25, 0, duration=0.25)
    pyautogui.dragRel(-25, 0, duration=0.25)
    pyautogui.moveRel(-50, 0, duration=0.25)
    pyautogui.dragRel(-25, 0, duration=0.25)

    pyautogui.moveRel(0, 30, duration=0.25)
    pyautogui.dragRel(-25, 0, duration=0.25)
    pyautogui.dragRel(0, 90, duration=0.25)
    pyautogui.dragRel(200, 0, duration=0.25)
    pyautogui.dragRel(0, -90, duration=0.25)
    pyautogui.dragRel(-25, 0, duration=0.25)

    pyautogui.moveRel(-25, 0, duration=0.25)
    pyautogui.dragRel(0, 90, duration=0.25)
    pyautogui.moveRel(-50, 0, duration=0.25)
    pyautogui.dragRel(0, -90, duration=0.25)
    pyautogui.moveRel(-50, 0, duration=0.25)
    pyautogui.dragRel(0, 90, duration=0.25)

    # 9
    pyautogui.moveRel(-25, -15, duration=0.25)
    pyautogui.dragRel(0, -15, duration=0.25)
    pyautogui.dragRel(-25, 0, duration=0.25)
    pyautogui.moveRel(25, -30, duration=0.25)
    pyautogui.dragRel(0, -15, duration=0.25)

    # 4
    pyautogui.moveRel(50, -15, duration=0.25)
    pyautogui.dragRel(0, 60, duration=0.25)
    pyautogui.moveRel(-22, 27, duration=0.25)
    pyautogui.dragRel(22, 0, duration=0.25)
    pyautogui.moveRel(22, 0, duration=0.25)
    pyautogui.dragRel(0, -12, duration=0.25)
    pyautogui.moveRel(0, -12, duration=0.25)
    pyautogui.dragRel(0, -60, duration=0.25)

    # 2
    pyautogui.moveRel(3, 30, duration=0.25)
    pyautogui.dragRel(25, 0, duration=0.25)
    pyautogui.moveRel(0, 30, duration=0.25)
    pyautogui.dragRel(25, 0, duration=0.25)

    # 0
    pyautogui.moveRel(25, 0, duration=0.25)
    pyautogui.dragRel(0, -30, duration=0.25)

    #
    pyautogui.moveRel(25, 57, duration=0.25)
    pyautogui.dragRel(25, 0, duration=0.25)
    pyautogui.dragRel(0, 90, duration=0.25)
    pyautogui.dragRel(-250, 0, duration=0.30)
    pyautogui.dragRel(0, -90, duration=0.25)
    pyautogui.dragRel(25, 0, duration=0.25)
    pyautogui.moveRel(25, 0, duration=0.25)
    pyautogui.dragRel(0, 90, duration=0.25)
    pyautogui.moveRel(50, 0, duration=0.25)
    pyautogui.dragRel(0, -90, duration=0.25)
    pyautogui.moveRel(50, 0, duration=0.25)
    pyautogui.dragRel(0, 90, duration=0.25)
    pyautogui.moveRel(50, 0, duration=0.25)
    pyautogui.dragRel(0, -90, duration=0.25)

    # 5
    pyautogui.moveRel(-150, 30, duration=0.25)
    pyautogui.dragRel(-25, 0, duration=0.25)
    pyautogui.moveRel(0, 30, duration=0.25)
    pyautogui.dragRel(-25, 0, duration=0.25)

    # 9
    pyautogui.moveRel(50, 0, duration=0.25)
    pyautogui.dragRel(25, 0, duration=0.25)
    pyautogui.dragRel(0, 15, duration=0.25)
    pyautogui.moveRel(0, -45, duration=0.25)
    pyautogui.dragRel(0, -15, duration=0.25)

    # 4  2 0
    # 4
    pyautogui.moveRel(50, -15, duration=0.25)
    pyautogui.dragRel(0, 60, duration=0.25)
    pyautogui.moveRel(-22, 27, duration=0.25)
    pyautogui.dragRel(22, 0, duration=0.25)
    pyautogui.moveRel(22, 0, duration=0.25)
    pyautogui.dragRel(0, -12, duration=0.25)
    pyautogui.moveRel(0, -12, duration=0.25)
    pyautogui.dragRel(0, -60, duration=0.25)

    # 2
    pyautogui.moveRel(3, 30, duration=0.25)
    pyautogui.dragRel(25, 0, duration=0.25)
    pyautogui.moveRel(0, 30, duration=0.25)
    pyautogui.dragRel(25, 0, duration=0.25)

    # 0
    pyautogui.moveRel(25, 0, duration=0.25)
    pyautogui.dragRel(0, -30, duration=0.25)


if __name__ == '__main__':
    # 绘制数字520
    func()
