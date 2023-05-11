## Cloud -9 Streamlit 으로 웹서비스 만들기

1. requirements.txt 파일을 만들고 필요한 라이브러리들을 입력

2. 저장 후 pip install -r requirements.txt

3. face.py 작성

## 실행 터미널 환경

- root 경로에 resize.sh 파일을 생성

### 파일 권한 부여

chmod +x resize.sh

### 원하는 사이즈로 실행 다음 하단 3개중 1개만

./resize.sh 20 # 20GB 로 늘리기

./resize.sh 30 # 30GB 로 늘리기 : 최소

./resize.sh 40 # 40GB 로 늘리기

streamlit run face.py

## ex

![zz](https://github.com/chosunghyun18/FaceDetection/assets/37647483/9df69a78-8282-4d4e-90bd-68644e178cec)

## 결과

Here are the other attributes:
{
"AgeRange": {
"High": 22,
"Low": 16
},
"Beard": {
"Confidence": 80.1970443725586,
"Value": false
},
"BoundingBox": {
"Height": 0.5413402318954468,
"Left": 0.23372748494148254,
"Top": 0.23699793219566345,
"Width": 0.5475195646286011
},
"Confidence": 99.99995422363281,
"Emotions": [
{
"Confidence": 85.1741943359375,
"Type": "CALM"
},
{
"Confidence": 10.519986152648926,
"Type": "HAPPY"
},
{
"Confidence": 6.427998065948486,
"Type": "SURPRISED"
},
{
"Confidence": 5.936996936798096,
"Type": "FEAR"
},
{
"Confidence": 2.345348596572876,
"Type": "CONFUSED"
},
{
"Confidence": 2.2382357120513916,
"Type": "SAD"
},
{
"Confidence": 0.639853298664093,
"Type": "DISGUSTED"
},
{
"Confidence": 0.5107327699661255,
"Type": "ANGRY"
}
],
"Eyeglasses": {
"Confidence": 96.51451873779297,
"Value": false
},
"EyesOpen": {
"Confidence": 97.9422836303711,
"Value": true
},
"FaceOccluded": {
"Confidence": 99.94535064697266,
"Value": false
},
"Gender": {
"Confidence": 99.57880401611328,
"Value": "Male"
},
"Landmarks": [
{
"Type": "eyeLeft",
"X": 0.3798084259033203,
"Y": 0.45855170488357544
},
{
"Type": "eyeRight",
"X": 0.6198298335075378,
"Y": 0.45753154158592224
},
{
"Type": "mouthLeft",
"X": 0.4033973217010498,
"Y": 0.6510077118873596
},
{
"Type": "mouthRight",
"X": 0.6038918495178223,
"Y": 0.649957537651062
},
{
"Type": "nose",
"X": 0.5055009722709656,
"Y": 0.5686339735984802
},
{
"Type": "leftEyeBrowLeft",
"X": 0.28869378566741943,
"Y": 0.4109380543231964
},
{
"Type": "leftEyeBrowRight",
"X": 0.4304318130016327,
"Y": 0.40330275893211365
},
{
"Type": "leftEyeBrowUp",
"X": 0.3601938784122467,
"Y": 0.3919861316680908
},
{
"Type": "rightEyeBrowLeft",
"X": 0.567288875579834,
"Y": 0.402608722448349
},
{
"Type": "rightEyeBrowRight",
"X": 0.7049663066864014,
"Y": 0.4088987112045288
},
{
"Type": "rightEyeBrowUp",
"X": 0.6359036564826965,
"Y": 0.39062637090682983
},
{
"Type": "leftEyeLeft",
"X": 0.3365462124347687,
"Y": 0.4567447006702423
},
{
"Type": "leftEyeRight",
"X": 0.42722463607788086,
"Y": 0.45989635586738586
},
{
"Type": "leftEyeUp",
"X": 0.37911689281463623,
"Y": 0.4491463005542755
},
{
"Type": "leftEyeDown",
"X": 0.3809894621372223,
"Y": 0.4669574201107025
},
{
"Type": "rightEyeLeft",
"X": 0.5720312595367432,
"Y": 0.45927608013153076
},
{
"Type": "rightEyeRight",
"X": 0.661483645439148,
"Y": 0.45524612069129944
},
{
"Type": "rightEyeUp",
"X": 0.6198933124542236,
"Y": 0.44805917143821716
},
{
"Type": "rightEyeDown",
"X": 0.6185724139213562,
"Y": 0.465856671333313
},
{
"Type": "noseLeft",
"X": 0.45827165246009827,
"Y": 0.5849553346633911
},
{
"Type": "noseRight",
"X": 0.5467996001243591,
"Y": 0.5844612121582031
},
{
"Type": "mouthUp",
"X": 0.5038148164749146,
"Y": 0.6310960650444031
},
{
"Type": "mouthDown",
"X": 0.5043702125549316,
"Y": 0.687904417514801
},
{
"Type": "leftPupil",
"X": 0.3798084259033203,
"Y": 0.45855170488357544
},
{
"Type": "rightPupil",
"X": 0.6198298335075378,
"Y": 0.45753154158592224
},
{
"Type": "upperJawlineLeft",
"X": 0.23258155584335327,
"Y": 0.4489453136920929
},
{
"Type": "midJawlineLeft",
"X": 0.28634679317474365,
"Y": 0.658851146697998
},
{
"Type": "chinBottom",
"X": 0.5045490860939026,
"Y": 0.7841572761535645
},
{
"Type": "midJawlineRight",
"X": 0.7093411087989807,
"Y": 0.6566128134727478
},
{
"Type": "upperJawlineRight",
"X": 0.7540971040725708,
"Y": 0.4463496208190918
}
],
"MouthOpen": {
"Confidence": 93.33851623535156,
"Value": false
},
"Mustache": {
"Confidence": 97.23092651367188,
"Value": false
},
"Pose": {
"Pitch": 1.3268544673919678,
"Roll": -0.5914899110794067,
"Yaw": 0.5754285454750061
},
"Quality": {
"Brightness": 95.37979125976562,
"Sharpness": 86.86019134521484
},
"Smile": {
"Confidence": 83.11076354980469,
"Value": false
},
"Sunglasses": {
"Confidence": 99.99620056152344,
"Value": false
}
