# 파이썬 클래스
# 파이썬 클래스는 타입을 만들어내는 도구입니다. int, float, str과 같이 여러분의 새로운 타입을 만들 수 있습니다.
# 251
# 클래스, 객체, 인스턴스
# 클래스, 객체, 인스턴스에 대해 설명해봅시다.

# 클래스 : 붕어빵 틀과 같은 것, 객체나 인스턴스의 설계도
# 객체 object == 인스턴스

# 252 클래스 정의
# 비어있는 사람 (Human) 클래스를 "정의" 해보세요.
# class Human:  # 사용자 정의 클래스 시작은 대문자
#     pass

# 253 인스턴스 생성
# 사람 (Human) 클래스의 인스턴스를 "생성" 하고 이를 areum 변수로 바인딩해보세요.
class Human:
    pass


areum = Human()


# 254 클래스 생성자-1
# 사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가하세요.
class Human:
    def __init__(self):  # 생성자
        print("응애응애")


areum = Human()


# 255 클래스 생성자-2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


areum = Human("아름", 25, "여자")
print(areum)
print(areum.sex)
print(areum.age)
print(areum.name)


# 256 인스턴스 속성에 접근
# 255에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요. 인스턴스 변수에 접근하여 값을 출력하면 됩니다.
# class Human:
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
# areum = Human("아름","25","여자")
# print(areum.age)
# 클래스 메소드 - 1
# 사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print(f"이름 :{self.name}, 나이 : {self.age}, 성별 : {self.sex}")

areum = Human("아름", 25, "여자")
areum.who() # Human.who(areum)
# 258 클래스 메소드 - 2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


areum = Human("불명", "미상", "모름")
areum.who()      # Human.who(areum)

areum.setInfo("아름", 25, "여자")
areum.who()      # Human.who(areum)
# 클래스 소멸자
# 사람 (human) 클래스에 "나의 죽음을 알리지 말라"를 출력하는 소멸자를 추가하세요.
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        print("나의 죽음을 알리지마라")

    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("아름", 25, "여자")
del(areum)
# 에러의 원인
#class OMG :
#   def print() : self가 필요함.
#       print("Oh my god")
# mystock = OMG()
# mystock.print() #OMG.print(mystock)
