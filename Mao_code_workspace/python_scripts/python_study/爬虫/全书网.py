#coding=utf-8
import urllib,re,requests
import json,sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
import MySQLdb
class Sql(object):
    """docstring for Sql."""
    conn=MySQLdb.connect(
    host='127.0.0.1',
    port=3306,
    user='novel',
    passwd='123456',
    db='novel',
    chatset='utf8'
    )
    def addnovel(self,sort,sort_name,name,imag,description,status,author):
        cur=self.conn.cursor()
        cur.execute("insert into novel(sort,sort_name,name,imag,description,status,author) values(%s,'%s','%s','%s','%s','%s','%s')" %(sort_name,name,imag,description,status,author))
        lastrowid=cur.lastrowid
        cur.close()
        self.conn.commit()
        return lastrowid
    def addchapter(self,novelid,title,content):
        cur=self.conn.cursor()
        cur.execute("insert into chapter(novelid,title,content) values(%s,'%s','%s')" %(novelid,title,content))
        cur.close()
        self.conn.commit()

mysql=Sql()

sort_dic={
    1:'玄幻魔法',
    2:'武侠修真',
    3:'纯爱耽美',
    4:'都市言情',
    6:'穿越重生',
    7:'歷史軍事',
    8:'網遊動漫',
    9:'恐怖靈異',
    10:'科幻小說',
    11:'美文名著'
}
def getnovel(url):
    html=requests.get(url).content.decode('gbk').encode('utf-8')
    #獲取書名
    reg=r'<meta property="og:novel:book_name" content="(.*?)"/>'
    bookname=re.findall(reg,html)[0]
    #獲取description([/s/S].*?)
    reg=r'<meta property="og:novel:description" content="(.*?)"/>'
    description=re.findall(reg,html,re.S)
    #獲取image
    reg=r'<meta property="og:novel:image" content="(.*?)"/>'
    bookname=re.findall(reg,html)[0]
    #獲取author
    reg=r'<meta property="og:novel:author" content="(.*?)"/>'
    author=re.findall(reg,html)[0]
    #獲取status
    reg=r'<meta property="og:novel:status" content="(.*?)"/>'
    author=re.findall(reg,html)[0]
    #獲取chapterUrl
    reg=r'<meta property="og:novel:chapter" content="(.*?)"/>'
    chapter=re.findall(reg,html)[0]
    mysql.addnovel()
    

def getlist(sort_id,sort_name):
    html=requests.get('http://www.quanshuwang.com/list/%s_1.html' %sort_id).content.decode('gbk').encode('utf-8')
    reg=r'<a target="_blank" href="(.*?)" class="1 mr10">'
    urllist=re.findall(reg,html)
    for url in urllist:
        getnovel(url)

for sort_id,sort_name in sort_dic.items():
    getlist(sort_id,sort_name)
    # print(sort_id,sort_name)
