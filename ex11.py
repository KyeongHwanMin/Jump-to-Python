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
# 260 에러의 원인
#class OMG :
#   def print() : self가 필요함.
#       print("Oh my god")
# mystock = OMG()
# mystock.print() #OMG.print(mystock)

#261 Stock 클래스 생성
#주식 종목에 대한 정보를 저장하는 Stock 클래스를 정의해보세요. 클래스는 속성과 메서드를 갖고 있지 않습니다.
# class Stock:
#     pass

#262 생성자
#Stock 클래스의 객체가 생성될 때 종목명과 종목코드를 입력 받을 수 있도록 생성자를 정의해보세요.
# class Stock:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
# 삼성 = Stock("삼성전자","005930")
# print(삼성.name)
# print(삼성.price)
#263 메서드
#객체에 종목명을 입력할 수 있는 set_name 메서드를 추가해보세요.
# class Stock:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#     def setname(self,name):
#         self.name = name
# a=Stock(None,None)
# a.setname("삼성전자")
# print(a.name)
#264 메서드
#객체에 종목코드를 입력할 수 있는 set_code 메서드를 추가해보세요.
# class Stock:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#     def setname(self,name):
#         self.name = name
#     def set_code(self,price):
#         self.price = price
# a=Stock(None,None)
# a.setname("삼성전자")

# 265 메서드
# 종목명과 종목코드를 리턴하는 get_name, get_code 메서드를 추가하세요. 해당 메서드를 사용하여 종목명과 종목코드를 얻고 이를 출력해보세요
# class Stock:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#     def get_name(self):
#         return "get메서드"+self.name
#     def get_code(self):
#         return "get메서드"+self.price
# 삼성 = Stock("삼성전자","005930")
# print(삼성.get_name())
# print(삼성.get_code())
# 266 객체의 속성값 업데이트
# 생성자에서 종목명, 종목코드, PER, PBR, 배당수익률을 입력 받을 수 있도록 생성자를 수정하세요. PER, PBR, 배당수익률은 float 타입입니다.
# class Stock:
#     def __init__(self,name,code,per,pbr,배당수익률):
#         self.name = name
#         self.code = code
#         self.per = per
#         self.pbr = pbr
#         self.배당수익률 = 배당수익률
#     def set_name(self,name):
#         self.name = name
#     def set_code(self,code):
#         self.code = code
#     def get_name(self):
#         return self.name
#     def get_code(self):
#         return self.code
# 267 객체 생성
# 266번에서 정의한 생성자를 통해 다음 정보를 갖는 객체를 생성해보세요.

# class Stock:
#     def __init__(self,name,code,per,pbr,배당수익률):
#         self.name = name
#         self.code = code
#         self.per = per
#         self.pbr = pbr
#         self.배당수익률 = 배당수익률
#     def set_name(self,name):
#         self.name = name
#     def set_code(self,code):
#         self.code = code
#     def get_name(self):
#         return self.name
#     def get_code(self):
#         return self.code
# 주식 = Stock("삼성전자","005930",15.79,1.33,2.83)
# print(주식.배당수익률)
# 268 객체의 속성 수정
# PER, PBR, 배당수익률은 변경될 수 있는 값입니다. 이 값을 변경할 때 사용하는 set_per, set_pbr, set_dividend 메서드를 추가하세요.

# class Stock:
#     def __init__(self,name,code,per,pbr,배당수익률):
#         self.name = name
#         self.code = code
#         self.per = per
#         self.pbr = pbr
#         self.배당수익률 = 배당수익률
#     def set_name(self,name):
#         self.name = name
#     def set_code(self,code):
#         self.code = code
#     def get_name(self):
#         return self.name
#     def get_code(self):
#         return self.code
#     def set_per(self,per):
#         self.per = per
#     def set_pbr(self,pbr):
#         self.pbr = pbr
#     def set_dividend(self,dividend):
#         self.set_dividend = dividend

# 객체의 속성 수정
# 269번에서 생성한 객체에 set_per 메서드를 호출하여 per 값을 12.75로 수정해보세요.

class Stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
삼성.set_per(12.75)
print(삼성.per)

# 여러 종목의 객체 생성
# 아래의 표를 참조하여 3종목에 대해 객체를 생성하고 이를 파이썬 리스트에 저장하세요. 파이썬 리스트에 저장된 각 종목에 대해 for 루프를 통해 종목코드와 PER을 출력해보세요.
# 삼성 = Stock("삼성전자","005930",15.79,1.33,2.83)
# 현대차 = Stock("현대차","005380",8.70,0.35,4.27)
# LG전자 = Stock("LG전자","066570",317.34,0.69,1.37)
# list =[삼성,현대차,LG전자]
# for i in range(len(list)):
#     print(f"종목코드 : {list[i].name}, PER : {list[i].per}")
종목 = []

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)

for i in 종목:
    print(i.code, i.per)        # i-> Stock 클래스의 객체를 바인딩하기 때문
