# _*_coding:utf-8_*_
# Author:liu
import re
from wxpy import *
from pyecharts import Pie
from pyecharts import Map
from pyecharts import WordCloud

'''
    分析微信好友的数据
'''
# 用于登录微信
bot = Bot()


# 男女比例展示
def show_male(dict_data):
    '''水球图展示男女比例'''
    sex_key_list = []
    sex_value_list = []
    # 提取数据
    for sex_key, sex_value in dict_data.items():
        sex_key_list.append(sex_key)
        sex_value_list.append(sex_value)

    # 创建饼图 title_pos:标题位置
    pie = Pie('男女比例', width=1400)

    # 添加数据 is_random:是否随机排列颜色，默认false
    pie.add("", sex_key_list, sex_value_list, is_label_show=True)
    pie.render('./img/男女比例.html')


# 统计好友男女比例
def tongji_sex(friend_list):
    '''饼图分析男女比例'''
    # 定义一个字典统计男女数量
    sex_dict = {'男': 0, '女': 0}

    for friend in friend_list:
        # 统计性别
        if friend.sex == 1:
            sex_dict['男'] += 1
        elif friend.sex == 2:
            sex_dict['女'] += 1
    # 数据展示
    show_male(sex_dict)


# 柱状图显示地区分布
def show_area(dict_data):
    area_key_list = []
    area_value_list = []
    # 数据分类统计
    for area_key, area_value in dict_data.items():
        area_key_list.append(area_key)
        area_value_list.append(area_value)
    # 地图显示分布
    map = Map("地区分布", width=1100, height=600)
    # 添加数据
    map.add("", area_key_list, area_value_list, maptype='china', is_visualmap=True,
            visual_text_color='#000')
    # 保存地图
    map.render('./img/地区分布.html')


# 统计地区分布
def tongji_area(friends):
    # 使用一个字典统计各省好友数量
    # province_dict = {'北京': 0, '上海': 0, '天津': 0, '重庆': 0,
    #                  '河北': 0, '山西': 0, '吉林': 0, '辽宁': 0, '黑龙江': 0,
    #                  '陕西': 0, '甘肃': 0, '青海': 0, '山东': 0, '福建': 0,
    #                  '浙江': 0, '台湾': 0, '河南': 0, '湖北': 0, '湖南': 0,
    #                  '江西': 0, '江苏': 0, '安徽': 0, '广东': 0, '海南': 0,
    #                  '四川': 0, '贵州': 0, '云南': 0, '内蒙古': 0, '新疆': 0,
    #                  '宁夏': 0, '广西': 0, '西藏': 0, '香港': 0, '澳门': 0}
    # 地区
    province_dict = {}

    # data3[item['area'].split(' ')[0]] = data3.get(item['area'].split(' ')[0], 0) + 1

    # 统计省份
    for friend in friends:
        # if friend.province in province_dict.keys():
        #     province_dict[friend.province] += 1
        if friend.province != "" and not (friend.province[0] < "a" and friend.province[0] < "z"):
            province_dict[friend.province] = province_dict.get(friend.province, 0) + 1

    # {'山西': 7, '上海': 0, '台湾': 0, '青海': 0,...}
    # 柱状图展示地区分布
    show_area(province_dict)


# 统计签名
def tongji_qianming(friends):
    '''统计签名'''

    # 保存签名列表
    qianming_list = []
    friend_name_list = []

    # 统计签名
    for friend in friends:
        # 对数据进行清洗，将标点符号等对词频统计造成影响的因素剔除
        # pattern = re.compile(r'[一-龥]+')
        # filterdata = re.findall(pattern, friend.signature)
        # print(filterdata)
        # print(friend.signature)
        # 对签名数据进行匹配筛选
        pattern = re.sub('</?.*?>', "", friend.signature)
        # print(pattern)

        if pattern != "":
            # 把签名添加到列表内
            qianming_list.append(pattern)

            friend_name_list.append(friend.name)
    # 个签显示
    show_cloud(qianming_list, friend_name_list)


# 词云图显示签名
def show_cloud(qianming_list, friend_name_list):
    '''词云图'''
    wordcloud = WordCloud(width=1600, height=1000)
    wordcloud.add("", qianming_list, friend_name_list, word_size_range=[20, 100])
    wordcloud.render('./img/个签.html')


def main():
    # 好友列表
    my_friends_list = bot.friends()

    # 组列表
    # my_group_list = bot.groups()

    tongji_sex(my_friends_list)
    tongji_area(my_friends_list)

    tongji_qianming(my_friends_list)


if __name__ == '__main__':
    main()
