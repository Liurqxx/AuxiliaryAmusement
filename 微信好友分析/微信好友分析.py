# _*_coding:utf-8_*_
# Author:liu
from wxpy import *
import requests
import qrcode
import io

# 用于登录微信
bot = Bot()


# 统计好友男女比例
def tongji(friend_list):
    '''男女比例'''
    # 定义一个字典统计男女数量
    sex_dict = {'male': 0, 'female': 0}

    for friend in friend_list:
        # 统计性别
        if friend.sex == 1:
            sex_dict['male'] += 1
        elif friend.sex == 2:
            sex_dict['female'] += 1


def show_area_distribution(friends):
    # 使用一个字典统计各省好友数量
    province_dict = {'北京': 0, '上海': 0, '天津': 0, '重庆': 0,
                     '河北': 0, '山西': 0, '吉林': 0, '辽宁': 0, '黑龙江': 0,
                     '陕西': 0, '甘肃': 0, '青海': 0, '山东': 0, '福建': 0,
                     '浙江': 0, '台湾': 0, '河南': 0, '湖北': 0, '湖南': 0,
                     '江西': 0, '江苏': 0, '安徽': 0, '广东': 0, '海南': 0,
                     '四川': 0, '贵州': 0, '云南': 0,
                     '内蒙古': 0, '新疆': 0, '宁夏': 0, '广西': 0, '西藏': 0,
                     '香港': 0, '澳门': 0}

    # 统计省份
    for friend in friends:
        if friend.province in province_dict.keys():
            province_dict[friend.province] += 1
    # {'山西': 7, '上海': 0, '台湾': 0, '青海': 0,...}

    print(province_dict)


def main():
    # 好友列表
    my_friends_list = bot.friends()

    # 组列表
    # my_group_list = bot.groups()

    # print(my_friends_list)
    tongji(my_friends_list)
    show_area_distribution(my_friends_list)


if __name__ == '__main__':
    main()
