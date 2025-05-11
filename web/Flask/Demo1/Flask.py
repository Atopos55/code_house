from flask import Flask, request, jsonify, send_from_directory, render_template
import requests
import base64
import os
import time
import uuid
from threading import Thread
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
CORS(app)

#用来写主页
@app.route('/')
def home():
    return render_template('home.html')

#用来写生成贴图的页面
@app.route("/index")
def index():
    return render_template('index.html')


#用来写生成贴图的页面
@app.route("/in")
def ini():
    return render_template('in.html')

#用来写生成贴图的页面
@app.route("/inde")
def inde():
    return render_template('inde.html')

#用来写介绍信息的页面
@app.route("/introduction")
def introduction():
    return render_template("introduction.html")

#用来装载模型
@app.route('/model')
def get_model():
    # 返回模型文件的路径
    model_path = 'static/models/马克杯.glb'
    return send_from_directory('static/models', '马克杯.glb', as_attachment=True)

@app.route('/model/path')
def get_model_path():
    # 返回模型文件的路径
    model_path = '/static/models/马克杯.glb'
    return {'model_path': model_path}

#用来写定价查询的页面
@app.route("/price")
def price():
    return render_template("price.html")


if __name__ == '__main__':
    # 运行Flask应用
    app.run(debug=True, port=5050)