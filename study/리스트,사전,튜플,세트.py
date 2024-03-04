# 리스트 [] 순서를 가지는 객체의 집합
'''
# # 지하철 칸별로 10명,20명,30명

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# # 조세호씨가 몇 번째 칸에 타고 있는가?

# print(subway.index("조세호"))

# # 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하") #append() 함수
# print(subway)

# # 정형돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1, "정형돈") #insert(1, b) 함수
# print(subway)

# # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)

# # 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# # 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort() # .sort() 오름차순 정렬
# print(num_list)

# # 순서 뒤집기 가능
# num_list.reverse() # .reverse() 내림차순 정렬
# print(num_list)

# # 모두 지우기
# num_list.clear() # .clear() 모두 지우기
# print(num_list)

# # 다양한 자료형 함께 사용
# num_list = [5,2,4,3,1]
# mix_list = ["조세호", 20, True]
# # print(mix_list)

# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)
'''

# 사전 dictionary {} key 와  value 형태로 구성됨. key에 대한 중복 x
'''cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3]) # [a] 형태로 출력
print(cabinet[100])

print(cabinet.get(3)) # .get(a) 로도 출력 가능
print(cabinet[5]) # 오류 후 프로그램 종료
print(cabinet.get(5)) # None 출력
print(cabinet.get(5, "사용 가능"))

print(3 in cabinet) # True : in 을 활용해서 사전 자료형에 값이 있는지 확인 가능

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국" # 이미 값이 존재할 경우 업데이트
cabinet["C-20"] = "조세호" 
print(cabinet)

# 나간 손님
del cabinet["A-3"] 
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)'''

# 튜플 () / 리스트와 다르게 내용 변경 x 리스트 보단 속도가 빠름.
'''menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)'''

# 집합 (set) {} 중복 x, 순서 x 값만 나열
my_set = {1,2,3,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 도 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java 를 잊어버린 사람
java.remove("김태호")
print(java)