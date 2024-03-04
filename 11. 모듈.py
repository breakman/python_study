# 모듈 : 필요한 것들끼리 부품처럼 잘 만들어진 파일 // 모듈을 사용하려면? - 같은 경로에 있거나 파이썬 라이브러리에 있는 폴더 안에 있어야함.
'''
# import theater_module # import 를 활용해 모듈 사용
# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
# theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때

# import theater_module as mv # import ## as ## 별명으로 호출
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import * # //from random import * //모듈 안에 있는 모든것을 사용함.
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning # 명시적으로 어떤 함수를 가져올지 정의 가능
# price(4)
# price_morning(5)
# price_soldier(7)

from theater_module import price_soldier as price
price(5) # theater_module 의 price_soldier
'''
# 패키지
'''
# import travel.thailand # 패키지 사용시 ##.## 뒷부분은 항상 모듈이나 패키지, 즉 클래스나 함수는 직접 임포트 불가능.
# import travel.thailand.ThailandPackage XX 불가능
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage # from import 구문에서는 모듈이나 패키지, 클래스 함수를 모두 import 가능
# trip_to = ThailandPackage()
# trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()
'''
# __all__
'''
# from random import *
from travel import * # *을 쓴다는 것 travel이라는 패키지 안에 있는 모든 것을 가져오는 것 공개 범위를 설정해줘야 함.
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()
'''
# 모듈 직접 실행 : 모듈이 잘 작동하는지 테스트를 진행해야함.
'''
from travel import * 
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()
'''
# 패키지, 모듈 위치 확인
'''
from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()
import inspect
import random
print(inspect.getfile(random)) # inspect.getfile(#) 파일의 위치가 어디있는지 탐색
print(inspect.getfile(thailand))
'''
# pip install : pip install 패키지명, / pip install -- upgrade 패키지명 , 패키지 업데이트 / pip uninstall 패키지명, 패키지 삭제 /
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
'''
# 내장 함수 / import 없이 사용 가능한 함수
'''
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
#print(dir())
import random # 외장 함수
# print(dir())
# import pickle
# print(dir())

# print(dir(random)) # 랜덤 모듈 내에서 쓸 수 있는 함수.
# list = [1, 2, 3]
# print(dir(list)) # list 에서 쓸 수 있는 함수 표시.

name = "Jim"
print(dir(name))
'''
# 외장 함수 / import 를 직접 해야 사용 가능
'''
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py 인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
import os
# print(os.getcwd()) # 현재 디렉토리 표시

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder) # os.rmdir() 폴더 제거
#     print(folder, "폴더를 삭제하였습니다.")
# else: 
#     os.makedirs(folder) # os.makedirs 폴더 생성 
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir()) # glob 과 비슷하게 사용할 수 있음.

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
# print("오늘 날짜는 ", datetime.date.today()) # 2021-01-10

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은", today + td)
'''