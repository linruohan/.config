from html.parser import HTMLParser
from urllib.request import urlopen


class Meet():
    def __init__(self, title, time, location):
        self._title = title
        self._time = time
        self._location = location

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        self._time = time

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    def __str__(self):
        return 'title:%s ,time:%s ,location:%s' % (self._title, self._time, self._location)

    __repr__ = __str__


meets = []


class MyHTMLParser(HTMLParser):
    title_w = False
    location_w = False
    title, time, location = "", "", ""

    def handle_starttag(self, tag, attrs):
        # print("start-tag:%s,attrs:%s" % (tag, attrs))
        # 可以写入title
        if tag == "h3" and len(attrs) and 'event-title' in attrs[0]:  # 可以写入title
            self.title_w = True
        # 可以写入time
        if tag == 'time':
            print('time:%s' % attrs[0][1])
            self.time = str(attrs[0][1])
        # 可以写入location
        if tag == 'span' and len(attrs) and 'event-location' in attrs[0]:
            self.location_w = True

    def handle_endtag(self, tag):
        pass
        # print("end-tag:%s" % tag)
        # if tag=="h3":
        #     self.title_w=False

    def handle_startendtag(self, tag, attrs):
        pass
        # print("se-tag:%s,attrs:%s" % (tag, list(attrs)))

    def handle_data(self, data):
        # print("data:%s" % data)
        #处理
        if self.title_w:
            print("title:%s" % data)
            self.title = data
            self.title_w = False
        if self.location_w:
            print("location:%s" % data)
            self.location = data
            meets.append(Meet(self.title, self.time, self.location))
            self.location_w = False

            # def handle_comment(self, data):
            #     print("comment-data:%s" % data)
            #
            # def handle_entityref(self, name):
            #     print("entityref:%s" % name)
            #
            # def handle_charref(self, name):
            #     print("charref:%s" % name)
            #
            # def handle_decl(self, decl):
            #     print("decl:%s" % decl)
            #
            # def handle_pi(self, data):
            #     print("pi:%s" % data)


parser = MyHTMLParser()
with urlopen("https://www.python.org/events/python-events/", ) as f:
    parser.feed(str(f.read()))

print(meets)
