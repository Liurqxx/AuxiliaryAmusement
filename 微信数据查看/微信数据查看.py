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
# 针对表情包的内容
face_bug = None


@itchat.msg_register([TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO], isFriendChat=True,
                     isMpChat=True)
def handle_receive_msg(msg):
    global msg_information
    global face_bug
    # 接受消息的时间
    msg_time_rec = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # 在好友列表中查询发送信息的好友昵称
    msg_from = itchat.search_friends(userName=msg['FromUserName'])['NickName']
    # 信息发送的时间
    msg_time = msg['CreateTime']
    # 每条信息的id
    msg_id = msg['MsgId']
    # 储存信息的内容
    msg_content = None
    # 储存分享的链接，比如分享的文章和音乐
    msg_share_url = None
    # 如果发送的消息是文本或者好友推荐
    if msg['Type'] == 'Text' or msg['Type'] == 'Friends':
        msg_content = msg['Text']
        # print(msg_content)

    # 如果发送的消息是附件、视屏、图片、语音
    elif msg['Type'] == "Attachment" or msg['Type'] == "Video" \
            or msg['Type'] == 'Picture' \
            or msg['Type'] == 'Recording':
        # 内容就是他们的文件名
        msg_content = msg['FileName']
        # 下载文件
        msg['Text'](str(msg_content))
        # print msg_content
    # 如果消息是推荐的名片
    elif msg['Type'] == 'Card':
        # 内容就是推荐人的昵称和性别
        msg_content = msg['RecommendInfo']['NickName'] + '的名片'
        if msg['RecommendInfo']['Sex'] == 1:
            msg_content += '性别为男'
        else:
            msg_content += '性别为女'

        print(msg_content)
    # 如果消息为分享的位置信息
    # elif msg['Type'] == 'Map':
    #     x, y, location = re.search(
    #         "<location x=\"(.*?)\" y=\"(.*?)\".*label=\"(.*?)\".*", msg['OriContent']).group(1, 2, 3)
    #     if location is None:
    #         msg_content = r"纬度->" + x.__str__() + " 经度->" + y.__str__()  # 内容为详细的地址
    #     else:
    #         msg_content = r"" + location
    elif msg['Type'] == 'Sharing':  # 如果消息为分享的音乐或者文章，详细的内容为文章的标题或者是分享的名字
        msg_content = msg['Text']
        msg_share_url = msg['Url']  # 记录分享的url
        print(msg_share_url)

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
    print('msg_infomationg===', msg_information)


# 这个是用于监听是否有friend消息撤回
@itchat.msg_register(NOTE, isFriendChat=True, isGroupChat=True, isMpChat=True)
def information(msg):
    # 这里如果这里的msg['Content']中包含消息撤回和id，就执行下面的语句
    if '撤回了一条消息' in msg['Content']:
        print(msg['MsgId'])
        # 测试中（问题未处理）
        # old_msg_id = re.search(r'&lt;msgid&gt;(.*?)&lt;/msgid&gt;', msg['Content']).group(1)  # 在返回的content查找撤回的消息的id
        old_msg_id = msg['MsgId']
        old_msg = msg_information.get(old_msg_id)  # 得到消息
        print(old_msg)

        if len(old_msg_id) < 11:  # 如果发送的是表情包
            itchat.send_file(face_bug, toUserName='filehelper')
        else:  # 发送撤回的提示给文件助手
            msg_body = "[" \
                       + old_msg.get['msg_from'] + " 撤回了 ]\n" \
                       + old_msg.get["msg_type"] + " 消息：" + "\n" \
                       + old_msg.get['msg_time_rec'] + "\n" + str(old_msg['msg_content'])
            # 如果是分享的文件被撤回了，那么就将分享的url加在msg_body中发送给文件助手
            if old_msg['msg_type'] == "Sharing":
                msg_body += "\n就是这个链接➣ " + old_msg.get('msg_share_url')

            # 将撤回消息发送到文件助手
            itchat.send_msg(msg_body, toUserName='filehelper')
            # 有文件的话也要将文件发送回去
            if old_msg["msg_type"] == "Picture" \
                    or old_msg["msg_type"] == "Recording" \
                    or old_msg["msg_type"] == "Video" \
                    or old_msg["msg_type"] == "Attachment":
                file = '@fil@%s' % (old_msg['msg_content'])
                itchat.send(msg=file, toUserName='filehelper')
                os.remove(old_msg['msg_content'])
            # 删除字典旧消息
            msg_information.pop(old_msg_id)


