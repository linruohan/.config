修改 Hosts 解决 Github 访问失败马克
乌图米
乌图米
今天写论文了吗？

这篇文章介绍一下如何通过修改 Hosts 提升 Github 访问速度。顺带科普一些笔者在搜罗相关知识时，收获的知识豆，例如 IP 地址、域名等等。

前面都是知识豆与原因分析，具体方法是：修改系统的「Hosts」无后缀文件，跳过 DNS 解析直接访问域名对应 IP 地址。详见最后几个小节。更新日期：20210606。

简洁版在这里：
乌图米：修改 Hosts 解决 Github 访问失败​
zhuanlan.zhihu.com图标
0 Github 访问失败或者缓慢？

为什么会访问失败或者速度很慢？

国内网络访问 Github 速度过慢的原因有许多，但其中最直接和原因是其 CND 域名遭到 DNS 污染，导致我们无法连接使用 GitHub 的加速服务，因此访问速度缓慢。

简单理解：CDN「Content Delivery Network」，即内容分发网络，依靠部署在各地的边缘服务器，平衡中心服务器的负荷，就近提供用户所需内容，提高响应速度和命中率。DNS 污染，是指一些刻意或无意制造出来的数据包，把域名指向不正确的 IP 地址，阻碍了网络访问。

我们默认从目标网址的最近 CDN 节点获取内容，但当节点过远或 DNS 指向错误时，就会操成访问速度过慢或无法访问的问题。
1 访问慢、无法加载还是无法通讯？

这三种情况是有区别的，含义不一样：

    访问慢：连接延迟高，内容能够被加载但需要较长的时间。无法加载：浏览器无法打开网址。无法通讯：无法进行直接的网络通讯，包括了上一种情况。

自然导致这三种情况的原因也不尽相同：

    访问慢：服务器或 CDN 节点的地理位置相对较远，难以物理超度。注意这里的表现是延迟高，不一定是每秒传输速度慢。无法加载：可能由于长时间的未响应，即访问慢的情况，导致浏览器判定无法加载内容；可能由于网址对应内容不能被直接访问，即无可访问内容或无权限访问。无法通讯：这类情况往往是 IP 解析错误，即遭受 DNS 污染；否则就是 IP 服务器出现了内部错误。

2 检测一下

可以利用两个工具来判断不同域名或 IP 地址是上述那种情况。笔者以github.com为例，实际操作一遍检测的过程，看看是什么情况：

    首先利用网络上的ping工具，例如这个，检测网址、IP 地址的通讯情况。输入要检测的网址github.com，点击「Ping 检测」。工具提供的服务是利用自己分布在各地的网络节点的本机ping工具，执行对网址的ping操作，汇总结果，统计响应网址的服务器 IP。检测结果如下图示。共计 106 个检测点，其中接受响应速度最快的节点在加拿大，目标服务器对其响应时间为 14ms；最慢在中国香港，响应时间 243ms。在成功访问的所有节点中，目标服务器的平均响应时间是 163.5ms。地图与颜色响应了国内不同省市的访问时间，红色说明访问超时，白色说明没有参与节点；约偏向绿色则响应时间越短。右侧还有一个统计表。这里的情况是：国内节点无法ping通github.com，即无法建立网络通讯。

    注意地图下方有一个独立 IP 的统计框，里面列举了所有节点被响应的 IP 地址。我们知道，网址到 IP 需要经过 DNS 解析，这里呈现的便是各个检测节点，经过默认的 DNS 解析得到的对应 IP 地址的汇总。事实上，你连接的网络也有默认或设定的 DNS，也会有一个解析得到的目标 IP，如果无法访问这个 IP 地址，就意味着你当前的网络无法访问github.com。

    再往下便是具体的每个节点的响应信息。

网络上的ping工具能为我们提供三个重要的信息：首先，如果存在ping通的节点，那么 IP 服务器没有宕机；其次，响应 IP 汇总表提供了所有可能的服务器与 CDN 的 IP 地址；最后，具体信息部分可以点击响应时间排序，我们可以找到响应最快的服务器 IP。

    接着我们使用自己电脑的ping工具来测试网络。打开终端，输入ping [ip address]，替换其中的 IP 地址或域名即可。我们不ping域名，那样会ping向设置的 DNS 解析出来的 IP 地址。我们ping上一步得到的响应最快的服务器。

ping 140.82.114.4  # 这个IP是响应最快的，来自加拿大
ping 192.30.253.112  # 这个IP也可以响应，来自中国香港

    虽然存在丢包的情况，但可以ping通。延迟较高。

    我们再ping上一步中连接超时的节点，对应的响应 IP。

ping 13.229.188.59  # 来自江苏宿迁[电信]，响应超时

    预料之中，现在就无法ping通了。

这一步说明，如果我们网络设置的 DNS 解析出的github.com的 IP 无法在本机ping通，我们便不能够访问该网址。这也是后面通过修改系统 Hosts 文件来解决访问失败问题的原因。

最后我们可以用浏览器尝试直接打开ping通的 IP 地址。其结果是：140.82.114.4无法被浏览器加载；192.30.253.112可以加载出 Github 首页。
3 检测结果

上一步操作的结果就是我们判断三种情况的依据。

    通过192.30.253.112响应的github.com，属于「访问慢」，可以连接但延迟较高；IP 可以被浏览器加载。通过140.82.114.4响应的github.com，同样属于「访问慢」；但被浏览器直接加载时，属于「无法加载」，即可以ping通但无法直接访问。通过13.229.188.59响应的github.com，属于「无法通讯」，无法建立链接。

