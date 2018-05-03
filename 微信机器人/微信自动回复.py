# _*_ coding:utf-8 _*_
# Author:liu
from wxpy import Bot
from wxpy import Tuling
from wxpy import embed
from wxpy import ensure_one
from threading import Thread
import time

'''
    使用图灵机器人自动回复消息：
        注册地址：http://www.tuling123.com/
'''
'''
抓住轻松的美妙，揪住快乐的美好，揽住温馨的嬉闹，高举甜蜜的欢笑；
甩掉烦恼的骚扰，驱赶失意的苦恼，践踏压力的跟跑，避开困苦的盘绕。
五一劳动节将到，扑入大自然的怀抱，愿你五一劳动节，拥有轻爽不少，常伴欢乐不消！
'''

# 实例化，并登录微信,cache_path=True：缓存，并不需要每次都登录微信
bot = Bot(cache_path=True)

# 查找到要使用机器人来聊天的好友
# my_friend = ensure_one(bot.search(u'****'))

# friend_name_list = []
# # 获取好友
friends = bot.friends()
#
# for friend in friends:
#     friend_name_list.append(friend.name)

# 调用图灵机器人API   获取地址：http://www.tuling123.com/
tuling = Tuling(api_key='×××××××××××××××××××××××××××')


def handle_info(friend):
    # 使用图灵机器人自动与所有好友聊天
    # @bot.register([my_friend, Group], TEXT)
    # @bot.register([friend], msg_types=['TEXT', 'RECORDING', 'PICTURE'])
    @bot.register(friend)
    def reply_my_friend(msg):
    
        tuling.do_reply(msg)

    bot.join()


# 发送消息
# for fr in friends:
#     if not fr.name == '夏沫烟雨':
#         fr.send('''
#     抓住轻松的美妙，揪住快乐的美好，揽住温馨的嬉闹，高举甜蜜的欢笑；
#     甩掉烦恼的骚扰，驱赶失意的苦恼，践踏压力的跟跑，避开困苦的盘绕。
#     五一劳动节将到，扑入大自然的怀抱，愿你五一劳动节，拥有轻爽不少，常伴欢乐不消！    --来自小强的得力助手
#     ''')
# my_friend.send('''抓住轻松的美妙，揪住快乐的美好，揽住温馨的嬉闹，高举甜蜜的欢笑；
# 甩掉烦恼的骚扰，驱赶失意的苦恼，践踏压力的跟跑，避开困苦的盘绕。
# 五一劳动节将到，扑入大自然的怀抱，愿你五一劳动节，拥有轻爽不少，常伴欢乐不消！''')

for f in friends:
    t1 = Thread(target=handle_info, args=(f,))
    print('线程开始...')
    t1.start()

# t1.join()

# 进入Python命令行，让程序保持运行
embed()
