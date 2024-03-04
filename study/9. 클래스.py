# 클래스 //붕어빵 틀
'''
# # 마린 : 공격 유닛, 군인. 총을 쓸 수 있음.

# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있음, 일반 모드 / 시즈모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(\
#         name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank_name, "1시", tank2_damage)

# class Unit:
#     def __init__(self, name, hp, damage): # __init__ 생성자 
#         self.name = name # 멤버 변수 self.name 클래스 내에서 정의 된 변수 
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)
# # marine3 = Unit("마린", 40) # 매개변수 만큼 갯수를 맞춰야 함.

# # 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # a.멤버 변수 이름

# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True # 객체에 외부에서 추가로 변수를 만들 수 있음.

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
'''
# # 메소드
'''
# 일반 유닛
class Unit:
    def __init__(self, name, hp, damage): # __init__ 생성자 
        self.name = name # 멤버 변수 self.name 클래스 내에서 정의 된 변수 
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):  
        self.name = name  # self x - name 위에서 전달받은 인자를 그대로 씀
        self.hp = hp
        self.damage = damage
    
    def attack(self, location): # 클래스 내에서 메소드 앞에는 무조건 self 를 붙임 # 공격하는 함수
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage)) # self.name 자기 자신에 있는 멤버변수의 값을 씀. location 전달 받은 값을 씀.
    
    def damaged(self, damage): # 공격 받는 함수
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)
'''
# # 상속, 다중 상속
'''
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed): # __init__ 생성자 
        self.name = name # 멤버 변수 self.name, 클래스 내에서 정의 된 변수 
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit): # 상속 asd(상속 받을 클래스)
    def __init__(self, name, hp, speed, damage):  
        Unit.__init__(self, name, hp, speed) # 이름과 체력을 받음.
        self.damage = damage
    
    def attack(self, location): # 클래스 내에서 메소드 앞에는 무조건 self 를 붙임 # 공격하는 함수
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage)) # self.name 자기 자신에 있는 멤버변수의 값을 씀. location 전달 받은 값을 씀.
    
    def damaged(self, damage): # 공격 받는 함수
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기.

# 날 수 있는 기능을 가진 클래스
class Flyable :
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed # 멤버 변수 초기화
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

# # 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")
'''
# # 메소드 오버라이딩 자식 클래스에서 정의한 메소드를 쓸 때 사용

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed): # __init__ 생성자 
        self.name = name # 멤버 변수 self.name, 클래스 내에서 정의 된 변수 
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit): # 상속 asd(상속 받을 클래스)
    def __init__(self, name, hp, speed, damage):  
        Unit.__init__(self, name, hp, speed) # 이름과 체력을 받음.
        self.damage = damage
    
    def attack(self, location): # 클래스 내에서 메소드 앞에는 무조건 self 를 붙임 # 공격하는 함수
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage)) # self.name 자기 자신에 있는 멤버변수의 값을 씀. location 전달 받은 값을 씀.
    
    def damaged(self, damage): # 공격 받는 함수
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기.

# 날 수 있는 기능을 가진 클래스
class Flyable :
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed # 멤버 변수 초기화
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location): # 메소드 오버라이딩 똑같은 함수 재정의
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
'''
vulture = AttackUnit("벌쳐", 80, 10, 20)

battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("9시")
'''
# # pass : 그냥 넘어감
'''
# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass 

game_start()
game_over()
'''
# # super
'''
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # super 는 괄호를 붙이고 self 는 없이 씀.
        self.location = location  # super 다중 상속때 문제 발생 순서상 먼저 상속받은 class 만 init 함수 호출. 하나하나 초기화를 해야함.
'''