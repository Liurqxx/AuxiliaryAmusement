# _*_coding:utf-8_*_
# Author:liu


def ditushili():
    # 数据
    data = [
        ("海门", 9), ("鄂尔多斯", 12), ("招远", 12), ("舟山", 12),
        ("齐齐哈尔", 14), ("盐城", 15), ("赤峰", 16), ("青岛", 18),
        ("乳山", 18), ("金昌", 19), ("泉州", 21), ("莱西", 21),
        ("日照", 21), ("胶南", 22), ("南通", 23), ("拉萨", 24),
        ("云浮", 24), ("梅州", 25), ("文登", 25), ("上海", 25),
        ("攀枝花", 25), ("威海", 25), ("承德", 25), ("厦门", 26),
        ("汕尾", 26), ("潮州", 26), ("丹东", 27), ("太仓", 27),
        ("曲靖", 27), ("烟台", 28), ("福州", 29), ("瓦房店", 30),
        ("即墨", 30), ("抚顺", 31), ("玉溪", 31), ("张家口", 31),
        ("阳泉", 31), ("莱州", 32), ("湖州", 32), ("汕头", 32),
        ("昆山", 33), ("宁波", 33), ("湛江", 33), ("揭阳", 34),
        ("荣成", 34), ("连云港", 35), ("葫芦岛", 35), ("常熟", 36),
        ("东莞", 36), ("河源", 36), ("淮安", 36), ("泰州", 36),
        ("南宁", 37), ("营口", 37), ("惠州", 37), ("江阴", 37),
        ("蓬莱", 37), ("韶关", 38), ("嘉峪关", 38), ("广州", 38),
        ("延安", 38), ("太原", 39), ("清远", 39), ("中山", 39),
        ("昆明", 39), ("寿光", 40), ("盘锦", 40), ("长治", 41),
        ("深圳", 41), ("珠海", 42), ("宿迁", 43), ("咸阳", 43),
        ("铜川", 44), ("平度", 44), ("佛山", 44), ("海口", 44),
        ("江门", 45), ("章丘", 45), ("肇庆", 46), ("大连", 47),
        ("临汾", 47), ("吴江", 47), ("石嘴山", 49), ("沈阳", 50),
        ("苏州", 50), ("茂名", 50), ("嘉兴", 51), ("长春", 51),
        ("胶州", 52), ("银川", 52), ("张家港", 52), ("三门峡", 53),
        ("锦州", 54), ("南昌", 54), ("柳州", 54), ("三亚", 54),
        ("自贡", 56), ("吉林", 56), ("阳江", 57), ("泸州", 57),
        ("西宁", 57), ("宜宾", 58), ("呼和浩特", 58), ("成都", 58),
        ("大同", 58), ("镇江", 59), ("桂林", 59), ("张家界", 59),
        ("宜兴", 59), ("北海", 60), ("西安", 61), ("金坛", 62),
        ("东营", 62), ("牡丹江", 63), ("遵义", 63), ("绍兴", 63),
        ("扬州", 64), ("常州", 64), ("潍坊", 65), ("重庆", 66),
        ("台州", 67), ("南京", 67), ("滨州", 70), ("贵阳", 71),
        ("无锡", 71), ("本溪", 71), ("克拉玛依", 72), ("渭南", 72),
        ("马鞍山", 72), ("宝鸡", 72), ("焦作", 75), ("句容", 75),
        ("北京", 79), ("徐州", 79), ("衡水", 80), ("包头", 80),
        ("绵阳", 80), ("乌鲁木齐", 84), ("枣庄", 84), ("杭州", 84),
        ("淄博", 85), ("鞍山", 86), ("溧阳", 86), ("库尔勒", 86),
        ("安阳", 90), ("开封", 90), ("济南", 92), ("德阳", 93),
        ("温州", 95), ("九江", 96), ("邯郸", 98), ("临安", 99),
        ("兰州", 99), ("沧州", 100), ("临沂", 103), ("南充", 104),
        ("天津", 105), ("富阳", 106), ("泰安", 112), ("诸暨", 112),
        ("郑州", 113), ("哈尔滨", 114), ("聊城", 116), ("芜湖", 117),
        ("唐山", 119), ("平顶山", 119), ("邢台", 119), ("德州", 120),
        ("济宁", 120), ("荆州", 127), ("宜昌", 130), ("义乌", 132),
        ("丽水", 133), ("洛阳", 134), ("秦皇岛", 136), ("株洲", 143),
        ("石家庄", 147), ("莱芜", 148), ("常德", 152), ("保定", 153),
        ("湘潭", 154), ("金华", 157), ("岳阳", 169), ("长沙", 175),
        ("衢州", 177), ("廊坊", 193), ("菏泽", 194), ("合肥", 229),
        ("武汉", 273), ("大庆", 279)
    ]

    geo = Geo("全国主要城市空气质量", "data from pm2.5", width=1200, height=600, )
    attr, value = geo.cast(data)
    geo.add("", attr, value, visual_range=[0, 200],
            visual_text_color="#fff", is_legend_show=False,
            symbol_size=15, is_visualmap=True,
            tooltip_formatter='{b}',
            label_emphasis_textsize=15,
            label_emphasis_pos='right')
    geo.render('info/地图实例1.html')


