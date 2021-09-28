# 07 분기문 if문
# 101
# 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?
# boolean
# 102
print(3 == 5)
# 103
print(3 < 5)
# 104
x = 4
print(1 < x < 5)
# 105
print((3 == 3) and (4 != 3))
# 106
print(3 >= 4)
# 107
if 4 < 3:
    print("Hello")
# 108
if 4 < 3:
    print("hello")
else:
    print("Hi")
# 109
if True:
    print("1")
    print("2")
else:
    print("3")
print("4")
# 110
if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")
# 111 사용자로부터 입력받은 문자열을 두 번 출력하라.
# 아래는 사용자가 "안녕하세요"를 입력한 경우의 출력 결과이다.
# user = input("입력:") # 입력 메서드(scanner.in())
# print(user*2)
# 112 사용자로부터 하나의 숫자를 입력받고,
# 입력 받은 숫자에 10을 더해 출력하라.
# user = input("하나의 숫자를 입력 하세요 : ")
# print(int(user) + 10)
# 113 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.
# user = input("숫자를 입력하세요. :")
# if int(user) % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")
# 114 사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력하라.
# 단 사용자가 입력한 값과 20을 더한 계산 값이 255를 초과하는 경우 255를 출력해야 한다.
# user = input("입력값: ")
# if int(user)+20 < 255:
#     print(int(user)+20)
# else:
#     print("출력 값 : ",255)
# 115 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라.
# 단 출력 값의 범위는 0~255이다. 예를 들어 결괏값이 0보다 작은 값이되는 경우 0을 출력하고 255보다 큰 값이 되는 경우 255를 출력해야 한다.
# user = input("입력값 :")
# num = int(user) - 20
# if num < 0:
#     print(0)
# elif num > 255:
#     print(255)
# else:
#     print(num)
# 116 사용자로부터 입력 받은 시간이 정각인지 판별하라.
# user = input("현재시간 : ")
# time = user[3:]
# time=int(time)
# if time > 0:
#     print("정각이 아닙니다.")
# else:
#     print("정각 입니다.")
#  ##########################
# time = input("현재시간: ")
# if time[-2:] == "00":
#     print("정각 입니다.")
# else:
#     print("정각이 아닙니다.")
# 117 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라.
# 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# user = input("좋아하는 과일은? : ")
# fruit = ["사과", "포도", "홍시"]
# if user in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")
# 118 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이라면 '투자 경고 종목입니다'를 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# user = input("투자종목을 입력하시오. :")
# if user in warn_investment_list:
#     print("투자 경고 종목")
# else:
#     print("경고 종목 아님.")
# 119 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# user = input("제가 좋아하는 계절은 : ")
# if user in fruit:
#     print("정답")
# else:
#     print("땡")
# 120 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 값 (value)에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# user = input("좋아하는 과일은? :")
# if user in fruit.values():
#     print("정답")
# else:
#     print("오답")

# 121 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라.
# user = input("문자 입력 :")
# if user.islower():
#     print(user.upper())
# else:
#     print(user.lower())
# 122 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.
# score = input("score: ")
# score = int(score)
# if 81 <= score <= 100:
#     print("grade is A")
# elif 61 <= score <= 80:
#     print("grade is B")
# elif 41 <= score <= 60:
#     print("grade is C")
# elif 21 <= score <= 40:
#     print("grade is D")
# else:
#     print("grade is E")

# 123 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라. 각 통화별 환율은 다음과 같다. 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.
# user = input("입력 : ")
# 환율 = {"달러":1167 , "엔": 1.096, "유로":1268, "위안": 171}
# money, num = user.split()
# print(float(money) * 환율[num],"원")

# 124 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
# user1 =int(input("input number:"))
# user2 =int(input("input number2:"))
# user3 =int(input("input number3:"))
#
# if user1 > user2 and user1 >user3:
#     print(user1)
# elif user2 > user1 and user2 > user3:
#     print(user2)
# else:
#     print(user3)

# 125 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.
# user = input("휴대전화 번호 입력:")
# user = user.split("-")
# if user[0] == "011":
#     print("당신은 SKT 사용자 입니다.")
# elif user[0] == "016":
#     print("당신은 KT 사용자 입니다.")
# elif user[0] == "019":
#     print("당신은 LGU 사용자 입니다.")
# else:
#     print("알수없음")

# 126 우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다. 예를들어, 강북구의 경우 010, 011, 012 세 자리로 시작한다.
# 사용자로 부터 5자리 우편번호를 입력받고 구를 판별하라
# user = input("우편번호:")
# address = user[:3]
# if address in ["010","011","012"]:
#     print("강북구")
# elif address in ["013","014","015"]:
#     print("도봉구")
# else:
#     print("노원구")

# 127 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 1, 3은 남자 2, 4는 여자를 의미한다. 사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.
# user = input("주민등록번호: ")
# number = user.split("-")[1]
#
# if number[0] == '1' or number[0] == '3' :
#     print("남자")
# elif number[0] == '2' or number[0] == '4':
#     print("여자")
# else :
#     print("잘못입력")

# 128 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다. 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라
# 주민번호 = input("주민등록번호: ")
# 뒷자리 = 주민번호.split("-")[1]
# if 0 <= int(뒷자리[1:3]) <= 8:
#     print("서울입니다.")
# else:
#     print("서울이 아닙니다.")
# data = input("주민등록번호: ")
# b = data.split("-")[1]
# if b[1:3] in ['00','01','02','03','04','05','06','07','08']:
#     print("서울 입니다.")
# else :
#     print("서울이 아닙니다.")
# 129 주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다. 먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤 그 값을 전부 더한다. 연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.
# data = input("주민등록번호: ")
# data = data.replace("-","")
# # "\" 다음 줄로 연결된 다는 의미
# 계산1 = int(data[0]) *2 + int(data[1]) *3 + int(data[2]) *4 +\
#         int(data[3]) *5 + int(data[4]) *6 + int(data[5]) *7 +\
#         int(data[6]) *8 + int(data[7]) *9 + int(data[8]) *2 +\
#         int(data[9]) *3 + int(data[10]) *4 + int(data[11]) *5
# 계산1=계산1 % 11
# 계산2 = 11 - 계산1
# 계산2 =str(계산2)
# if data[-1] == 계산2[-1]:
#     print("유효")
# else :
#     print("유효하지 않음")

# 130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

open = float(btc['opening_price'])
high = float(btc['max_price'])
low = float(btc['min_price'])
diff = high - low # 변동폭

if(open+diff) > high:
    print("상승장")
else:
    print("하락장")

