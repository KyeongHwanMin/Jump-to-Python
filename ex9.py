#09 파이썬 함수
# 함수란 자주 사용하는 코드에 대한 이름표입니다. 변수가 어떤 값을 바인딩하는 것처럼 함수는 어떤 코드를 바인딩합니다.
# 201 "비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.
def print_coin():
    print("비트코인")

#202 201번에서 정의한 함수를 호출하라.
print_coin()
#203 201번에서 정의한 print_coin 함수를 100번호출하라.
for i in range(100):
    print_coin()
#204 "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.
def print_coins():
    for i in range(100):
        print("비트코인")
#205
# hello()
# def hello():
#     print("Hi")
# 함수 정의 되기전에 호출해서 오류 발생
#206
def message() :
    print("A")
    print("B")
message()
print("C")
message()
#207
print("A")
def message() :
    print("B")
print("C")
message()
#208
print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2()
#209
def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()
#210
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()
#211
def 함수(문자열) :
    print(문자열)

함수("안녕")
함수("Hi")
#212
def 함수(a, b) :
    print(a + b)

함수(3, 4)
함수(7, 8)
#213
# def 함수(문자열) :
#     print(문자열)
# 함수()
# 함수에 정의와 다르게 함수를 호출하고 있다. 함수를 호출할 때 하나의 파라미터를 입력해야한다.
#214
# def 함수(a, b) :
#     print(a + b)
# 함수("안녕", 3)
# 정의된 함수는 같은 타입의 두 개의 값을 입력 받아 덧셈 연산을 적용하려는 의도로 설계됐습니다. 하지만 함수를 호출 할때 문자열과 숫자를 입력해서 문자열과 숫자는 더할 수 없다는 에러가 발생합니다
#215
def print_with_smile(문자열):
    print(문자열+":D")
print_with_smile("a")
#216 215에서 정의한 함수를 호출하라. 파라미터는 "안녕하세요"로 입력하라.
print_with_smile("안녕하세요")
#217 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.
def print_upper_price(price):
    print(price*1.3)
#218 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.
def print_sum(a,b):
    print(a+b)
print_sum(3,5)
#219 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.
def print_arithmetic_operation(a,b):
    print(a+b)
    print(a - b)
    print(a * b)
    print(a / b)
print_arithmetic_operation(10,20)
#220 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.
def print_max(a,b,c):
    if a > b :
        if a > c :
            print(a)
    if b > a :
        if b > c :
            print(b)
    if c > a:
        if c > b :
            print(c)
print_max(10,20,30)
def print_max1(a,b,c):
    print(max(a,b,c))
print_max1(10,20,30)

#221 입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의하라.
def print_reverse(string):
    print(string[::-1])
print_reverse("문자")
#222 성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의하라.
def print_score(list):
    print(sum(list)/len(list))
print_score([1,2,3])
#223 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.
def print_even(list):
    for i in list:
        if i % 2 == 0:
            print(i)
print_even([1,3,2,10,12,11,15])
#224 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.
def print_keys(dict):
    for i in dict.keys():
        print(i)
print_keys({"이름":"길말똥","나이":30,"성별":0})
#225 my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
def print_value_by_key(a,b):
    print(my_dict[b])
print_value_by_key(my_dict,"10/26")
#226 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.
def print_5xn(a):
    times = len(a)/5
    times=int(times+0.9) # 11/5=2.1+0.9=3.0
    for i in range(times):     #i->0, 1
       print(a[5*i:5*i+5])    #[0:5],[5:10]

print_5xn("아이엠어보이유알어걸추가")
#227 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.
import math
def printmxn(data,num):
    #횟수를 계산
    tiems = len(data)/num
    times = math.ceil(tiems) # 올림 함수

    for i in range(times):
        print(data[i*num : (i+1)*num]) # num=3, i=0, [0:3]
printmxn("아이엠어보이유알어걸", 3)
#228 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.
def calc_monthly_salary(annual_salary):
    money = int(annual_salary / 12)
    print(money)

calc_monthly_salary(12000000)
#229
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)
#230
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)