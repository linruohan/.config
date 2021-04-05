from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
from PyQt5.QtCore import *
import sys
import os


class HelloWorldHtmlApp(QWidget):
    def __init__(self):
        super(HelloWorldHtmlApp, self).__init__()
        self.setWindowTitle('QWebView Interactive Demo')
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.view = QWebEngineView()
        # self.view.setHtml('''
        #   <html>
        #     <head>
        #       <title>A Demo Page</title>
        #
        #       <script language="javascript">
        #         // Completes the full-name control and
        #         // shows the submit button
        #         function completeAndReturnName() {
        #           var fname = document.getElementById('fname').value;
        #           var lname = document.getElementById('lname').value;
        #           var full = fname + ' ' + lname;
        #
        #           document.getElementById('fullname').value = full;
        #           document.getElementById('submit-btn').style.display = 'block';
        #
        #           return full;
        #         }
        #       </script>
        #     </head>
        #     <body>
        #       <form>
        #         <label for="fname">First name:</label>
        #         <input type="text" name="fname" id="fname"></input>
        #         <br />
        #         <label for="lname">Last name:</label>
        #         <input type="text" name="lname" id="lname"></input>
        #         <br />
        #         <label for="fullname">Full name:</label>
        #         <input disabled type="text" name="fullname" id="fullname"></input>
        #         <br />
        #         <input style="display: none;" type="submit" id="submit-btn"></input>
        #       </form>
        #     </body>
        #   </html>
        # ''')
        # self.view.load(QUrl.fromLocalFile(os.path.join(os.path.dirname(__file__),"001.html")))
        self.view.load(QUrl(os.path.dirname(__file__)+'./001.html'))
        # self.view.show()
        self.button = QPushButton('Set Full Name')
        self.button.clicked.connect(self.complete_name)

        self.layout.addWidget(self.view)
        self.layout.addWidget(self.button)

    def js_callback(self, result):
        print(result)

    def complete_name(self):
        self.view.page().runJavaScript('completeAndReturnName();', self.js_callback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = HelloWorldHtmlApp()
    tree.show()
    app.exec_()
