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
    # 设置附件的MIME和文件名，这里是jpg类型,可以换png或其他类型:
    mime = MIMEBase('image', 'jpg', filename='Lyon.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='Lyon.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

# 登录并发送邮件
try:
    # QQsmtp服务器的端口号为4


   mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

# 登录并发送邮件
try:
    # QQsmtp服务器的端口号为465或587
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
