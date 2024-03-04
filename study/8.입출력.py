# 표준 입출력

import sys
print("Python", "Java", sep=",", end="?") # sep ="," ,로 구분되는 구간에 내용 추가
print("무엇이 더 재밌을까요?") # end ="" 한줄에 바로, 문장의 끝부분을 해당 텍스트로 바꿔라.

print("Python","Java", file = sys.stdout) # file = sys.stdout 표준 출력으로 문장
print("Python","Java", file = sys.stderr) # stderr 표준 에러로 

# scores = {"수학": 0, "영어": 50, "코딩": 100} # 튜플 형태로 보냄
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust(a) 왼쪽에서 글자 a개 만큼의 공간에 대해 왼쪽정렬후 글자 표시
#     # rjust(a) 오른쪽에서 글자 a개 만큼의 공간을 확보한 뒤 오른쪽 정렬후 글자 표시 문자열만!!

# # 은행 대기순번표
# # 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3)) # zfill(a) a 만큼의 공간을 확보한 뒤 값을 집어 넣음.

# # 표준 입력
# answer = input("아무 값이나 입력하세요 : ") # input() 항상 문자열 형태로 저장됨.
# answer = 10
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")

# # 다양한 출력 포맷
'''
# # 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보 {0:' >10'} 빈 공간
# print("{0: >10}".format(500)) # 앞에 + 부호가 없을 시 - 만 표시
# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500)) # 앞에 + 부호가 있을 시 + - 표시
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500)) #{0:'_<10'} _
# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(10000000000))
# # 3자리 마다 콤마를 찍어주기 , +- 부호도 붙이기
# print("{0:+,}".format(10000000000))
# print("{0:+,}".format(-10000000000))
# # 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수도 확보, 빈 자리는 ^ 표시로 채우기 {0:^<+30,}
# print("{0:^<+30,}".format(1000000000000))
# # 소수점 출력 {0:f}
# print("{0:f}".format(5/3))
# # 소수점 특정 자리수 까지만 표시 {0:.af} (소수점 a+1째 자리에서 반올림)
# print("{0:.2f}".format(5/3))
'''
# 파일 입출력
'''
# score_file = open("score.txt", "w", encoding="utf8") # score.txt 라는 파일을 w 쓰기위한 목적으로 열고 encoding="utf8" 한글 정보
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close() # 열려 있는 파일을 닫아 주는 역할

# score_file = open("score.txt", "a", encoding="utf8") # "a" 이미 존재한 파일에 이어서 쓴다. append
# score_file.write("과학 : 80") # 줄바꿈이 없음
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") # "r" read 파일에 있는 내용을 읽는 용도
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # readline 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") # 파일이 몇 줄 인지 모를 때
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()
'''
# # pickle
'''
# import pickle
# # profile_file = open("profile.pickle", "wb") # w 'b' 바이너리 타입 정의
# # profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# # print(profile)
# # pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장
# # profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # 파일에 있는 내용을 가져와서 데이터 형태로 불러옴. file 에 있는 정보를 profile 에 불러오기
# print(profile)
# profile_file.close()
'''
# with  매번 close() 를 할 필요가 없음
'''
# import pickle

# # with open("profile.pickle", "rb") as profile_file:
# #     print(pickle.load(profile_file))

# # with open("study.txt", "w", encoding="utf8") as study_file:
# #     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())
'''