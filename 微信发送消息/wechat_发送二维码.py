# _*_ coding:utf-8 _*_
# Author:liu
from wxpy import *
import requests
import qrcode
import io


# 好友列表
# friends_list = bot.friends()

# 组列表
# group_list = bot.groups()


def get_news():
    '''获取金山词霸每日一句'''
    url = "http://open.iciba.com/dsapi/"
    html = requests.get(url)
    # 得到每日一句英文
    contents = html.json()['content']
    # 得到每日一句中文
    translation = html.json()['translation']
    return contents, translation


# 生成二维码
def get_code_by_str(text):
    # 判断用户输入的类型
    if not isinstance(text, str):
        print('请输入字符串参数')
        return None
    # 设置图案样式
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # 设置二维码数据
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image()
    img_data = io.BytesIO()
    img.save(img_data)
    return img_data.getvalue()


def main():
    '''给指定好友发送指定信息的二维码'''
    # 用于登录微信
    bot = Bot()

    try:
        while True:
            # 好友列表
            friends_list = bot.friends()
            print(friends_list)
            # info = input("请输入二维码信息：")
            # 得到词霸每日一句的中英文
            info_en, info_ch = get_news()
            info_ch = info_ch[5:]
            send_to = input("请输入对方的昵称：")
            # 要发送的朋友的微信名称（不是备注也不是账号）
            my_friend = bot.friends().search(u'{}'.format(send_to))[0]

            # 发送数据
            # my_friend.send(get_news()[0])
            # my_friend.send(get_news()[1][5:])
            # my_friend.send(get_code_by_str(info))
            # 发送图片
            with open('img.png', 'wb') as file:
                file.write(get_code_by_str(info_ch))
            my_friend.send_image('img.png')
            # my_friend.send(u'来自爸爸的心灵鸡汤！')

            # 定时发送，每86400秒(一天)发送一次
            # t = Timer(86400, main)
            # t.start()
    except Exception as e:
        print(e)
        print('发送失败')


if __name__ == '__main__':
    main()
