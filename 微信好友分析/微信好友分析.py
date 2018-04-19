# _*_coding:utf-8_*_
# Author:liu
from wxpy import *
from pyecharts import Pie
from pyecharts import Bar

# 用于登录微信
bot = Bot()
# 男女比例展示
def show_male(dict_data):
    '''饼图展示男女比例'''
    sex_key_list = []
    sex_value_list = []
    # 提取数据
    for sex_key, sex_value in dict_data.items():
        sex_key_list.append(sex_key)
        sex_value_list.append(sex_value)

    # 创建饼图 title_pos:标题位置
    pie = Pie('男女比例', width=900)

    # 添加数据 is_random:是否随机排列颜色，默认false
    pie.add("", sex_key_list, sex_value_list, is_label_show=True)
    pie.render('./img/男女比例.html')

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

    # 数据展示
    # 制成图表(柱状图)
    bar = Bar('地区分布')
    # mark_line:显示最大值和最小值  mark_point:显示平均值
    bar.add('', area_key_list, area_value_list, is_stack=True, mark_line=['min', 'max'], mark_point=['average'])
    # 保存html文件
    bar.render(path='./img/地区分布.html')

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
