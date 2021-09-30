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
