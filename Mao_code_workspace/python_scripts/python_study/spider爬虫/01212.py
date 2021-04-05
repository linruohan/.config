from optparse import OptionParser
import queue
import re
import sqlite3
import threading
import urllib.request
import time
import ThreadPool

class Store(object):
    """结果存储类

    每次操作完成后将结果存入队列，最后把结果统一存进数据库
    """
    def __init__(self, db_name, table_name="blog"):
        """初始化函数

        Args:
            db_name: 数据库文件名
            table_name: 数据库表名
        """
        threading.Thread.__init__(self)
        self._work_queue = queue.Queue()
        if db_name != None:
            self._dbname = db_name
        else:
            self._dbname = "default"+str(int(time.time()))+".db"
        self._tablename = table_name

    def add_item(self, title, user_id, content):
        """添加一条记录

        Args:
            title: 博文标题
            user_id: 博文作者id
            content: 博文内容
        """
        self._work_queue.put((title, user_id, content))

    def store(self):
        """将所有记录存至数据库
        """
        conn = sqlite3.connect(self._dbname)
        c = conn.cursor()
        try:
            c.execute(("CREATE TABLE %s "
                       "(TITLE TEXT PRIMARY KEY NOT NULL, "
                       " USER_NAME TEXT NOT NULL, "
                       " CONTENT TEXT NOT NULL)"%self._tablename))
        except:
            pass
        purchases = []
        while self._work_queue.qsize() != 0:
            purchases.append(self._work_queue.get())
        c.executemany('INSERT INTO %s VALUES (?,?,?)'%self._tablename,
                      purchases)
        conn.commit()
        conn.close()
        print("store end. dbfile name is %s" % (self._dbname))


def Download_URL(url, headers={}):
    """下载指定url页面

    Args:
        url: 要下载页面的URL
        headers: headers为字典结构。键为HTTP请求的消息报头名，值为对应的报头值

    Returns:
        页面下载成功，返回对应的HTML。

    Raises:
        None
    """
    req = urllib.request.Request(urllib.request.quote(url, ":?=/&%"),
                                 headers=headers)
    while True:
        try:
            response = urllib.request.urlopen(req, timeout=5)  # timeout设置超时时间
            html = response.read().decode("utf-8")
            print("success: " + req.full_url)
            return html
        except Exception as reason:
            print(reason)

def Store_Article(title, content):
    """存储文章

    Args：
        title: 文章标题
        content: 文章内容
    """
    global user_id
    global store

    # 新增一条要存储的结果
    store.add_item(title, user_id, content)

def Download_Article(param):
    """下载博文

    Args:
        param: 字典。url键为博文地址，title键为文章标题
    """
    global user_id, headers
    article_url = param['url']
    article_title = param['title']

    # 通过正则匹配，返回博文内容。
    # 随后保存博文内容，标题为：[作者ID]+博文名
    article_html = Download_URL(article_url, headers)
    content = re.findall('(<div id="article_details" class="details">'
                         '[\s\S]*?</div>)'
                         '\s*<dl class="blog-associat-tag">',
                         article_html)[0]
    Store_Article("[" + user_id + "]" + article_title, content)

def Download_Page(param):
    """下载目录页

    Args:
        param: 字典。url键中存有目录页的URL地址。
    """
    global headers, host
    global thread_pool
    page_url = param['url']

    # 正则匹配，返回所有文章的链接和标题。格式为：(链接, 标题)
    # 随后下载每篇博文
    page_html = Download_URL(page_url, headers)
    article_list = re.findall('<span class="link_title">'
                              '<a href="([\s\S]*?)">'
                              '\s*([\s\S]*?)\s*</a></span>',
                              page_html)
    for article in article_list:
        param = {
            'url': host + article[0],
            'title': re.sub(r'[/:*?<|\\]', '', article[1]) + ".html"
        }
        thread_pool.add_work(Download_Article, param)

def Download_Front_Page(param):
    """下载博客首页

    Args:
        param: 字典。url键为博客首页地址。
    """
    global headers, user_id
    global thread_pool
    front_page_url = param["url"]

    # 通过正则匹配，获得页数，博文数。
    # 随后下载所有目录页
    html = Download_URL(front_page_url, headers)
    article_count = int(re.findall("([0-9]+)条数据", html)[0])
    page_count = int(re.findall("共([0-9]+)页", html)[0])
    print("id: " + user_id + "\n" + "article count: " +
          str(article_count) + "\n" + "page count: " + str(page_count))
    for page_num in range(1, page_count+1):
        param = {
            "url": front_page_url + "/article/list/" + str(page_num)
        }
        thread_pool.add_work(Download_Page, param)

def option_parser():
    """解析命令行参数

    Returns:
        (user_id, thread_count, db_name)
        分别为用户ID，线程池线程个数，数据库文件名
    """
    user_id = None
    thread_count = 1
    db_name = None

    parser = OptionParser()
    parser.add_option("-i", "--id", dest="user_id",
                      help="blog owner id", metavar="[user id]")
    parser.add_option("-t", "--thread", dest="thread_count",
                      help="worker thread count", metavar="[count of thread]")
    parser.add_option("-f", "--filename", dest="dbfile",
                      help="data file name", metavar="[data file name]")
    (options, args) = parser.parse_args()
    if options.user_id != None:
        user_id = options.user_id
    else:
        print("eg: blog_backup.py -i csdn_id")
        exit()
    if options.thread_count != None:
        thread_count = int(options.thread_count)
    if options.dbfile != None:
        db_name = options.dbfile
    return (user_id, thread_count, db_name)

def main():
    global thread_pool, store
    global headers, host, user_id
    user_id, thread_count, db_name = option_parser()
    store = Store(db_name)
    thread_pool = ThreadPool.Thread_Pool(thread_count)
    host = "http://blog.csdn.net"
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36"
            " (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
    }

    front_page_url = host + "/" + user_id
    param = {
        "url": front_page_url
    }
    # 向任务队列添加下载博客首页的任务
    # 随后会自动解析下载所有目录页，进而解析下载所有博文
    # 当所有下载任务均结束后，队列为空。在任务进行时队列不会为空。
    # 所以可以通过等待队列为空进行线程同步
    thread_pool.add_work(Download_Front_Page, param)
    thread_pool.wait_queue_empty()

    store.store()
    print("---end---")

if __name__ == "__main__":
    main()
