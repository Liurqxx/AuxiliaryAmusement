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

if __name__ == '__main__':
    main()
