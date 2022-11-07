################################################## Cat's Mind #######################################################

고양이 꼬리의 움직임 패턴 기반 감정 분류모델 만들기

<note> 해당 페이지는 자유롭게 수정하셔도 좋습니다. 다만 고쳐놓기만 하면 안 보니 내용 바꿨으면 구두로도 전달
<note2> 다 한 작업은 삭제하지 말아주세요. 업무일지의 기능도 일부 담당 중입니다. 

보드 형식으로 공유하고자 할 경우 이곳 참고
https://github.com/users/kimslocal/projects/1/views/2?layout=board

#####################################################################################################################


____________________프로젝트 방향______________________________________
[현재]
각 프레임 별로 계산한 각도값들을 정제해 Classifier의 training 자료로 활용함.
최종적으로 영상 -> 프레임 추출 -> RCNN으로 Keypoint 탐지 -> Keypoint 각도 계산 -> Classifier -> 분류 결과
로 이어지는 프로세스 라인을 기획 중.


_________________________일정________________________________________

할 일 페이즈 1:

1. [완료] Keypoint integrity 검증하는 기능 bb converter에 넣어서 git에 올리기

2. [완료] 업데이트된 데이터셋 내려받아서 가공 후 git에 업로드

3. [완료] Predict 돌렸을 때 나오는 keypoint visualization 기능 구현하기

4. [완료] Keypoint와 keypoint 이름을 맞게 부착하기

5. [완료] Augemtnation 해서 돌리기
      -> Roboflow에서 Augmentation한 데이터를 따로 내려받음

6. [진행 중] Cocoeval.py에서 sigma 수치가 어떤 의미인지 파악하기(원본에서 수치가 고정적이지 않은 이유)
      -> 이후 고양이에 맞게 개수해서 RCNN모델 성능 향상이 있는지 확인하기
      
7. 라벨 데이터 추가적으로 더 확보하기
      -> 영상 프레임에 말고 단독 이미지 데이터 라벨링을 더 많이 해야 모델이 더 robust해질 것 같다. 

8. Keypoint Model의 Training 결과(Loss 등) 수치적으로 확실하게 파악하기


할 일 페이즈 2:

1. [완료] Predicted된  keypoint 중 어떤 것이 tail_0인지 찾기.
   그냥 순서대로 나옴. 6번째 인덱스.

2. [진행] 고양이 몸의 중심선을 기준으로 다른 점들간의 각도를 계산해서 array로 저장하는 스크립트 만들기
   -> Github에 labeler_and_angle_calcutor.iypnb 참조.
   -> 각도 기준에 대해서 고민 좀 다시 해봐야 함. 중심선 잡는 기준, 그리고 일부 keypoint는 예각, 둔각이 기준없이 나오게 되는데 한 쪽으로 통일할지 어떻게 할지 협의해야 함.
   
3. 동일한 video의 2초대 subvideo를 일정 간격으로 샘플링한 프레임 컷 25~30개에 대해 모델을 적용시켜서 각 keypoint의 각도를 temporal series로 만들기
   + 거기에 감정 라벨링하기 -> 실질적인 training data
   + 각각의 컴포넌트는 대략적으로 만들었으나 다 별개의 ipynb파일로 나뉘어져 있어서 통합적으로 관리하는 파일 필요. 
   
_____

할 일 페이즈 3:

1. 각도값 데이터 전처리하기 

2. 영상 프레임 감정 라벨링하기

3. 적합한 머신러닝 알고리즘 찾은 후 학습하기
   -> GridSearchCV 등으로 가장 효율 좋은 모델 찾는 것 필요

4. 영상 -> 샘플링 -> 모델 run 이어지도록 만들기


_______

3. app으로 기능 구현하기



_______________________잠재적 문제점들 거론하는 영역____________________________

1. keypoint detector의 training 자료로 연속되는 프레임 컷 말고 단독 이미지를 많이 사용해야 모델이 더 빨리 robust해질 것 같습니다.

이상적인 시나리오라면 (keypoint detector의 성능이 좋다면) 이걸 그대로 유튜브 영상들에 돌려서 각도 데이터들을 다 자동으로 추출해서 다음 emotion classifier에게 먹여줄 training
data를 바로 확보하면 좋겠는데, keypoint detector의 성능이 빠른 시일 안에 향상이 안된다면 아예 저희가 직접 영상 프레임들에 대해 라벨링한 걸 가지고 emotion classifier를 만들어야
할 지도 모르겠습니다. 그 점을 고려하면 앞으로 라벨링할 때 Roboflow에서 연속된 이미지 프레임만 가지는 데이터셋과, 단독 이미지만으로 구성된 데이터셋을 따로 분리해서 관리하는 것이
좋아 보입니다 (막줄이 핵심). 

