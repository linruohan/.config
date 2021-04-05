# *_*coding:utf-8 *_* 
__Author__ = 'xiaohan'
# listview = QListView()
# # 实例化列表模型，添加数据
# slm = QStringListModel()
# # 设置模型列表视图，加载数据列表
# slm.setStringList(list(work_category.values()))
# # 设置列表视图的模型
# listview.setModel(slm)
# # 单击触发自定义的槽函数
# listview.clicked.connect(self.listview_clicked)
# self.left_layout.addWidget(listview)
self.left_layout.addWidget(category_list)

def listview_clicked(self, qModelIndex):
    # 提示信息弹窗，你选择的信息
    # QMessageBox.information(self, 'Tips', '你选择了：' + list(work_category.values())[qModelIndex.row()])
    list_name = list(work_category.values())[qModelIndex.row()]
    print(list_name)