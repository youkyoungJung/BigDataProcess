# BigDataProcess

* ## HW4: KNN-알고리즘을 통한 필기체인식 시스템


 ### 예제데이터를 갖고 주어진 데이터로 학습하여 결과 예측하기. 
- #### 제공한 예제 데이터 : trainingDigits 폴더 , testDigits 폴더


 1. trainingDigits 폴더 :  N_M.txt(N : 숫자, M : 데이터 ID) -파일 이름에 데이터의 라벨이 있음. 훈련데이터
 2. testDigits 폴더 : N_M.txt(N : 숫자, M : 데이터 ID)
 테스트 데이터. 이 폴더의 데이터를 이용하여 숫자 인식. 결과 도출 (인식한 결과와 실제 라벨을 확인하여 에러율 계산)


3. knn 알고리즘에서 k를 변화시키면서 에러율 계산하기.
4. 출력 규칙 :  k가 1일 때부터 20일때까지 에러율을 차례대로 출력한다. 숫자 20개가 차례대로 한줄에 한 숫자로 출력되며 소수점은 절사함.


- #### knn.py : def autoNorm - 정규화 함수,  def classify0 - 분류함수
- #### student20181013.py : def DirectoryToFileName - 디렉터리에서 파일 이름으로 접근하는 함수
                           
