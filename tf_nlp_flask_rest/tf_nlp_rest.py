# -*- coding: utf-8 -*-
"""tf_nlp_rest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DEQEwlRiA_Yln3ImnA6vowZ6cQ07pKRW
"""

!ls

!unzip text_classifier_model.zip

import tensorflow as tf

!ls

from tensorflow.keras.models import load_model

model = load_model('text_classifier_model/1/')

import pickle

with open('tfidfmodel.pickle','rb') as file:
    tfidf = pickle.load(file)

!pip install flask-ngrok

from flask_ngrok import run_with_ngrok
from flask import Flask, request

app = Flask(__name__)

run_with_ngrok(app)

@app.route('/predict',methods=['POST'])
def text_classifier():
    request_data = request.get_json(force=True)
    text = request_data['sentence']
    print("printing the sentence")
    print(text)
    text_list=[]
    text_list.append(text)
    print(text_list)
    numeric_text = tfidf.transform(text_list).toarray()
    output = model.predict(numeric_text)[:,1]
    print("Printing prediction")
    print(output)
    sentiment="unknown"
    if output[0] > 0.5 :
      print("positive prediction")
      sentiment="postive"
    else:
      print("negative prediction")
      sentiment="negative"
    print("Printing sentiment")     
    print(sentiment)
    return "The sentiment is {}".format(sentiment)

app.run()

