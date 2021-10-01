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
import random


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
# 종목 = []
#
# 삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# 현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
# LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)
#
# 종목.append(삼성)
# 종목.append(현대차)
# 종목.append(LG전자)
#
# for i in 종목:
#     print(i.code, i.per)        # i-> Stock 클래스의 객체를 바인딩하기 때문

# 271 Account 클래스
# 은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다. Account 클래스를 생성한 후 생성자를 구현해보세요. 생성자에서는 예금주와 초기 잔액만 입력 받습니다. 은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.
import random
# class Account:
#
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#         self.bank = "SC은행"
#         num1 = random.randint(0,999)
#         num2 = random.randint(0,99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account_number = num1 +'-' +num2 +'-' +num3
#
# kim = Account("김민수",100)
# print(kim.name)
# print(kim.price)
# print(kim.bank)
# print(kim.account_number)

# 클래스 변수
# 클래스 변수를 사용해서 Account 클래스로부터 생성된 계좌 객체의 개수를 저장하세요.

import random

# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#
#         Account.account_count += 1
#
#
# kim = Account("김민수", 100)
# print(Account.account_count)
# lee = Account("이민수", 100)
# print(Account.account_count)
#
# # 클래스 변수 출력
# # Account 클래스로부터 생성된 계좌의 개수를 출력하는 get_account_num() 메서드를 추가하세
# import random
#
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#         Account.account_count +=1
#
#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)     # Account.account_count
#
#
# kim = Account("김민수", 100)
# lee = Account("이민수", 100)
# kim.get_account_num() # Account.get_account_num(kim)

# 274 입금 메서드
# Account 클래스에 입금을 위한 deposit 메서드를 추가하세요. 입금은 최소 1원 이상만 가능합니다.
# import random
#
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#         Account.account_count +=1
#
#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)     # Account.account_count
#
#     def deposit(self, amount):
#         if amount >= 1:
#             self.balance += amount
# 275 Account 클래스에 출금을 위한 withdraw 메서드를 추가하세요. 출금은 계좌의 잔고 이상으로 출금할 수는 없습니다.
import random

# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#         Account.account_count += 1
#
#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)  # Account.account_count
#
#     def deposit(self, amount):
#         if amount >= 1:
#             self.balance += amount
#
#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.balance -= amount
#
# k = Account("kim", 100)
# k.deposit(100)
# k.withdraw(90)
# print(k.balance)
# 276 정보 출력 메서드
# Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를 추가하세요. 잔고는 세자리마다 쉼표를 출력하세요.
# import random
#
#
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#         Account.account_count += 1
#
#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)  # Account.account_count
#
#     def deposit(self, amount):
#         if amount >= 1:
#             self.balance += amount
#
#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.balance -= amount
#
#     def display_info(self):
#         print("은행이름: ", self.bank)
#         print("예금주: ", self.name)
#         print("계좌번호: ", self.account_number)
#         print("잔고: ", self.balance)
#
#
# p = Account("파이썬", 10000)
# p.display_info()

#277 이자 지급하기
#입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 코드를 변경해보세요.
# import random
#
#
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.deposit_count = 0
#
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#         Account.account_count += 1
#
#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)  # Account.account_count
#
#     def deposit(self, amount):
#         if amount >= 1:
#             self.balance += amount
#
#             self.deposit_count += 1
#             if self.deposit_count % 5 == 0:         # 5, 10, 15
#                 # 이자 지금
#                 self.balance = (self.balance * 1.01)
#
#
#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.balance -= amount
#
#     def display_info(self):
#         print("은행이름: ", self.bank)
#         print("예금주: ", self.name)
#         print("계좌번호: ", self.account_number)
#         print("잔고: ", self.balance)
#
# p = Account("파이썬", 10000)
# p.deposit(10000)
# p.deposit(10000)
# p.deposit(10000)
# p.deposit(5000)
# p.deposit(5000)
# print(p.balance)
# 278 여러 객체 생성
# Account 클래스로부터 3개 이상 인스턴스를 생성하고 생성된 인스턴스를 리스트에 저장해보세요.
# import random
#
#
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.deposit_count = 0
#
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#         Account.account_count += 1
#
#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)  # Account.account_count
#
#     def deposit(self, amount):
#         if amount >= 1:
#             self.balance += amount
#
#             self.deposit_count += 1
#             if self.deposit_count % 5 == 0:         # 5, 10, 15
#                 # 이자 지금
#                 self.balance = (self.balance * 1.01)
#
#
#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.balance -= amount
#
#     def display_info(self):
#         print("은행이름: ", self.bank)
#         print("예금주: ", self.name)
#         print("계좌번호: ", self.account_number)
#         print("잔고: ", self.balance)
#
# data = []
# k = Account("KIM", 10000000)
# l = Account("LEE", 10000)
# p = Account("PARK", 10000)
#
# data.append(k)
# data.append(l)
# data.append(p)
#
# print(data)
# 279 객체 순회
# 반복문을 통해 리스트에 있는 객체를 순회하면서 잔고가 100만원 이상인 고객의 정보만 출력하세요.
# import random
#
#
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.deposit_count = 0
#
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#         Account.account_count += 1
#
#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)  # Account.account_count
#
#     def deposit(self, amount):
#         if amount >= 1:
#             self.balance += amount
#
#             self.deposit_count += 1
#             if self.deposit_count % 5 == 0:         # 5, 10, 15
#                 # 이자 지금
#                 self.balance = (self.balance * 1.01)
#
#
#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.balance -= amount
#
#     def display_info(self):
#         print("은행이름: ", self.bank)
#         print("예금주: ", self.name)
#         print("계좌번호: ", self.account_number)
#         print("잔고: ", self.balance)
#
# data = []
# k = Account("KIM", 10000000)
# l = Account("LEE", 10000)
# p = Account("PARK", 10000)
# data.append(k)
# data.append(l)
# data.append(p)
#
# for c in data:
#     if c.balance >= 1000000:
#         c.display_info()
#280 입출금 내역
#입금과 출금 내역이 기록되도록 코드를 업데이트 하세요. 입금 내역과 출금 내역을 출력하는 deposit_history와 withdraw_history 메서드를 추가하세요.
# import random
#
#
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.deposit_count = 0
#         self.deposit_log = []
#         self.withdraw_log = []
#
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#         Account.account_count += 1
#
#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)  # Account.account_count
#
#     def deposit(self, amount):
#         if amount >= 1:
#             self.deposit_log.append(amount)
#             self.balance += amount
#
#             self.deposit_count += 1
#             if self.deposit_count % 5 == 0:         # 5, 10, 15
#                 # 이자 지금
#                 self.balance = (self.balance * 1.01)
#
#
#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.withdraw_log.append(amount)
#             self.balance -= amount
#
#     def display_info(self):
#         print("은행이름: ", self.bank)
#         print("예금주: ", self.name)
#         print("계좌번호: ", self.account_number)
#         print("잔고: ", self.balance)
#
#     def withdraw_history(self):
#         for amount in self.withdraw_log:
#             print(amount)
#
#     def deposit_history(self):
#         for amount in self.deposit_log:
#             print(amount)
#
#
# k = Account("Kim", 1000)
# k.deposit(100)
# k.deposit(200)
# k.deposit(300)
# k.deposit_history()
#
# k.withdraw(100)
# k.withdraw(200)
# k.withdraw_history()

