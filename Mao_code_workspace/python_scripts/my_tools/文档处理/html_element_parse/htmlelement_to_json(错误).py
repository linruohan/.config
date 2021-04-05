# coding=utf-8
import sys, io
from lxml import etree
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
doc = '''
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv='Pragma' content='No-cache'>
<meta http-equiv='Cache-Control' content='No-cache'>
<meta http-equiv='Expires' content='0'>
<link href="/itmsld/css/style.css;jsessionid=4EE8A05BF625C60756AE60740EC145FE" rel="stylesheet" type="text/css" />
<link href="/itmsld/compnents/bootstrap/css/bootstrap.css" rel="stylesheet" type="text/css" />
<link href="/itmsld/compnents/bootstrap/css/bootstrap-responsive.css" rel="stylesheet"/>
<link id="headCss" href="/itmsld/css/transport.css" type="text/css" rel="stylesheet"/>
<link href="/itmsld/css/listpage.css" type="text/css" rel="stylesheet">
<link href="/itmsld/compnents/jquery-validation/1.10.0/validate.css" type="text/css" rel="stylesheet" />

<script src="/itmsld/compnents/bootstrap/js/jquery-1.7.2.min.js" type="text/javascript"></script>
<script src="/itmsld/js/common.js;jsessionid=4EE8A05BF625C60756AE60740EC145FE" type="text/javascript"></script>

<script  type="text/javascript">
	var themeType = parent.themeType;
	if(themeType == undefined){
		themeType = parent.parent.themeType;
	}
	var skincssType = parent.skincssType;
	if(skincssType == undefined){
		skincssType = parent.parent.skincssType;
	}
	if(themeType == '2'){
		if(skincssType == '1'){
			$("#headCss").attr("href","/itmsld/css/transport.css");
			$("#skin-sel").attr("class","skin-sel-blue");
		}else if(skincssType == '2'){
			$("#headCss").attr("href","/itmsld/cssGreen/transport.css");
			$("#skin-sel").attr("class","skin-sel");
		}else if(skincssType == '3'){
			$("#headCss").attr("href","/itmsld/cssDarkBlue/transport.css");
			$("#skin-sel").attr("class","skin-sel-blue");
		}

		var d=window.parent.document.getElementById("skin-sel");
		if(d==null){
			d = parent.parent.document.getElementById("skin-sel");
		}
		if(d!=null){
			$(d).children("li").bind("click", function(){
				var value1= parent.$(".skin_seled").text();
				if(value1=="1"){
					$("#headCss").attr("href","/itmsld/css/transport.css");
					$("#skin-sel").attr("class","skin-sel-blue");
				}else if(value1=="2"){
					$("#headCss").attr("href","/itmsld/cssGreen/transport.css");
					$("skin-sel").attr("class","skin-sel");
				}else if(value1=="3"){
					$("#headCss").attr("href","/itmsld/cssDarkBlue/transport.css");
					$("#skin-sel").attr("class","skin-sel-blue");
				}
				jQuery.ajax({
				type : "GET",
				async: false,
				url: "/itmsld/system/skin/change_skin/" + value1 + "/",
				success : function(data) {
					//alert(data);
				}
			});
			});
			}
		}

	//切换皮肤方法
	var d=window.parent.document.getElementById("skin-sel");
	if(d==null){
		d = parent.parent.document.getElementById("skin-sel");
	}
	if(d!=null){
		var value= d.options[d.selectedIndex].value;
		if(value=="1"){
			$("#headCss").attr("href","/itmsld/css/transport.css");
			$("#skin-sel").attr("class","skin-sel-blue");
		}else if(value=="2"){
			$("#headCss").attr("href","/itmsld/cssGreen/transport.css");
			$("#skin-sel").attr("class","skin-sel");
		}else if(value=="3"){
			$("#headCss").attr("href","/itmsld/cssDarkBlue/transport.css");
			$("#skin-sel").attr("class","skin-sel-blue");
		}
		//d.addEventListener("change",ssss,false);
		//监听主页皮肤切换
		$(d).bind("change", function(){
			var  d1=window.parent.document.getElementById("skin-sel");
			if(d1==null){
				d1 = parent.parent.document.getElementById("skin-sel");
			}
			var value1= d1.options[d1.selectedIndex].value;
			if(value1=="1"){
				$("#headCss").attr("href","/itmsld/css/transport.css");
				$("#skin-sel").attr("class","skin-sel-blue");
			}else if(value1=="2"){
				$("#headCss").attr("href","/itmsld/cssGreen/transport.css");
				$("#skin-sel").attr("class","skin-sel");
			}else if(value1=="3"){
				$("#headCss").attr("href","/itmsld/cssDarkBlue/transport.css");
				$("#skin-sel").attr("class","skin-sel-blue");
			}
		});
	}


// 判断页面中的iframe地图是否加载完成了--xiongjie添加
function iframeMapOnload(ifrId, mapLoadCallBack) {
	var ifrObj = document.getElementById(ifrId);
	var type = "load";
	// 兼容浏览器判断
	if(ifrObj.addEventListener) {
		ifrObj.addEventListener(type, mapLoadCallBack, false);
	} else if (ifrObj.attachEvent) {
		ifrObj.attachEvent("on" + type, mapLoadCallBack);
	} else {
		ifrObj["on" + type] = mapLoadCallBack;
	}
}

function resetParentIframeHeight() {
	var height = $("#content_body").height();
	parent.resetIframeHeight(height);
}

// 临时添加应急,地图管理使用ZLT
var tempLoadTimes = 0;
</script>
<!--[if lt IE 9]>
  <script src="/itmsld/compnents/bootstrap/js/html5.js"></script>
<![endif]-->

<!--兼容IE6的插件（ie-bsie）-->
<!--[if lte IE 6]>
<link rel="stylesheet" type="text/css" href="/itmsld/compnents/bootstrap/css/bootstrap-ie6.min.css">
<link rel="stylesheet" type="text/css" href="/itmsld/compnents/bootstrap/css/ie.css">
<![endif]-->
<title>智能交通综合管控平台</title>
</head>
<body id="content_body" data-spy="scroll" data-target=".bs-docs-sidebar" style="margin:0; padding:0px;">


<link href="/itmsld/cssDarkBlue/login_yangling.css" rel="stylesheet" />
<body>
<div id="wrap">
  <div class="login_wrap">
    <div class="decoration"><img src="/itmsld/images/login_2014811/xiushi.png"></div>
    <div class="jinghui"></div>
    <div class="sysname">智能交通综合管控平台</div>
    <div class="login_main_box">
      <div class="version">版本：V1.0</div>
      <div class="itms_logo"><img src="/itmsld/images/login_2014811/itms_logo.png"></div>
      <div class="login_info">
        <form action="j_spring_security_check" method="post" id="loginForm" class="log_form">
          <div class="username"><input type="text" autofocus name="j_username" id="username" maxlength="30" autocomplete="off" value="" placeholder="请输入用户名"></div>
          <div class="password"><input name="j_password" id="password" type="password" value="" maxlength="20" autocomplete="off" placeholder="请输入密码"></div>
          <div class="login_error" style="display:none">


               <div style="font-weight: bold;color: #EA5200;">用户名密码不正确</div>

          </div>
          <div class="login_btn_line">
            <input type="submit" value="登 录" class="btn btn-info" >
            <input type="reset" value="重 置" class="btn" onclick="reset()" style="margin-left:20px;border:1px solid #ccc;">
          </div>
        </form>
      </div>
      <div class="copyright">CopyRight 版权所有 西安翔迅科技有限责任公司</div>
    </div>
  </div>
</div>
</body>
<script type="text/javascript">
    function reset(){
       	$("#username").val("");
       	$("#password").val("");
    }
    $(function(){
		var height = $(window).height();
		$("#wrap").height(height);
		$("#username").focus();
	});
</script>
<script src="/itmsld/compnents/jquery-validation/1.10.0/jquery.validate.min.js" type="text/javascript"></script>
<script src="/itmsld/compnents/jquery-validation/1.10.0/messages_bs_zh.js" type="text/javascript"></script>
<script src="/itmsld/compnents/bootstrap/js/bootstrap.min.js" type="text/javascript"></script>
<script src="/itmsld/js/listpage.js" type="text/javascript"></script>
<script src="/itmsld/js/common.js" type="text/javascript"></script>
<script src="/itmsld/compnents/bootstrap/js/bootstrap-tooltip.js"></script>
<script src="/itmsld/compnents/bootstrap/js/bootstrap-popover.js"></script>
<script src="/itmsld/compnents/bootstrap/js/application.js"></script>
<!--兼容IE6的插件（鄙视ie-bsie）-->
<!--[if lte IE 6]>
<script type="text/javascript" src="/itmsld/compnents/bootstrap/js/bootstrap-ie.js"></script>
<![endif]-->
</body>
</html>
'''


