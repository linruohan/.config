from xml.parsers.expat import  ParserCreate


class DefaultSaxHandler(object):
    def start_element(self,name,attrs):
        print('sax:start_element:%s,attrs:%s' %(name,str(attrs)))
    def end_element(self,name):
        print('sax:end_element:%s' %name)
    def char_data(self,text):
        print('sax:char_data:%s' %text)

xml=r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handle=DefaultSaxHandler()
parser=ParserCreate()
parser.StartElementHandler=handle.start_element
parser.EndElementHandler=handle.end_element
parser.CharacterDataHandler=handle.char_data
parser.Parse(xml)
