#coding=utf-8

import requests,re

r=requests.get("http://huaban.com/favorite/beauty/")
# def make_ajax_url(No):
#     """ 返回ajax请求的url """
#     return "http://huaban.com/favorite/beauty/?i5p998kw&max=" + No + "&limit=20&wfl=1"
#
# html = requests.get(url=make_ajax_url(images[-1]['id'])).content
html=r.content
re=re.compile(r'app\.page\["pins"\].*')
appPins=re.findall(html)
null=None
result=eval(appPins[0][19:-1])
images=[]
for i in result:
    info={}
    info['id']=str(i['pin_id'])
    info['url']="http://img.hb.aicdn.com/"+i["file"]["key"]+"_fw658"
    ifo['type']=i["file"]["type"][6:]
    images.append(info)

for image in images:
    req=requests.get(image["url"])
    imageName=image["id"]+"."+image["type"]
    with open(imageName,'wb') as f:
        f.write(req.content)
