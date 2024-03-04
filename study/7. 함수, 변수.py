# # 함수
'''
# def open_account():
#     print("새로운 계좌가 생성되었습니다. ")

# open_account() # 함수 호출'''

# # 전달값과 반환값
'''
# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money: # 잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance
# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission # 튜플형식으로 보냄.

# balance = 0 # 잔액
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))'''

# 기본값
'''# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \
#         .format(name, age, main_lang)) # \ enter 줄바꿈

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업.

def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \
        .format(name, age, main_lang))

profile("유재석")
profile("김태호")
'''
# # 키워드 값을 이용한 함수 호출
'''
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name ="유재석", main_lang = "파이썬", age = 20) # 키워드 값 입력을 통해 순서 없이 함수 호출 가능
# profile(main_lang ="자바", age = 25, name= "김태호")
'''
# 가변 인자
'''
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end= "") # end= " " 이 문장 출력 후 밑 문장 출력
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language): # *a 가변인자 서로 다른 개수의 값을 넣을 때 활용
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end= "") # end= " " 이 문장 출력 후 밑 문장 출력
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")
'''
# 지역변수, 전역변수 지역변수 : 함수 내에서만 사용 가능 함수 호출 후 사라짐, 전역변수 : 프로그램 내에서 어디서든 호출할 수 있음.
'''
gun = 10 # 전역변수

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용 'global a'
    # gun = 20 # 지역변수
    gun = gun - soldiers 
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
# checkpoint(2)
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))
'''