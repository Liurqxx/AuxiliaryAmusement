# _*_coding:utf-8_*_
# Author:liu
import requests
import json
import hashlib

'''
请求参数：

q=apple

from=en

to=zh

appid=2015063000000001

salt=1435660288

平台分配的密钥: 12345678

生成sign：

>拼接字符串1

拼接appid=2015063000000001+q=apple+salt=1435660288+密钥=12345678

得到字符串1 =2015063000000001apple143566028812345678

>计算签名sign（对字符串1做md5加密，注意计算md5之前，串1必须为UTF-8编码）

sign=md5(2015063000000001apple143566028812345678)

sign=f89f9594663708c1605f3d736d01d2d4

完整请求为：

http://api.fanyi.baidu.com/api/trans/vip/translate?
q=apple&from=en&to=zh&appid=2015063000000001&salt=1435660288&sign=f89f9594663708c1605f3d736d01d2d4

'''


def main():
    select_num = int(input("请输入功能选项(1:英->中 2:中->英)："))
    if select_num == 1:
        # 英文转中文
        from_info = 'en'
        to_info = 'zh'
    elif select_num == 2:
        # 中文转英文
        from_info = 'zh'
        to_info = 'en'
    # 要翻译的内容
    info = input("请输入要翻译的内容:")

    url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    # 拼接appid=2015063000000001+q=apple+salt=1435660288+密钥=12345678
    str1 = 'appid' + info + '1435660288秘钥'
    # md5加密
    sign = hashlib.md5(str1.encode()).hexdigest()
    # json数据封装
    json_info = {
        'q': info,
        'from': from_info,
        'to': to_info,
        'appid': '20180409000144259',
        'salt': '1435660288',
        'sign': sign

    }
    # 得到json数据
    result = requests.post(url, data=json_info).content
    # 得到结果
    result = json.loads(result.decode())['trans_result']

    # {'from': 'en', 'trans_result': [{'src': 'apple', 'dst': '苹果'}], 'to': 'zh'}
    # 提取数据
    result = result[0]['dst']
    print('翻译结果：', result)


if __name__ == '__main__':
    main()