4 域名，网址与 IP 地址

上面提到的这些东西有点乱了，整理一下。

    「IP 地址」：每个连接到互联网的主机都会被分配一个 IP 地址，用来唯一标识该主机，节点之间的访问通过 IP 地址来进行，形如192.30.253.112。「域名」：IP 地址使用数字标识，使用时不好记忆书写，因此在 IP 地址的基础上又发展出一种符号化的地址方案，来代替数字型的 IP 地址。每一个符号化的地址都与特定的 IP 地址对应。IP 地址相对应的字符型地址，就被称为域名。形如github.com。「网址」：URL「统一资源定位符」，俗称为网址。浏览器地址栏输入的字符串，服务器上储存文件的位置。格式为：<协议>://<域名或IP>:<端口>/<路径>。<协议>://<域名或IP>是必需的，<端口>/<路径>有时可省略。形如https://www.github.com/wootommy。「DNS」：域名虽然便于人们记忆，但节点之间通过 IP 地址通讯。两者之间的转换工作称为域名解析，域名解析需要由专门的域名解析服务器来完成，即 DNS 服务器。域名的最终指向是 IP 地址。

注意，IP 地址和域名是一对多的关系。一个 IP 可以对应多个不同的域名，但是一个域名只能对应一个 IP 地址。就跟人的名字一样，你可以有多个名字。但这些名字都是指的你。

然而我们利用网络工具测试时，发现github.com有多个响应 IP 服务器。这就是开头提到的 CDN 服务。多个平行的服务器响应，均匀了中心服务器的负载，使得网络通讯更加迅速。

现实的情况是，github.com启用的 CDN 节点遭到了 DNS 污染，错误的 IP 指向，包括错误 IP、响应过慢的 IP，都会造成我们访问 Github 失败。
5 方案：修改 Hosts 文件

再总结一下 Github 访问失败或者缓慢的原因：本机网络设置的 DNS 服务器解析 Github 相关域名到遭受污染的 IP 地址，这些 IP 地址要么本身无法访问，要么节点过远，从而导致了访问失败或者速度缓慢。

那么我们修改的方案可以是：

    修改本机 Hosts 文件，主动建立域名与 IP 的映射关系，访问到这些域名时直接使用 Hosts 指定的 IP，绕过 DNS 解析。修改网络的 DNS 服务器，换到能够解析出合适 IP 的 DNS 服务器。

显然第一种方案更加方便。因为 DNS 服务器储存的映射关系是动态更新的，无法直接控制。直接修改本机 Hosts 文件，锁定域名对应的 IP，更加有效方便。当然，Hosts 文件的作用就是绑定域名与 IP 的映射关系。
6 macOS 修改 Hosts 文件

    打开终端，使用 vim 修改 Hosts 文件：

sudo vi /etc/hosts

    操作 vim 可以简单百度一下。添加 Github 相关域名的绑定，修改如下图所示，具体值见最后。

    刷新网络 DNS 缓存：

sudo killall -HUP mDNSResponder

macOS 自带sudo与vim，当然，可以通过 Homebrew 安装最新版本的vim：brew install vim。
7 Windows 修改 Hosts 文件

    打开 cmd，使用 vim 修改 Hosts 文件：

sudo vim C:\Windows\System32\drivers\etc\hosts

    操作 vim 可以简单百度一下。添加 Github 相关域名的绑定，修改如上图所示，具体值见最后。刷新网络 DNS 缓存：

ipconfig /flushdns

Windows 不自带sudo与vim，可以通过 Scoop 安装：scoop install sudo vim。
8 当前 IP 值

列出当前使用的 Github 相关域名比较合适的 IP 值，笔者会定期维护更新。其中的设置可以解决github.com头像无法显示的问题：

# Github Hosts
# Update 20210606
140.82.113.4 github.com
140.82.114.9 nodeload.github.com
140.82.114.6 api.github.com
140.82.112.10 codeload.github.com
185.199.108.133 raw.github.com
185.199.108.153 training.github.com
185.199.108.153 assets-cdn.github.com
185.199.108.153 documentcloud.github.com
185.199.108.154 help.github.com

185.199.108.153 githubstatus.com
199.232.69.194 github.global.ssl.fastly.net

185.199.108.133 raw.githubusercontent.com
185.199.108.133 cloud.githubusercontent.com
185.199.108.133 gist.githubusercontent.com
185.199.108.133 marketplace-screenshots.githubusercontent.com
185.199.108.133 repository-images.githubusercontent.com
185.199.108.133 user-images.githubusercontent.com
185.199.108.133 desktop.githubusercontent.com

185.199.108.133 avatars.githubusercontent.com
185.199.108.133 avatars0.githubusercontent.com
185.199.108.133 avatars1.githubusercontent.com
185.199.108.133 avatars2.githubusercontent.com
185.199.108.133 avatars3.githubusercontent.com
185.199.108.133 avatars4.githubusercontent.com
185.199.108.133 avatars5.githubusercontent.com
185.199.108.133 avatars6.githubusercontent.com
185.199.108.133 avatars7.githubusercontent.com
185.199.108.133 avatars8.githubusercontent.com
# End of the section

不一定保证每一项都是正确、有效的，但目前来说笔者实测能够稳定访问 Github。欢迎大家留言讨论，指正或者建议更好用的 IP 地址。
