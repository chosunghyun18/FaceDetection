import json

import cv2
import boto3
import numpy as np
import streamlit as st

#업로드 된 File 에서 bytes 와 numpy array (image) 생성하는 function
def prepare_image(file):
    file_bytes = file.read()
    nd_bytes = np.asarray(bytearray(file_bytes), dtype=np.uint8)
    return file_bytes, cv2.imdecode(nd_bytes, 1)

#bound box 를 그리는 function
def draw_bbox(img, bbox):
    h, w, _ = img.shape
    x1 = int(bbox['Left'] * w)
    y1 = int(bbox['Top'] * h)
    x2 = int((bbox['Left'] + bbox['Width']) * w)
    y2 = int((bbox['Top'] + bbox['Height']) * h)
    cv2.rectangle(im, (x1, y1), (x2, y2), (0, 255, 0), 2)
    

#Amazon session 과 rekognition client 초기화
session = boto3.Session(profile_name='default')
client = session.client('rekognition')

st.title("rekognition FaceDetections")
uploaded_file = st.file_uploader("Choose a image")

if uploaded_file is not None:
    
    file_bytes, im = prepare_image(uploaded_file)
    # rekognition api 호출
    response = client.detect_faces(Image={'Bytes': file_bytes}, Attributes=['ALL'])
    for faceDetail in response['FaceDetails']:

        st.text('The detected face is between ' + str(faceDetail['AgeRange']['Low']) + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')

        print('Here are the other attributes:')
        print(json.dumps(faceDetail, indent=4, sort_keys=True))

        st.text("Gender: " + str(faceDetail['Gender']))
        st.text("Smile: " + str(faceDetail['Smile']))
        st.text("Eyeglasses: " + str(faceDetail['Eyeglasses']))
        st.text("Emotions: " + str(faceDetail['Emotions'][0]))
        
        draw_bbox(im, faceDetail['BoundingBox'])

    st.image(im, channels="BGR")