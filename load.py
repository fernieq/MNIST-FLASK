#该文件调用本地训练好的模型，生成model 以及 graph 方便app调用
import numpy as np
import keras.models
from scipy.misc import imread, imresize,imshow
import tensorflow as tf

from keras.models import Sequential
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.models import model_from_json

def init():

    json_file = open('model.json','r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    #将 woeights 载入 model 中
    model.load_weights("model.h5")
    print("Loaded Model from disk")
    
    #compile and evaluate loaded model
    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    #loss,accuracy = model.evaluate(X_test,y_test)
    #print('loss:', loss)
    #print('accuracy:', accuracy)
    graph = tf.get_default_graph()
    
    return model,graph

