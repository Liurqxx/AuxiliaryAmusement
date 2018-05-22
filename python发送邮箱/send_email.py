# _*_ coding:utf-8 _*_
# Author:liu
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart









sg['Subject'] = input(u'请输入邮件主题：')
# 发送方信息
msg['From'] = sender
# 邮件正文是MIMEText:
msg_content = input(u'请输入邮件主内容:')
msg.attach(MIMEText(msg_content, 'plain', 'utf-8'))
# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open(u'./img.png', 'rb') as f:
    # 设置
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.set_debuglevel(1)
    s.login(sender, passWord)
    # 给receivers列表中的联系人逐个发送邮件
    for item in receivers:
        msg['To'] = to = item
        s.sendmail(sender, to, msg.as_string())
        print('Success!')
    s.quit()
    print("All emails have been sent over!")
except smtplib.SMTPException as e:
    print("Falied,%s", e)
