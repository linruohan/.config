# url = 'https://www.douban.com/people/maohuoer/photos'
url = 'https://www.douban.com/people/maohuoer/photos?start=90'
if url.split('photos')[1]=='':
    page=1
else:
    page=int(int(url.split('photos')[1].split('=')[1])/18)
print(page)