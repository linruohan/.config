# *_*coding:utf-8 *_* 
__Author__ = 'xiaohan'
# coding=utf-8
from pyecharts import Gauge
import random
gauge = Gauge("仪表盘示例")
gauge.add("业务指标", "完成率", 66.66)
gauge.render('gauge.html')