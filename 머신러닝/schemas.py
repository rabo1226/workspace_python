#BaseModel 클래스를 임포트
#BaseModel 클래스는 자바의 DTO 역할에 맞게 설계된 클래스
from pydantic import BaseModel

#BaseModel 클래스를 상속하여 WeatherInput 클래스를 정의
class WeatherInput(BaseModel):
  mw : float
  temperature : float
  humidity : float
  wind : float
  region : str

#전달할 데이터
class PredictOutput(BaseModel): 
  predictData : float

  #java 식
  #class PrdictOutput extends BaseModel{
  # private float predictData;
  #}