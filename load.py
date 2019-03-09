#load the trained model's structure and weights from json and h5 file
import numpy as np
import keras.models
from scipy.misc import imread, imresize,imshow
from keras.models import Sequential, model_from_json
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
import tensorflow as tf

def init():

    json_file = open('modelStructure.json','r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    model.load_weights("modelWeights.h5")
    #compile and evaluate loaded model
    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    #loss,accuracy = model.evaluate(X_test,y_test)
    #print('loss:', loss)
    #print('accuracy:', accuracy)
    graph = tf.get_default_graph()
    
    return model,graph

