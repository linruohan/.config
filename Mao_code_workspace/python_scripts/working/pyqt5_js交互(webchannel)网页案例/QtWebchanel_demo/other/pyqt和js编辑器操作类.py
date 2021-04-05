# GithubWEB编辑器的项目很丰富，也都做的很好，于是想利用PyQT5的QWebEngineView来嵌入自己喜欢的WEB编辑器打造自己的编辑器，因为CSS和JS来实现样式和定义一些事件动作很灵活也很漂亮。
#
# 以下是PYQT与JS交互的核心代码：
import os
class EditorOper(object):
    def __init__(self, parent =None):
        self.kContent = KContentOper()
        self.parent = parent
        self.currentItemId = 0
        self.popupMenu = None
        self.noteDir = os.path.join(os.path.abspath('.'), 'note')
        self.statusBar = self.parent.parent().parent().statBar

    def loadContent(self, treeItem):
        self.parent.setEnabled(True)
        self.clearContent()
        itemTreePath = treeItem.getItemTreePath()
        if treeItem.childCount() > 0:
            itemTreePath += '/.desc'
        self.filePath = self.noteDir + itemTreePath.replace('/', '\\')
        try:
            with open(self.filePath, 'r', encoding = 'utf8') as f:
                content = f.read()
            self.renderContent(content)
        except Exception as e:
            self.statusBar.showMessage(e.args[1])
            self.clearContent()

    def saveContent(self, treeItem):
        self.parent.page().runJavaScript('''document.querySelector('[data-toggle="pen"]').innerHTML''', lambda x: self.writeToFsys(x))


    def renderContent(self, content, type='NORMAL'):
        if type == 'WARNNING':
            content = "<b>" + content + "</b>"
        print(content)
        jsStr = '''document.querySelector('[data-toggle="pen"]').innerHTML=decodeURIComponent("%s")''' % (content, )
        self.parent.page().runJavaScript(jsStr)
        self.statusBar.showMessage("加载成功")

    def clearContent(self):
        self.parent.page().runJavaScript('''document.querySelector('[data-toggle="pen"]').innerHTML=""''')

    def writeToFsys(self, content):
        fileDir = '\\'.join(self.filePath.split('\\')[:-1])
        if not os.path.exists(fileDir):
            os.makedirs(fileDir)

        contentPro = ContentProcess(content, fileDir)
        content = contentPro.imgLocal()
        content = parse.quote(content)


        try:
            with open(self.filePath, 'w+', encoding = 'utf8') as f:
                f.write(content)

            self.statusBar.showMessage("保存成功")
        except Exception as e:
            print(e)
            self.statusBar.showMessage(e.args[1])