def dilizuobiaoxi():
    # 地理坐标系
    data = [
        (u"山东", 9), (u"鄂尔多斯", 12), (u"招远", 12), (u"舟山", 12), (u"齐齐哈尔", 14), (u"盐城", 15),
        (u"赤峰", 16), (u"青岛", 18), (u"乳山", 18), (u"金昌", 19), (u"泉州", 21), (u"莱西", 21),
        (u"日照", 21), (u"胶南", 22), (u"南通", 23), (u"拉萨", 24), (u"云浮", 24), (u"梅州", 25)]
    geo = Geo(u"全国主要城市空气质量", "data from pm2.5",
              title_color="#fff", title_pos="center",
              width=1200, height=600, background_color='#404a59')
    attr, value = geo.cast(data)
    print(attr)
    print(value)
    geo.add("", attr, value, visual_range=[0, 200],
            visual_text_color="#fff", symbol_size=15, is_visualmap=True)

    geo.render('./info/地理坐标系.html')


def dilizuobiaoxi2():
	'''地图坐标系地图'''
    data = [("海门", 9), ("鄂尔多斯", 12), ("招远", 12), ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15)]
    geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center", width=1200, height=600,
              background_color='#C2C2C2')
    attr, value = geo.cast(data)
    geo.add("", attr, value, type="effectScatter", is_random=True, effect_scale=5)

    geo.render('./info/地理坐标系2.html')


def guanxitu():
    '''显示微博转发关系图'''
    with open("./jsonweibo.json", "r", encoding="utf-8") as f:
        j = json.load(f)
    nodes, links, categories, cont, mid, userl = j
    graph = Graph("微博转发关系图", width=1200, height=600)
    graph.add("", nodes, links, categories, label_pos="right", repulsion=50, is_legend_show=False, line_curve=0.2,
              label_text_color=None)
    # graph.show_config()
    graph.render()


def map_demo():
    '''地图实例'''

    value = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]
    attr = ["福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"]
    map = Map("Map 结合 VisualMap 示例", width=1200, height=600)
    map.add("", attr, value,
            maptype='china', is_visualmap=True, visual_text_color='# 000')
    # map.show_config()
    map.render()


def shuiqiu1():
    '''水球图'''
    liquid = Liquid("水球图示例")
    liquid.add("Liquid", [0.6])
    # liquid.show_config()
    liquid.render('./info/水球图1.html')


def shuiqiu2():
    '''水球图'''
    liquid = Liquid("水球图示例")
    liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_outline_show=False)
    liquid.render('./info/水球图2.html')


def shuiqiu3():
    '''水球图'''
    liquid = Liquid("水球图示例")
    liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_animation=False, shape='diamond')
    liquid.render('./info/水球图3.html')


