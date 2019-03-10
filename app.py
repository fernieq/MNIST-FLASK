#import flask class
#render the html template to display the web
#request class to handle post/get methods
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

#import cansandra packages to store the input and output data
import logging
import time
import socket

log = logging.getLogger()
log.setLevel('INFO')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)
#from cassandra.cluster import Cluster
#from cassandra.query import SimpleStatement
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
    #we store the id number, input number, and the time of the input to a table called mnist1
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

#init flask app
app = Flask(__name__)
global model, graph
model, graph = init()
    
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict/', methods=['GET','POST'])
def predict():
    #get the time
    uploadtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    
    #whenever the predict method is called, we're going
    #to input the user drawn character as an image into the model
    #perform inference, and return the classification
    #get the raw data format of the image
    formatImage(request.get_data())

    #read the image into memory
    x = imread('output.png', mode='L')
    #compute a bit-wise inversion so black becomes white and vice versa
    x = np.invert(x)
    #resize the image
    x = imresize(x,(28,28))
    #convert to a 4D tensor to feed into our model
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
    
def formatImage(imgData):
    """Decode the input image to raw binary data and feed it into the graph"""
    imgstr = re.search(b'base64,(.*)', imgData).group(1)
    with open('output.png','wb') as output:
        output.write(base64.decodebytes(imgstr))

#127.0.0.1:5000
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

