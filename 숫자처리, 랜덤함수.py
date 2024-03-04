# 숫자 처리 함수
'''print(abs(-5)) # 5 abs() 절댓값 함수
print(pow(4, 2)) # 4^2 pow() 제곱 함수
print(max(5 , 12)) # 12 max() 최댓값 함수 두 숫자 중 큰 값을 반환
print(min(5, 12)) # 5 min() 최솟값 함수 두 숫자 중 작은 값을 반환
print(round(3.14)) # 3 round() 반올림 함수
print(round(4.99)) # 5

 # math 라이브러리 사용 from math import *
from math import *
print(floor(4.99)) # 4 floor() 내림 함수
print(ceil(3.14)) # 4 ceil() 올림 함수
print(sqrt(16)) # 4 sqrt() 제곱근 함수'''

# 랜덤 함수 random 라이브러리 사용 from random import *
'''from math import *
from random import *

print(random()) # random() 0.0~ 1.0 미만의 임의의 값 생성
print(random()*10) # 0.0 ~ 10.0 미만의 임의의 값 생성 
print(int(random()*10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random()*10) + 1) # 1 ~ 10 이하의 임의의 값 생성
'''
# 로또 예제
from random import *
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성

print(randrange(1, 46)) # 1 ~ 45 이하의 임의의 값 생성 randrange(a, b) a부터 b 미만의 임의의 값 생성

print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성 randint(a, b) a부터 b 이하의 임의의 값 생성