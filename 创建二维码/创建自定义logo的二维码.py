from PIL import Image
import qrcode

# 初步生成二维码图像
qr = qrcode.QRCode(version=5,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=8,border=4)
qr.add_data("https://github.com/lrq154439")
qr.make(fit=True)

# 获得Image实例并把颜色模式转换为RGBA
img = qr.make_image()
img = img.convert("RGBA")

# 打开logo文件
icon = Image.open("./logo.jpeg")

# 计算logo的尺寸
img_w,img_h = img.size
factor = 3
size_w = int(img_w / factor)
size_h = int(img_h / factor)

# 比较并重新设置logo文件的尺寸
icon_w,icon_h = icon.size
if icon_w >size_w:
    icon_w = size_w
if icon_h > size_h:
    icon_h = size_h
icon = icon.resize((icon_w,icon_h),Image.ANTIALIAS)

# 计算logo的位置，并复制到二维码图像中
w = int((img_w - icon_w)/2)
h = int((img_h - icon_h)/2)
icon = icon.convert("RGBA")
img.paste(icon,(w,h),icon)

# 保存二维码
img.save('./自定义logo二维码.png')
