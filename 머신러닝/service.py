import pickle
import pandas as pd
import os

#절대경로(한번 값을 넣고 바뀌지 않을 때 대문자)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#저장한 파일들 불러오기

#인코딩 객체
le = None

#학습된 랜덤포레스트 모델
rf_model = None

#학습에 사용된 컬럼 정보
train_col = None

with open(BASE_DIR + '/le_시도명.pkl', 'rb') as f :
  le = pickle.load(f)

with open(BASE_DIR + '/rf_model.pkl', 'rb') as f :
  rf_model = pickle.load(f)
  
with open(BASE_DIR + '/train_col.pkl', 'rb') as f :
  train_col = pickle.load(f)

#예측 실행 함수
def run_predict(data) : 
  data = {
  '설비용량(MW)' : [data.mw], 
  '기온' : [data.temperature],
  '습도' : [data.humidity],
  '풍속' : [data.wind],
  '시도명' : [data.region], 
  'encoded_시도명' : 0 
  }
  #데이터프레임으로 데이터를 변환
  df = pd.DataFrame(data)

  new_df = df.copy()
  #시도명 인코딩
  new_df['encoded_시도명'] = le.transform(new_df['시도명'])

  #시도명 컬럼 삭제
  new_df.drop(columns='시도명', inplace=True)
  #우리가 전달한 데이터로 발전량을 예측
  predict_data = rf_model.predict(new_df)
  result = float(predict_data[0])
  return result


