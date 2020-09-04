# -*- coding: utf-8 -*- 

import tensorflow as tf
import numpy as np
import json
import requests

SIZE=299
MODEL_URI='http://localhost:8501/v1/models/mnist:predict'
CLASSES = ['4.19학생혁명기념탑', '가든파이브', '가로수길', '경희궁', '관악구청', '광화문', '금천구립가산도서관', '대한민국_역사_박물관', '돈의문_박물관_마을', '디큐브아트센터', '명동성당', '삼전도비', '서대문구청', '서울_남현동_요지', '서울_역사_박물관', '성동구립도서관', '성동구청', '세종대왕_동상', '쉐라톤_서울_디큐브_시티_호텔', '암사종합시장', '영등포구청', '올림픽공원', '올림픽공원_세계평화의문', '전차381호', '중랑구청', '청운문학도서관', '한양대학교_서울캠퍼스']

def get_prediction(image_path):
    image = tf.keras.preprocessing.image.load_img(image_path, target_size=(SIZE, SIZE))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.keras.applications.inception_v3.preprocess_input(image)
    image = np.expand_dims(image, axis=0)

    data = json.dumps({
        'instances': image.tolist()
    })
    response = requests.post(MODEL_URI, data=data.encode('utf-8'))
    result = json.loads(response.text)
    prediction = np.squeeze(result['predictions'][0])
    prediction = prediction.argsort()[-5:][::-1]
    class_top5 = []
    for i in range(len(prediction)):
        CLASS = CLASSES[prediction[i]]
        class_top5.append(CLASS)
    return class_top5

'''    #prediction = np.argmax(prediction)
    class_top5 = []
    for i in range(len(prediction)):
        CLASS = CLASSES[prediction[i]]
        #class_top5.append(CLASS)
'''        
#get_prediction(r'C:\Users\choiu\DACON Dropbox\01 Competition\26 NIA 랜드마크\2. 데이터\ai_hub_2020-08-28\서울시\삼전도비\삼전도비_108.JPG')