@itchat.msg_register([TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def handle_receive_msg(msg):
    global face_bug
    global msg_information
    msg_time_rec = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 接受消息的时间
    # groupid = msg['FromUserName']
    # chatroom = itchat.search_chatrooms(userName=groupid)
    msg_Actual_from = msg['ActualNickName']
    # msg_Actual_from = msg['User']
    # msg_from = msg_Actual_from['Self']['NickName']
    msg_from = msg_Actual_from
    msg_time = msg['CreateTime']  # 信息发送的时间
    msg_id = msg['MsgId']  # 每条信息的id
    msg_content = None  # 储存信息的内容
    msg_share_url = None  # 储存分享的链接，比如分享的文章和音乐
    print(msg['Type'])

    if msg['Type'] == 'Text' or msg['Type'] == 'Friends':  # 如果发送的消息是文本或者好友推荐
        msg_content = msg['Text']
        print(msg_content)

    # 如果发送的消息是附件、视屏、图片、语音
    elif msg['Type'] == "Attachment" or msg['Type'] == "Video" \
            or msg['Type'] == 'Picture' \
            or msg['Type'] == 'Recording':
        msg_content = msg['FileName']  # 内容就是他们的文件名
        msg['Text'](str(msg_content))  # 下载文件
        # print msg_content
    elif msg['Type'] == 'Card':  # 如果消息是推荐的名片
        msg_content = msg['RecommendInfo']['NickName'] + '的名片'  # 内容就是推荐人的昵称和性别
        if msg['RecommendInfo']['Sex'] == 1:
            msg_content += '性别为男'
        else:
            msg_content += '性别为女'

        print(msg_content)

    elif msg['Type'] == 'Map':  # 如果消息为分享的位置信息
        x, y, location = re.search(
            "<location x=\"(.*?)\" y=\"(.*?)\".*label=\"(.*?)\".*", msg['OriContent']).group(1, 2, 3)
        if location is None:
            msg_content = r"纬度->" + x.__str__() + " 经度->" + y.__str__()  # 内容为详细的地址
        else:
            msg_content = r"" + location
    elif msg['Type'] == 'Sharing':  # 如果消息为分享的音乐或者文章，详细的内容为文章的标题或者是分享的名字
        msg_content = msg['Text']
        msg_share_url = msg['Url']  # 记录分享的url
        print(msg_share_url)

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


# 这个是用于监听是否有Group消息撤回
@itchat.msg_register(NOTE, isGroupChat=True, isMpChat=True)
def information(msg):
    global msg_information
    # 这里如果这里的msg['Content']中包含消息撤回和id，就执行下面的语句
    if '撤回了一条消息' in msg['Content']:
        # 测试
        # print('1=msg===', msg)
        # &lt;sysmsg type="revokemsg"&gt;&lt;revokemsg&gt;&lt;session&gt;9056974594@chatroom&lt;/session&gt;&lt;oldmsgid&gt;1094812759&lt;/oldmsgid&gt;&lt;msgid&gt;6448073312596945382&lt;/msgid&gt;&lt;replacemsg&gt;&lt;![CDATA[你撤回了一条消息]]&gt;&lt;/replacemsg&gt;&lt;/revokemsg&gt;&lt;/sysmsg&gt;
        # print('2==msg[\'Content\']', msg['Content'])

        '''
    {
    'StatusNotifyCode': 0,
    'CreateTime': 1524744941,
    'ImgStatus': 1,
    'PlayLength': 0,
    'ToUserName': '@3b5c21df143a83691096f09375deb672a481eed5f750723868f11659ecee6418',
    'OriContent': '',
    'StatusNotifyUserName': '',
    'MsgId': '2487016030372881170',
    'isAt': False,
    'HasProductId': 0,
    'Ticket': '',
    'Type': 'Note',
    'ActualNickName': '夏沫烟雨',
    'ForwardFlag': 0,
    'Text': '你撤回了一条消息',
    'FileName': '',
    'FromUserName': '@@acc08417accc5bbbdf83b8b953affa3f6d08ef0965e20d99fa3adc0435d2335b',
    'RecommendInfo': {
        'VerifyFlag': 0,
        'Alias': '',
        'Content': '',
        'UserName': '',
        'NickName': '',
        'Sex': 0,
        'Ticket': '',
        'QQNum': 0,
        'Province': '',
        'City': '',
        'Scene': 0,
        'AttrStatus': 0,
        'Signature': '',
        'OpCode': 0
    },
    'SubMsgType': 0,
    'ImgHeight': 0,
    'FileSize': '',
    'AppInfo': {
        'AppID': '',
        'Type': 0
    },
    'Content': '&lt;sysmsgtype="revokemsg"&gt;&lt;revokemsg&gt;&lt;session&gt;9056974594@chatroom&lt;/session&gt;&lt;oldmsgid&gt;1094812744&lt;/oldmsgid&gt;&lt;msgid&gt;8355431330327922915&lt;/msgid&gt;&lt;replacemsg&gt;&lt;![
        CDATA[
            你撤回了一条消息
        ]
    ]&gt;&lt;/replacemsg&gt;&lt;/revokemsg&gt;&lt;/sysmsg&gt;',
    'ImgWidth': 0,
    'EncryFileName': '',
    'NewMsgId': 2487016030372881170,
    'AppMsgType': 0,
    'Status': 4,
    'ActualUserName': '@3b5c21df143a83691096f09375deb672a481eed5f750723868f11659ecee6418',
    'VoiceLength': 0,
    'MediaId': '',
    'Url': '',
    'MsgType': 10002
}


        '''
        old_msg_id = re.search(r'&lt;msgid&gt;(.*?)&lt;/msgid&gt;', msg['Content']).group(1)  # 在返回的content查找撤回的消息的id
        # print("old_msg_id==", old_msg_id)

        old_msg = msg_information.get(old_msg_id)  # 得到消息
        print(old_msg)

        if len(old_msg_id) < 11:  # 如果发送的是表情包
            itchat.send_file(face_bug, toUserName='filehelper')
        else:  # 发送撤回的提示给文件助手
            msg_body = "【" \
                       + old_msg.get('msg_from') + " 群消息撤回提醒】\n" \
                       + " 撤回了 " + old_msg.get("msg_type") + " 消息：" + "\n" \
                       + old_msg.get('msg_time_rec') + "\n" \
                       + r"" + old_msg.get('msg_content')
            # 如果是分享的文件被撤回了，那么就将分享的url加在msg_body中发送给文件助手
            if old_msg['msg_type'] == "Sharing":
                msg_body += "\n就是这个链接➣ " + old_msg.get('msg_share_url')

            # 将撤回消息发送到文件助手
            itchat.send_msg(msg_body, toUserName='filehelper')
            # 有文件的话也要将文件发送回去
            if old_msg["msg_type"] == "Picture" \
                    or old_msg["msg_type"] == "Recording" \
                    or old_msg["msg_type"] == "Video" \
                    or old_msg["msg_type"] == "Attachment":
                file = '@fil@%s' % (old_msg['msg_content'])
                itchat.send(msg=file, toUserName='filehelper')
                os.remove(old_msg['msg_content'])
            # 删除字典旧消息
            msg_information.pop(old_msg_id)


if __name__ == '__main__':
    # itchat.auto_login(enableCmdQR=True, hotReload=True)
    itchat.auto_login()
    itchat.run()
