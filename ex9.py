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