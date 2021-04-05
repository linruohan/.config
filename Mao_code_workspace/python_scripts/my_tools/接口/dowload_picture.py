# coding=utf-8
import requests
from contextlib import closing


def download():
    url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&' \
          'sec=1504068152047&di=8b53bf6b8e5deb64c8ac726e260091aa&imgtype=0&src=http%3A%2F%2' \
          'Fpic.baike.soso.com%2Fp%2F20140415%2Fbki-20140415104220-671149140.jpg'
    response = requests.get(url, stream=True)
    # 一个图片是由字节流数据组成，我们可以把图片
    # 分层多个字节流数据，加载到内存，然后复制字节流到
    # 一个本地路径，最后组合成一张图片。 stream=字节流
    print(response.status_code)
    print(response.content)
    # contextlib.closing()
    # 函数是实现在一个代码块之后自动关闭，这里的代码块，就是我们请求下载图片的过程。
    # 及时关闭stream
    with closing(requests.get(url, stream=True)) as response:
        with open('selenium1.png', 'wb')as f:
            # 每128个流遍历一次
            for data in response.iter_content(128):
                # 把流写入到文件，这个文件最后写入完成就是，selenium.png
                f.write(data)


if __name__ == '__main__':
    download()
