# 用 Flask 写 Hello world 
'''
这是一个很轻量级的 Web 框架，但是扩展性很好。
'''
from flask import Flask 
app = Flask(__name__) 
  
@app.route("/") 
def hello(): 
    return "Hello World!" 
  
if __name__ == "__main__": 
    app.run()
