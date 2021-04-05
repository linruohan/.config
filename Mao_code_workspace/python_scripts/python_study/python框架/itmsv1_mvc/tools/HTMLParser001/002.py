from html5lib import HTMLParser

html = '''<h3 class="tb-main-title" data-title="【金冠现货/全色/顶配版】Xiaomi/小米 小米note移动联通4G手机">
     【金冠现货/全色/顶配版】Xiaomi/小米 小米note移动联通4G手机
   </h3>
   <p class="tb-subtitle">
 【购机即送布丁套+高清贴膜+线控耳机+剪卡器+电影支架等等,套餐更多豪礼更优惠】    【购机即送布丁套+高清贴膜+线控耳机+剪卡器+电影支架等等,套餐更多豪礼更优惠】    【金冠信誉+顺丰包邮+全国联保---多重保障】
 </p>
   <div id="J_TEditItem" class="tb-editor-menu"></div>
 </div>
<h3 class="tb-main-title" data-title="【现货增强/标准】MIUI/小米 红米手机2红米2移动联通电信4G双卡">
     【现货增强/标准】MIUI/小米 红米手机2红米2移动联通电信4G双卡
   </h3>
   <p class="tb-subtitle">
 [红米手机2代颜色版本较多,请亲们阅读购买说明按需选购---感谢光临] 【金皇冠信誉小米手机集市销量第一】【购买套餐送高清钢化膜+线控通话耳机+ 剪卡器(含还原卡托)+ 防辐射贴+专用高清贴膜+ 擦机布+ 耳机绕线器+手机电影支架+ 一年延保服务+ 默认享受顺丰包邮 !
 </p>
   <div id="J_TEditItem" class="tb-editor-menu"></div>
 </div>'''


# 定义一个MyParser继承自HTMLParser
class MyParser (HTMLParser):
    re = []  # 放置结果
    flg = 0  # 标志，用以标记是否找到我们需要的标签
    def feed(self,data):
        return data
    def handle_starttag(self, tag, attrs):
        # if tag == 'h3':  # 目标标签
        #
        for attr in attrs:
            if attr[0] == 'class' and attr[1] == 'tb-main-title':  # 目标标签具有的属性
                self.flg = 1  # 符合条件则将标志设置为1
                break
            else:
                pass


def handle_data(self, data):
    if self.flg == 1:
        self.re.append (data.strip ())  # 如果标志为我们需要的标志，则将数据添加到列表中
        self.flg = 0  # 重置标志，进行下次迭代
    else:
        pass


my = MyParser ()
my.feed (html)
print (my.re)
