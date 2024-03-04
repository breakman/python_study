#산술 연산자

print(1+1) # 덧셈
print(3-2) # 뺄셈
print(5*3) # 곱셈
print(6/3) # 나누기
print(2**3) # 제곱
print(5%3) # 나머지
print(5//3) # 몫
print(type(5/3))

#비교 연산자

print(10 > 3) # True 
print(4 >= 7) # False
print(10 < 3) # False 
print(4 <= 7) # True ,cls - terminal 초기화 입력

print(3 == 3) # == 같다 True
print(3 == 4) # False

print(1 != 3) # != 같지 않다 True
print(not(1 != 3)) #not 이 같이 쓰였으니 False

#논리 연산자

print((3>0) and (3 < 5)) # AND 그리고 모두 참이어야 함.True
print((3>0) & (3 < 5)) # & 그리고 True
print((3 > 0) or (3 > 5)) # OR 또는 하나만 참이여도 됨.True
print((3 > 0) | (3 > 5)) # | 또는 True

print(5 > 4 > 3) #True
print(5 > 3 > 7) #False