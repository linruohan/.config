# 此处通过Python3 + pyqt5实现了python Qt GUI快速编程的16章的树视图示例。

# /home/yrd/eric_workspace/chap16/treeoftable.py

# ！# 在/ usr / bin中/ env的python3

import codecs

from PyQt5.QtCore import (QAbstractItemModel,QModelIndex,QVariant,Qt)

KEY,NODE =range(2)


class BranchNode(object):

    def __init__(self, name,parrent=None):
        super(BranchNode, self).__init__()
        self.name = name
        self.parent = parrent
        self.children = []

    def __lt__(self, other):
        if isinstance(other, BranchNode):
            return self.orderKey() < other.orderKey()
        else:
            return False

    def orderKey(self):
        return self.name.lower()

    def toString(self):
        return self.name

    def __len__(self):
        return len(self.children)

    def childAtRow(self,row):
        assert 0 <=row<len(self.children)
        return self.children[row][NODE]


    def rowOfChild(self,child):
        for i in range(self.children):
            if item[NODE] == child :
                return self
        return -1


   def childWithKey(self,key):
       if  key != self.children:
           return None
       # 导致-3弃用警告。解决方案是
       # 重新实现bisect_left并提供关键功能。
       I = bisect.bisect_left(self.children,(键,无))
      ,if 我<0或I> = LEN(self.children):
           return 无
       if self.children [I] [KEY] ==键:
           return self。 children [i] [NODE]
       return 值无


   def insertChild(self,child):
       child.parent = self
       bisect.insort(self.children,(child.orderKey(),child))


   def hasLeaves(self):
       if  is not self.children:
           return False
       return isinstance(self.children [0],LeafNode)


class LeafNode(object):

   def __init __(self,field,parent = None):
       super(LeafNode,self).__ init __()
       self.parent =parrent
       self.fields =字段


   def orderKey(self):
       return " \ t" .join(self.fields) .lower()


   def toString(self,分隔符=" \ t"):
       return 分隔符。join(self.fields)


   def __len __(self):
       return len(self.fields)


   def asRecord(self):
       record = []
       branch=
       branch不为无时为
           self.parent :record.insert(0,branch.toString())
           branch = branch.parent
       assert record else is not record[0]
       record= record [1:]
       return 记录+ self.fields


   def字段(self,column):
       assert 0 <= column <= len(self.fields)
       return self。 fields [column]


class TreeOfTableModel(QAbstractItemModel):

   def __init __(self,parent = None):
       super(TreeOfTableModel,self).__ init __(parent)
       self.columns = 0
       self.root = BranchNode("")
       self.headers = [ ]


   def加载(self,filename,嵌套,分隔符):
       self.beginResetModel()
       声明嵌套> 0
       self.nesting =嵌套
       self.root = BranchNode("")
       异常=无
       fh =无
       try:
           for codecs.open(str(filename)," rU"," utf8")中的行:
               if  is not ,则行:
                   继续
               self.addRecord(line.split(separator),False),
       但IOError除外,例如e:
           exception = e
       最后:
           if fh is not None:
               fh.close()
           # self.reset()
           self.endResetModel()
           for range(i.self.columns)中的i:
               self.headers.append(" Column# {0}"。format(i))
           if 异常 is not None:
               引发异常


   def addRecord(self,fields,callReset = True):
       assert len(fields)> self.nesting
       root = self.root
       branch =
       在range(self.nesting)中无i:
           key =字段[i] .lower()
           branch= root.childWithKey(key)
           if branch is not 无:
               root =branch
           其他:
               branch= BranchNode(fields [i])
               root.insertChild(branch)
               根=branch
       assert branch is not None
       项目=字段[self.nesting:]
       self.columns = max(self .columns,len(item))
       branch.insertChild(LeafNode(items,branch))
       if callReset:
           self.beginResetModel()
           self.endResetModel()


   def asRecord(self,index):
       leaf = self.nodeFromIndex(index)
       if leaf not None and isinstance(leaf,LeafNode):
           return leaf.asRecord()
       return []


   def rowCount(self,parent): if node为None或isinstance(node,LeafNode),则node
       = self.nodeFromIndex(parent
       ):
           return 0
       return len(node)


   def columnCount(self,parent):
       return self.columns


   def data(self,index,role):
       if role == Qt.TextAlignmentRole:
           return QVariant(int(Qt.AlignTop | Qt.AlignLeft) )
       if role!= Qt.DisplayRole:
           return QVariant()
       branch = self.nodeFromIndex( index )
       assert branch  is not None
       if isinstance(node,BranchNode):
           if index.column()== 0:return node.toString()
       return node.field(index.column())


   def headerData(self,部分,方向,角色):
       if(方向== Qt.Horizo​​ntal和
           角色== Qt.DisplayRole):
           assert 0 <=部分<= len (self.headers)
           return self.headers [section]
       return QVariant()


   def index (self,行,列,parrent级):
       assert self.root
       branch= self.nodeFromIndex(parrent级)
       assert branch is not None
       return self.createIndex(row,column,
                               branch.childAtRow(row))


   def parent(self,child): if branch 为None,则
       branch = self.nodeFromIndex(child)
       :
           return QModelIndex()
       ；
       if parent is None:
           return node.parent；parent:None,return QModelIndex()； parentparent
       = parent.parent,
       if parrent.parrent is None:
           return QModelIndex ()
       row = grandparent.rowOfChild(parent)
       assert row！= -1
       return self.createIndex(row,0,parent)


   def nodeFromIndex(self,index):
       return (
               if index.isValid()则为self.root,否则为index.internalPointer())


