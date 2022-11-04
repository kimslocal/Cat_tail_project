# Cat_tail_project
고양이 꼬리 탐지 감정분류 예측모델 만들기

_________________________일정________________________________________

할 일 페이즈 1:

1. [완료] Keypoint integrity 검증하는 기능 bb converter에 넣어서 git에 올리기

2. [완료] 업데이트된 데이터셋 내려받아서 가공 후 git에 업로드

3. [완료] Predict 돌렸을 때 나오는 keypoint visualization 기능 구현하기

4. [완료] Keypoint와 keypoint 이름을 맞게 부착하기

5. Augemtnation 해서 돌리기

6. Cocoeval.py에서 sigma 수치가 어떤 의미인지 파악하기(원본에서 수치가 고정적이지 않은 이유)


할 일 페이즈 2:

1. Predicted된  keypoint 중 어떤 것이 tail_0인지 찾기.

2. 고양이 몸의 선을 기준으로 다른 점들간의 상대각도를 계산해서 array로 저장하는 스크립트 만들기

3. 동일한 video의 2초대 subvideo를 일정 간격으로 샘플링한 프레임 컷 25~30개에 대해 모델을 적용시켜서 각 keypoint의 각도를 temporal series로 만들기
   + 거기에 감정 라벨링하기 -> 실질적인 training data

_____

할 일 페이즈 3:

1. 적합한 머신러닝 알고리즘 찾은 후 학습하기

2. 영상 -> 샘플링 -> 모델run 이어지도록 만들기

3. app으로 기능 구현하기

