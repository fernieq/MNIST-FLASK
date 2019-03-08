#该文件创建了一个flaskapp，用于构建web框架
from flask import Flask, render_template, request
from scipy.misc import imsave, imread, imresize
import numpy as np
import keras.models
import re
import base64

import sys 
import os
#sys.path.append(os.path.abspath("."))
from load import *

###cassandra 相关的包
import logging
import time
import socket

log = logging.getLogger()
log.setLevel('INFO')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)
#from cassandra.cluster import Cluster
#from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
######################

### Connect to the cassandra database
cluster = Cluster(contact_points=['127.0.0.1'],port=9042)
session = cluster.connect()
    
log.info("Creating keyspace...")
try:
    session.execute("""
        CREATE KEYSPACE
        IF NOT EXISTS mnist_database
        WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '2' }
        """)
        
    log.info("setting keyspace...")
    #session.set_keyspace(mnist_database)
    session.execute("use mnist_database")
    
    log.info("creating table...")
    session.execute("""
        CREATE TABLE mnist1(
        id uuid,
        digits text,
        upload_time timestamp,
        primary key(id)
        )
        """)
except Exception as e:
    log.error("Unable to create keyspace")
    log.error(e)

#############


#model，graph 见load.py
app = Flask(__name__)
global model, graph
model, graph = init()
    
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict/', methods=['GET','POST'])
def predict():
    #获取时间
    uploadtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    
    # 通过画布获取用户画的图像
    parseImage(request.get_data())

    # 将图像进行转换
    x = imread('output.png', mode='L')
    x = np.invert(x)
    x = imresize(x,(28,28))

    #调用模型
    x = x.reshape(1,28,28,1)
    with graph.as_default():
        out = model.predict(x)
        
        print(out)
        print(np.argmax(out, axis=1))
        print(uploadtime)
        response = np.array_str(np.argmax(out, axis=1))
        print(str(response))
        session.execute("INSERT INTO mnist1(id, digits,upload_time) values(uuid(), %s, %s)",[ str(response) , uploadtime])
        return response
    
def parseImage(imgData):
    # 将画布转换为out.png输出
    imgstr = re.search(b'base64,(.*)', imgData).group(1)
    with open('output.png','wb') as output:
        output.write(base64.decodebytes(imgstr))

#127.0.0.1:5000
if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

