
from lxml import etree

html = """<div class="content">
<p>
<a>test</a>
<a class="1">test</a>
</p>
<p>
<h1>test</h1>
</p>
</div>"""

dom = etree.fromstring(html)
a_list=dom.xpath('*')
# a_list = dom.xpath("//a[contains(@class, '1')]")
for a in a_list:
    parent = a.getparent()
    print(a.text)
    # parent.remove(a)
print(etree.tostring(dom, method="html", encoding="utf-8"))
# print(a_list)

# output: b'<div class="content">\n<p>\n<a>test</a>\n</p>\n<p>\n<h1>test</h1>\n</p>\n</div>'