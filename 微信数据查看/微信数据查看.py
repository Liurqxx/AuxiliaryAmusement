# _*_coding:utf-8_*_
# Author:liu

import itchat
from itchat.content import TEXT
from itchat.content import *
from wxpy import Bot
import time
import re
import os

msg_information = {}
face_bug = None  # 针对表情包的内容


@itchat.msg_register([TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO], isFriendChat=True,
                     isMpChat=True)
def handle_receive_msg(msg):
    global face_bug
    msg_time_rec = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 接受消息的时间
    msg_from = itchat.search_friends(userName=msg['FromUserName'])['NickName']  # 在好友列表中查询发送信息的好友昵称


    face_bug = msg_content

    # 将信息存储在字典中，每一个msg_id对应一条信息
    msg_information.update(
        {
            msg_id: {
                "msg_from": msg_from, "msg_time": msg_time, "msg_time_rec": msg_time_rec,
                "msg_type": msg["Type"],
                "msg_content": msg_content, "msg_share_url": msg_share_url
            }
        }
    )


# 这个是用于监听是否有friend消息撤回
@itchat.msg_register(NOTE, isFrien
            msg_content = r"纬度->" + x.__str__() + " 经度->" + y.__str__()  # 内容为详细的地址
        else:
   old_msg["msg_type"] == "Recording" \
                    or old_msg["msg_type"] == "Video" \
                    or old_msg["msg_type"] == "Attachment":
                file = '@fil@%s' % (old_msg['msg_content'])
                itchat.send(msg=file, toUserName='filehelper')
                os.remove(old_msg['msg_content'])
            # 删除字典旧消息
            msg_information.pop(old_msg_id)


if __name__ == '__main__':
    # Main
    # itchat.auto_login(enableCmdQR=True, hotReload=True)
    #登录微信
    itchat.auto_login()
    itchat.run()
