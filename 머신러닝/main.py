#FastAPI 사용을 위해 라이브러리 설치
#pip install fastapi uvicorn

from fastapi import FastAPI
import uvicorn
from schemas import WeatherInput, PredictOutput
from service import run_predict

app = FastAPI()

##############################
@app.post('/test-1')
def test1(data : WeatherInput) :
  #매개변수로 전달받은 데이터 확인
  print(f'전달받은 데이터 => {data}')
  #발전량 예측
  predict_data = run_predict(data)
  return PredictOutput(predictData=predict_data)

#java식 PredictOutput PredictOutput = new PredictOutput() 디폴트 생성자 -> PredictOutput()

@app.get('/test-2')
def test1() :
  result = {
    'stuNum' : 1,
    'stuName' : 'kim',
    'score' : 80
  }
  return result

##############################
if __name__ == '__main__' : 
  uvicorn.run(app)