def pingxingzuobao():
    '''平行坐标-自定义指示器'''
    c_schema = [{"dim": 0, "name": "data"}, {"dim": 1, "name": "AQI"}, {"dim": 2, "name": "PM2.5"},
                {"dim": 3, "name": "PM10"}, {"dim": 4, "name": "CO"}, {"dim": 5, "name": "NO2"},
                {"dim": 6, "name": "CO2"}, {"dim": 7, "name": "等级", "type": "category",
                                            "data": ['优', '良', '轻度污染', '中度污染', '重度污染', '严重污染']}]
    data = [
        [1, 91, 45, 125, 0.82, 34, 23, "良"], [2, 65, 27, 78, 0.86, 45, 29, "良"], [3, 83, 60, 84, 1.09, 73, 27, "良"],
        [4, 109, 81, 121, 1.28, 68, 51, "轻度污染"], [5, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
        [6, 109, 81, 121, 1.28, 68, 51, "轻度污染"], [7, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
        [8, 89, 65, 78, 0.86, 51, 26, "良"], [9, 53, 33, 47, 0.64, 50, 17, "良"], [10, 80, 55, 80, 1.01, 75, 24, "良"],
        [11, 117, 81, 124, 1.03, 45, 24, "轻度污染"], [12, 99, 71, 142, 1.1, 62, 42, "良"],
        [13, 95, 69, 130, 1.28, 74, 50, "良"], [14, 116, 87, 131, 1.47, 84, 40, "轻度污染"]]
    parallel = Parallel("平行坐标系-用户自定义指示器")
    parallel.config(c_schema=c_schema)
    parallel.add("parallel", data)
    parallel.render('./info/平行坐标-自定义指示器.html')


def leidatu():
    '''雷达图'''

    schema = [("销售", 6500), ("管理", 16000), ("信息技术", 30000), ("客服", 38000), ("研发", 52000), ("市场", 25000)]
    v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
    v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
    radar = Radar()
    radar.config(schema)
    radar.add("预算分配", v1, is_splitline=True, is_axisline_show=True)
    radar.add("实际开销", v2, label_color=["#4e79a7"], is_area_show=False)
    radar.render('./info/雷达图.html')


def sandiantu():
    '''散点图'''
    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [10, 20, 30, 40, 50, 60]
    scatter = Scatter("散点图示例")
    scatter.add("A", v1, v2)
    scatter.add("B", v1[::-1], v2)
    scatter.render('./info/散点图.html')


def sandiandayinziti():
    '''散点打印字体'''

    scatter = Scatter("散点图示例")
    v1, v2 = scatter.draw("./img.PNG")
    scatter.add("散点图打印文字", v1, v2, is_random=True)
    scatter.render('./info/散点图打印文字.html')


def ciyuntu():
    '''词云图'''

    name = ['SamSClub', 'Macys', 'AmySchumer', 'JurassicWorld', 'CharterCommunications', 'ChickFilA', 'PlanetFitness',
            'PitchPerfect', 'Express', 'Home', 'JohnnyDepp',
            'LenaDunham', 'LewisHamilton', 'KXAN', 'MaryEllenMark', 'FarrahAbraham', 'RitaOra', 'SerenaWilliams',
            'NCAAbaseballtournament', 'PointBreak']
    value = [10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555, 550, 462, 366, 360, 282,
             273, 265]

    wordcloud = WordCloud(width=1300, height=620)
    wordcloud.add("", name, value, word_size_range=[20, 100])
    wordcloud.render('./info/词云图.html')


def yibiaopan():
    '''仪表盘图'''

    gauge = Gauge("仪表盘示例")
    gauge.add("业务指标", "完成率", 66.66)
    gauge.render('./info/仪表盘.html')


def loudoutu():
    '''漏斗图'''

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    value = [20, 40, 60, 80, 100, 120]
    funnel = Funnel("漏斗图示例")
    funnel.add("商品", attr, value, is_label_show=True, label_pos="inside", label_text_color="#fff")
    funnel.render('./info/漏斗图.html')


def lianyitexiaosandiantu():
    '''带有涟漪特效的散点图'''

    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [25, 20, 15, 10, 60, 33]
    es = EffectScatter("动态散点图示例")
    es.add("effectScatter", v1, v2)
    es.render()
    es = EffectScatter("动态散点图各种图形示例")
    es.add("", [10], [10], symbol_size=20, effect_scale=3.5, effect_period=3, symbol="pin")
    es.add("", [20], [20], symbol_size=12, effect_scale=4.5, effect_period=4, symbol="rect")
    es.add("", [30], [30], symbol_size=30, effect_scale=5.5, effect_period=5, symbol="roundRect")
    es.add("", [40], [40], symbol_size=10, effect_scale=6.5, effect_brushtype='fill', symbol="diamond")
    es.add("",
           [50],
           [50],
           symbol_size=16,
           effect_scale=5.5,
           effect_period=3,
           symbol="arrow")
    es.add("", [60], [60], symbol_size=6, effect_scale=2.5, effect_period=3, symbol="triangle")
    es.render('./info/涟漪特效散点图.html')


def jizuobiao_duidiezhuzhuang():
    '''极坐标-堆叠柱状图'''

    radius = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    polar = Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
    polar.add("", [1, 2, 3, 4, 3, 5, 1], radius_data=radius, type='barAngle', is_stack=True)
    polar.add("", [2, 4, 6, 1, 2, 3, 1], radius_data=radius, type='barAngle', is_stack=True)
    polar.add("", [1, 2, 3, 4, 1, 2, 5], radius_data=radius, type='barAngle', is_stack=True)
    polar.render('./info/极坐标-堆叠柱状图.html')


def jizuobiao_huitu():
    '''极坐标-绘制花朵'''
    data = []
    for i in range(361):
        t = i / 180 * math.pi
        r = math.sin(2 * t) * math.cos(2 * t)
        data.append([r, i])
    polar = Polar("极坐标系示例", width=1200, height=600)
    polar.add("Flower", data, start_angle=0, symbol=None, axis_range=[0, None], area_color="#f71f24", area_opacity=0.6)
    polar.render('./info/极坐标-绘制花朵.html')


def dianyingbili():
    '''各类电影占的比例'''

    pie = Pie('各类电影所占的比例', "数据来着豆瓣", title_pos='center')

    pie.add("", ["剧情", ""], [25, 75], center=[10, 30], radius=[18, 24],
            label_pos='center', is_label_show=True, label_text_color=None, )

    pie.add("", ["奇幻", ""], [24, 76], center=[30, 30], radius=[18, 24],
            label_pos='center', is_label_show=True, label_text_color=None, legend_pos='left')

    pie.add("", ["爱情", ""], [14, 86], center=[50, 30], radius=[18, 24],
            label_pos='center', is_label_show=True, label_text_color=None)

    pie.add(
        "", ["惊悚", ""], [11, 89], center=[70, 30], radius=[18, 24],
        label_pos='center', is_label_show=True, label_text_color=None)

    pie.add("", ["冒险", ""], [27, 73],
            center=[90, 30], radius=[18, 24],
            label_pos='center', is_label_show=True, label_text_color=None)

    pie.add(
        "", ["动作", ""], [15, 85], center=[10, 70], radius=[18, 24],
        label_pos='center', is_label_show=True, label_text_color=None)

    pie.add("", ["喜剧", ""], [54, 46],
            center=[30, 70], radius=[18, 24],
            label_pos='center', is_label_show=True, label_text_color=None)

    pie.add(
        "", ["科幻", ""], [26, 74], center=[50, 70], radius=[18, 24],
        label_pos='center', is_label_show=True, label_text_color=None)

    pie.add("", ["悬疑", ""], [25, 75],
            center=[70, 70], radius=[18, 24],
            label_pos='center', is_label_show=True, label_text_color=None)

    pie.add(
        "", ["犯罪", ""], [28, 72], center=[90, 70], radius=[18, 24],
        label_pos='center', is_label_show=True, label_text_color=None, is_legend_show=True, legend_top="center")

    pie.render('./info/电影所占比例.html')


def jizuobiao_huitu2():
    '''极坐标绘制蜗牛'''
    data = []
    for i in range(5):
        for j in range(101):
            theta = j / 100 * 360
            alpha = i * 360 + theta
            # e = 2.718281828459045
            r = math.pow(math.e, 0.003 * alpha)
            data.append([r, theta])
    polar = Polar("极坐标系示例")

    polar.add("", data, symbol_size=0, symbol='circle', start_angle=-25, is_radiusaxis_show=False, area_color="#f3c5b3",
              area_opacity=0.5, is_angleaxis_show=False)

    polar.render('./info/极坐标-蜗牛.html')


if __name__ == '__main__':
	pass
    # dilizuobiaoxi()
    # dilizuobiaoxi2()
    # guanxitu()
    # map_demo()
    # shuiqiu1()
    # shuiqiu2()
    # shuiqiu3()
    # pingxingzuobao()
    # leidatu()
    # sandiantu()
    # sandiandayinziti()
    # ciyuntu()
    # yibiaopan()
    # loudoutu()
    # lianyitexiaosandiantu()
    # jizuobiao_duidiezhuzhuang()
    # jizuobiao_huitu()
    # dianyingbili()
    # jizuobiao_huitu2()