class Html_parse():
    def __init__(self, path):
        self.doc = self.read_html(path)
        self.jsonfile = self.chuli(self.doc)
        self.read_json(self.jsonfile)
        # self.doc.close()
        # self.json.close()

    # 字典中有特定的key
    def has_attr(self, dic1, str):
        list = [k for k, v in dic1.items() if str in k]
        if len(list): return True
        return False

    # 字典value中有中文

    def chinese_contain(self, str1):
        for i in list(str1):
            if u'\u4e00' <= i <= u'\u9fff':
                return True
        return False

    def read_html(self, path):
        f = open(path, 'r', encoding='utf-8')
        data = f.read()
        # print(data)
        return data

    def chuli(self, doc):
        data = {}
        html = doc.replace(u'\xa9', u'').encode('utf-8', 'ignore')
        page = etree.HTML(html)
        htree = etree.ElementTree(page)
        n = 0
        for t in page.iter():
            attr = t.attrib
            text = t.text
            xpath = htree.getpath(t)
            discription = ''
            dic = dict(attr)
            # print(dic.keys())
            key = [k for k, v in dic.items() if self.chinese_contain(v)]
            if len(key):
                discription = dic[key[0]]
            elif self.has_attr(dic, 'name'):
                discription = dic['name']
            elif self.has_attr(dic, 'value'):
                discription = dic['value']
            elif self.has_attr(dic, 'id'):
                discription = dic['id']
            elif self.has_attr(dic, 'id'):
                discription = dic['id']
            elif self.has_attr(dic, 'class'):
                discription = dic['class']
            data[n] = {'discription': discription, 'key': key, 'attr': dict(attr), 'xpath': xpath, 'text': text}
            n += 1

        # print(data)
        jsonfile='123.json'
        f = open(jsonfile, 'w')
        json1 = json.dumps(data)
        f.write(json1)
        print('成功将element集合写入json文件！')
        return jsonfile

    def read_json(self, f):
        n = 0
        with open(f, 'r') as f1:
            data = json.load(f1)
            print(data)
        # for k, v in data.items():
        #     for i, j in v.items():
        #         if j:
        #             # print('这里面的值bu为空')
        #             print('data[%s][%s]=%s' % (k, i, j))
        for k, v in data.items():
            if v['discription']:
                n += 1
                name = v['discription']
                xpath = v['xpath']
                element = 'xpath=>%s' % xpath
                # print(name,xpath,element)
                data1 = str(n) + ':\n' + name + '\n' + element + '\n\n'
                # print(data1)
                with open('001.txt', 'a') as f:
                    f.write(data1)
        print('成功将element写入text文件！')


if __name__ == '__main__':
    path = '01main.html'

    s = Html_parse(path)
    # chuli(doc)
    # read_json('123.json')
