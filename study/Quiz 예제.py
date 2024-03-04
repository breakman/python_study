# # 1번
'''# from random import *
# date = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월", str(date),"일로 선정되었습니다.")'''

# # 2번
'''# # site_address = "http://youtube.com"
# # last_3 = site_address[7:10]
# # count = len(site_address[7:14])
# # e_count = site_address[7:14].count("e")
# # print("생선된 비밀번호 : " +last_3 + str(count) + str(e_count) + "!")

# url = "http://youtube.com"
# my_str = url.replace("http://", "")
# my_str = my_str[:my_str.index(".")]
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0} 의 비밀번호는 {1} 입니다." .format(url, password))'''

# # 3번
'''# from random import *
# # 내가 한 방법
# # users = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# # print(users)
# # shuffle(users)
# # list_1 = sample(users, 1)
# # print(list_1)
# # users.remove(list_1[0])
# # print(users)
# # list_2 = sample(users, 3)
# # print("-- 당첨자 발표 --\n치킨 당첨자 : " + str(list_1) + "\n" + "커피 당첨자 : " + str(list_2) + "\n" + "-- 축하합니다 --")

# # 정답
# users = list(range(1,21))
# shuffle(users)
# winners = sample(users, 4)
# print(" -- 당첨자 발표 -- ")
# print(" 치킨 당첨자 : {0}".format(winners[0]))
# print(" 커피 당첨자 : {0}".format(winners[1:]))
# print(" -- 축하 합니다 -- ")'''

# # 4번 복습 필요 !!
'''# # 50명의 승객과 매칭 기회가 있을 떄, 총 탑승 승객 수를 구하는 프로그램 작성
# from random import *
# count = 0
# for i in range(1, 51):
#     time = randrange(5, 51)
#     if 5 <= time <= 15:
#         print("[O]{0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         count += 1
#     else :
#         print("[ ]{0}번째 손님 (소요시간 : {1}분)".format(i, time))
# print("총 탑승 승객 {0} 명".format(count))'''

'''# from random import *
# count = 0
# for i in range(1, 51):
#     time = randrange(5, 51)
#     if 5 <= time <= 15 :
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         count += 1
#     else :
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
# print("총 탑승 승객 : {0} 명".format(count))'''

# # 5번 복습 !!
'''
# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21

# height = 175 # cm 단위
# gender = "남자"
# weight = round(std_weight(height/100, gender), 2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
'''

# 6번 복습!!
'''
# # for i in range(1, 51):
# #     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_files:
# #         report_files.write("- {0} 주차 주간보고 -".format(i))
# #         report_files.write("\n 부서 : ")
# #         report_files.write("\n 이름 : ")
# #         report_files.write("\n 업무 요약 : ")
# for i in range(1, 51):
#     with open(str(i) + "주차.txt", "r", encoding="utf8") as report_files:
#         print(report_files.read())
'''

# 7번
'''
# 부동산 프로그램 작성. 
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

house = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")
house.append(house1)
house.append(house2)
house.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(house)))
for hou in house:
    hou.show_detail()
'''
# 8번 예외 처리 코드 예제
'''
# 조건 1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는  ValueError 로 처리
#          출력 메시지 : "잘못된 값을 입력하였습니다."
# 조건 2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#          치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#          출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."


class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg
chicken = 10
waiting = 1
while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        oder = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if oder > chicken:
            print("재료가 부족합니다.")
        elif oder <= 0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
                .format(waiting, oder))
            waiting += 1
            chicken -= oder
            
        if chicken <= 0:
            raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")
            
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError as err:
        print(err)
        break
'''
# 9번 퀴즈 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

# 조건 : 모듈 파일명은 byme.py 로 작성

import byme
byme.sign()