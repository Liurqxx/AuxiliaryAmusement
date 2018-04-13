# _*_coding:utf-8_*_
# Author:liu
import re
import requests
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


# 获取字体
def getFont(name):
    font_list_name = {
        '个性签': 'jfcs.ttf',
        '连笔签': 'qmt.ttf',
        '潇洒签': 'bzcs.ttf',
        '草体签': 'lfc.ttf',
        '合文签': 'haku.ttf',
        '商务签': 'zql.ttf',
        '可爱签': 'yqk.ttf',
    }
    return font_list_name[name]