# 281 클래스 정의
# class 차:
#     def __init__(self,바퀴,가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
#
# car = 차(2,100)
# print("----")
# print(car.바퀴)
# print(car.가격)

# 282 클래스 상속
# 차 클래스를 상속받은 자전차 클래스를 정의하세요.
# class 차:
#     def __init__(self,바퀴,가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
# class 자전차(차):
#     pass

# 283 클래스 상속
# 다음 코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.
# class 차:
#     def __init__(self,바퀴,가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
# class 자전차(차):
#     def __init__(self,바퀴,가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
#
# bicycle = 자전차(2,100)
# print(bicycle.가격)

# 284 클래스 상속
# 다음 코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.
# class 차:
#     def __init__(self,바퀴,가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
# class 자전차(차):
#     def __init__(self,바퀴,가격,구동계):
#         super().__init__(바퀴,가격)
#         self.구동계 = 구동계
# bicycle = 자전차(2,100,"시마노")
# print(bicycle.구동계)
# print(bicycle.바퀴)
# # 클래스 상속
# # 다음 코드가 동작하도록 차 클래스를 상속받는 자동차 클래스를 정의하세요.
# class 차:
#     def __init__(self,바퀴,가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
# class 자전차(차):
#     def __init__(self,바퀴,가격,구동계):
#         super().__init__(바퀴,가격)
#         self.구동계 = 구동계
# class 자동차(차):
#     def __init__(self,바퀴,가격):
#         super().__init__(바퀴,가격)
#
#     def 정보(self):
#         print(f"바퀴수 : {self.바퀴}")
#         print(f"가격 : {self.가격}")
# car = 자동차(4,1000)
# car.정보()
# 부모 클래스 생성자 호출
class 차:
    def __init__(self,바퀴,가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

    def 정보(self):
        print("바퀴수 : ", self.바퀴)
        print("가격 : ", self.가격)
class 자전차(차):
    def __init__(self,바퀴,가격,구동계):
        super().__init__(바퀴,가격)

class 자동차(차):
    def __init__(self,바퀴,가격):
        super().__init__(바퀴,가격)

    def 정보(self):
        print(f"바퀴수 : {self.바퀴}")
        print(f"가격 : {self.가격}")
bicycle = 자전차(2,100,"시마노")
bicycle.정보()

# 287 부모 클래스 메서드 호출
# 자전차의 정보() 메서드로 구동계 정보까지 출력하도록 수정해보세요.
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

    def 정보(self):
        print("바퀴수 ", self.바퀴)
        print("가격 ", self.가격)

class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)

class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계
    def 정보(self):
        super().정보
        print("바퀴수 : ",self.구동계)
bicycle = 자전차(2,100,"시마노")
bicycle.정보()
#288 메서드 오버라이딩
class 부모:
    def 호출(self):
        print("부모호출")

class 자식(부모):
    def 호출(self):
        print("자식호출")


나 = 자식()
나.호출()
# 289 생성자
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
나 = 자식()
# 290 부모클래스 생성자 호출
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()