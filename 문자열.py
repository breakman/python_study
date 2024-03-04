# 문자열 
'''sentence = '나는 소년입니다' # 'a' 문자열
print(sentence)
sentence2 = "파이썬은 쉬워요" # "a" 문자열
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은  쉬워요
""" # """a""" 여러줄 문자열
print(sentence3)
'''

# 슬라이싱
'''jumin = "990121-1234567"

print("성별 : " + jumin[7]) # 배열은 0부터
print("연 : " + jumin[0:2]) # 0 부터 2 직전까지 (0 , 1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
print("뒤 7자리(뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번재부터 끝까지
'''

# 문자열 처리 함수
'''python = "Python is Amazing"
print(python.lower()) # a.lower() 소문자 출력 함수
print(python.upper()) # a.upper() 대문자 출력 함수
print(python[0].isupper()) # a[i].isupper() 대문자 판단 함수 출력 결과는 True or False
print(len(python)) # len() 문자열 길이 측정 함수
print(python.replace("Python", "Java")) # a.replace("b", "c") b라는 문자열을 찾은 뒤 c 로 치환

index = python.index("n") # a.index("b") 해당하는 문자가 몇번째 인덱스에 있는지 정수출력
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java")) # 찾는 값이 없을 땐 -1 반환
# print(python.index("Java")) # 찾는 값이 없을 땐 오류를 낸 뒤 프로그램 종료

print(python.count("n")) # 해당하는 값이 몇번 나왔는지 판단'''

# 문자열 포맷
'''# print("a" + "b")
# print("a", "b")
# # 방법 1
# print("나는 %d살입니다." % 20) # %d : 정수
# print("나는 %s을 좋아해요." % "파이썬") # %s : 문자열
# print("Apple 은 %c로 시작해요." % "A") # $c : 한 글자
# %s : 모든 형태 가능
# print("나는 %s살입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2 .format()
# print("나는 {}살 입니다." .format(20))
# print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))

# 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간")) # 변수 선언 순서 상관없음

# 방법 4 (v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")'''

# 탈출 문자

# \n 줄바꿈
# print("백문이 불여일견\n백견이 불여일타") 
# print('저는 "나도 코딩"입니다.') # 순서를 혼합.

# \" \' 문장 내에서 따옴표 기능
# print("저는 \"나도코딩\"입니다.")

# \\ : 문장 내에서 \ 로 출력
# print("C:\\Users\\dlwns\\Desktop\\pythonWorkspace>")

# \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t :  탭
print("Red\tApple")