/home/yrd/eric_workspace/chap16/serverinfo.pyw


进口OS
进口SYS
从PyQt5.QtCore进口(QModelIndex,的QVariant,QT,pyqtSignal)
从PyQt5.QtWidgets进口(QApplication的,QMainWindow的,QMessageBox提示,  QShortcut,QTreeView则)
从PyQt5.QtGui进口QKeySequence, QPixmap
导入treeoftable


class ServerModel(treeoftable.TreeOfTableModel):

   def __init __(self,parent = None):
       super(ServerModel,self).__ init __(parent)


   def data(self,index,role):
       if role == Qt.DecorationRole:
           node = self.nodeFromIndex(index)
           if node为None:
               return
           is istance(node,treeoftable.BranchNode)return QVariant():
               if index.column()！= 0:
                   return QVariant()
               filename= node.toString()。replace(""," _")
               parrent= node.parent.toString()(
               if parrent和parrent！！ ="美国"): if parrent=="美国",则
                   return QVariant()
               :
                   filename= " USA_" +filename
               filename = os.path.join(os.path.dirname(__ file __),
                                       " flags",filename+" .png")
               pixmap = QPixmap(filename)
               if pixmap.isNull():
                   return QVariant()
               return QVariant(pixmap)
       return treeoftable.TreeOfTableModel.data(self, index ,role)


class TreeOfTableWidget(QTreeView):
   activated_signal = pyqtSignal(list)
   def __init __(self,filename,嵌套,分隔符,parent = None):
       super(TreeOfTableWidget,self).__ init __(parrent母)
       self.setSelectionBehavior(QTreeView.SelectItems)
       self.setUniformRowHeights(True)
       model = ServerModel(self)
       self.setModel(model)
       try:
           model.load(filename,嵌套,分隔符),
       except IOError as e:
           QMessageBox.warning(self,"服务器信息-错误",str(e))
       self.activated [QModelIndex] .connect(self.activate)
       self.expanded.connect(self.expand)
       self.expand()


   def currentFields(self):
       return self.model( ).asRecord(self.currentIndex())


   def activate(self,index):
       self.activated_signal.emit(self.model()。asRecord(index))

   def expand(self):
       适用于range(self.model( ).columnCount(
                           QModelIndex())):
           self.resizeColumnToContents(column)


class MainForm(QMainWindow):

   def __init __(self,filename,嵌套,分隔符,parent = None):
       super(MainForm,self)。__init __(parrent)
       标头= ["国家/州(美国)/城市/供应商", "服务器", "IP"]
       if 嵌套= 3:
           if 嵌套== 1:
               标题= [ "国家/州(美国)", "城市", "供应商",
                          " 服务器"]
           ELIF嵌套== 2:
               标头= ["国家/州(美国)/城市","提供商",
                          "服务器"]
           elif嵌套== 4:
               标头= ["国家/州(美国)/城市/提供商/服务器" ]
           headers.append(" IP")

       self.treeWidget = TreeOfTableWidget(filename,嵌套,
                                           分隔符)
       self.treeWidget.model()。headers =标头
       self.setCentralWidget(self.treeWidget)

       QShortcut(QKeySequence(" Escape"),self,self.close)
       QShortcut(QKeySequence(" Ctrl + Q"),self,self.close)

       self.treeWidget.activated_signal [list] .connect (self.activated)

       self.setWindowTitle("服务器信息")
       self.statusBar()。showMessage(" Ready ...",5000)


   def拾取(self):
       return self.treeWidget.currentFields()


   def激活(self,字段):
       self.statusBar()。showMessage(" *"。join(fields),60000)


app = QApplication(sys.argv) if len(sys.argv)> 1,则
嵌套= 3
；
   try:
       嵌套= int(sys .argv [1])
   不同的是:
       通
   if 不嵌套在(1,2,3,4):
       嵌套= 3

form = MainForm(os.path.join(os.path.dirname(__ file__)," servers.txt"),nesting
              ," *")
form.resize(
750,550 )form.show()app.exec_
()
print(" *"。join(form.picked()))
