from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
from werkzeug.utils import secure_filename#获取文件名字


app = Flask(__name__)


@app.route('/')#路由
def index():
    return render_template('index.html')

@app.route('/upload',methods=['GET','POST'])#路由
def upload():
    file=request.files.get('file')#获取name=file的文件
    filename=secure_filename(file.filename)

    #print(type(filename))
    #with open('static/%s' %filename,'wb') as f:
    #    f.write(file.read())
    filepath=r'E:\atom\Python\web\demo01\static\files\%s' %filename
    file.save(filepath)

    return render_template('file.html',path='static/files/%s' %filename)

if __name__ == '__main__':
    app.run(debug=True)
