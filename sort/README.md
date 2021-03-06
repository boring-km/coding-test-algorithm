# 이것이 코딩 테스트다 - 6장 정렬
- 1. 기준에 따라 데이터를 결정
- 2. 위에서 아래로
- 3. 성적이 낮은 순서로 학생 출력하기
- 4. 두 배열의 원소 교체

## 1. 기준에 따라 데이터를 정렬
- 선택 정렬
  - 데이터 중에서 가장 작은 데이터를 선택해 맨 앞 데이터와 바꾸고, <br>
  그다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복
  
- 삽입 정렬
  - 특정 데이터가 적절한 위치에 들어가기 전에 그 앞까지 데이터를 이미 정렬되어 있다고 가정 <br>
  앞의 숫자와 비교해서 크면 우측 작으면 좌측
  
- 퀵 정렬
  - 병합 정렬과 함께 빠름
  - 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다.
  - pivot 설정
  
- 계수 정렬
  - '데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때'만 사용 가능
  - 실수형 범위에서 사용 어려움
  - 값의 범위만큼 리스트 생성해서 그 값의 인덱스마다 값을 1씩 추가
  
### 1.1 파이썬에서 정렬 라이브러리
- 항상 최악에도 O(NlogN)
> 1. 풀 수 있는 문제: 단순히 정렬 기법을 아는지 물어보는 문제
> 2. 선택 정렬, 삽입 정렬, 퀵 정렬 등 원리를 알아야 푸는 문제
> 3. **퀵 정렬으로는 풀 수 없고 계수 정렬 등 다른 알고리즘을 사용하거나 기존 알고리즘의 구조적인 개선을 거쳐야하는 문제**

