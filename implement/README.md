# 이것이 코딩 테스트다 - 4장 구현
- 아이디어를 코드로 바꾸는 구현
- 왕실의 나이트
- 게임 개발

## 1. 아이디어를 코드로 바꾸는 구현
- 코딩 테스트에서 구현이란 '머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정' 이다.
- **풀이를 떠올리기는 쉽지만 소스코드로 옮기기가 어려운 문제**
- 대체로 사소한 조건 설정이 많은 문제일수록 코드로 구현하기가 까다롭다.
- **완전탐색**: 모든 경우의 수를 주저 없이 다 계산하는 해결 방법
- **시뮬레이션**: 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행

#### 파이썬에서 리스트 크기(int 자료형)
| 데이터의 개수(리스트의 깊이) | 메모리사용량 |
| ---------------------------- | ------------ |
| 1,000                        | 약 4KB       |
| 1,000,000                    | 약 4MB       |
| 10,000,000                   | 약 40MB      |

### 채점환경

- 파이썬이 많이 느려서 수행 시간 제한을 2배로 적용하기도 함
- 시간 제한이 1초이고, 데이터 갯수가 100만 개인 문제라면 일반적으로 O(NlogN) 이내 풀어야함
- Pypy3가 python3보다 대부분 실행 속도가 더 빠르다