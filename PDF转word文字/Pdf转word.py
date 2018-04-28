# _*_ coding:utf-8 _*_
# Author:liu
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator

'''
    pdf->word
    整体思路：构造文档对象，解析文档对象，提取所需内容
'''


def main():
	    # 打开本地pdf文件
    file = open('./文档.pdf', 'rb')

    # 创建一个pdf文档分析器
    parser = PDFParser(file)

    # 创建一个pdf文档
    doc = PDFDocument()

    # 链接分析器和文档对象
    parser.set_document(doc)
    doc.set_parser(parser)

    # 初始化
    doc.initialize('')

    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise Exception
    else:
        # 创建PDF资源管理器
        resource = PDFResourceManager()

        # 创建一个PDF参数分析器
        laparams = LAParams()

        # 创建聚合器，用于读取文档的对象
        device = PDFPageAggregator(resource, laparams=laparams)

        # 创建解释器，对文档编码，解释成Python能够识别的格式
        interpreter = PDFPageInterpreter(resource, device)
        # 循环遍历列表，每次处理一页的内容
        # doc.get_pages() 获取page列表
        for page in doc.get_pages():
            # 利用解释器的process_page()方法解析读取单独页数
            interpreter.process_page(page)
            # 使用聚合器get_result() 方法获取内容
            layout = device.get_result()
            # 这里layout是一个LTPage对象
            for out in layout:
                # 判断是否含有get_text()方法，获取文字
                if hasattr(out, "get_text"):
                    print(out.get_text())
                    # 保存到文件中
                    with open('./test.txt', 'a') as f:
                        f.write(out.get_text() + '\n')

if __name__ == '__main__':
    main()
