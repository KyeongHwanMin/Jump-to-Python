# 08 파이썬
# 131 ~ 140
# 131
과일 = ["사과","귤","수박"]
for 변수 in 과일:
    print(변수)
#132
과일 = ["사과","귤","수박"]
for 변수 in 과일:
    print("###")
#기초문법 배우기-1에서 for문의 핵심은 "들여쓰기된 코드가 자료구조에 저장된 데이터 개수만큼 반복된다"라고 설명했습니다. 과일 = ["사과", "귤", "수박"] 에는 세 개의 데이터가 저장돼 있으므로 들여쓰기된 print("####")코드가 세 번 실행됩니다.
#133
for 변수 in ["A","B","C"]:
    print(변수)
#134
for 변수 in ["A","B","C"]:
    print("출력:",변수)
#135
for 변수 in ["A","B","C"]:
    b = 변수.lower()
    print("변환:",b)
#136
for 변수 in[10,20,30]:
    print(변수)
#137
for a in [10,20,30]:
    print(a)
#138
for 변수 in [10,20,30]:
    print(변수,"\n-----")
#139
print("++++")
for 변수 in [10,20,30]:
    print("변수")
#140
for 변수 in ["1","2","3","4","5"]:
    print("-------")
#141 다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 for 문을 사용해서 화면에 출력하라. 단 부가세는 10원으로 가정한다.
리스트 = [100,200,300]
for 변수 in 리스트:
    print(변수+10)
#142
리스트 = ["김밥","라면","튀김"]
for 메뉴 in 리스트 :
    print("오늘의 메뉴 : ", 메뉴)
#143
리스트 = ["sk하이닉스","삼성전자","LG전자"]
for 변수 in 리스트:
    print(len(변수))
#144
리스트 = ['dog','cat','parrot']
for 변수 in 리스트:
    print(변수,len(변수))
#145
리스트 = ['dog','cat','parrot']
for 변수 in 리스트:
    print(변수[0])
#146
리스트 = [1,2,3]
for a in 리스트:
    print('3 x',a)
#147
리스트 =[1,2,3]
for a in 리스트:
    print('3 x',a,"=",3*a)
    print("3 x{} ={}".format(a,3*a))
    print(f"3 x {a} = {a*3}")
#148
# 리스트 = ["가","나","다","라"]
# for 변수 in 리스트[1:]:
#     print(변수)
#149
리스트 = ["가", "나", "다", "라"]
for 변수 in 리스트[::2]:
    print(변수)
#150
리스트 = ["가", "나", "다", "라"]
for 변수 in 리스트[::-1]:
    print(변수)
#151
리스트 = [3, -20, -3, 44]
for 변수 in 리스트:
    if(변수 < 0):
        print(변수)
#152 3의 배수만 출력
리스트 = [3, 100, 23, 44]
for 변수 in 리스트 :
    if 변수 % 3 == 0 :
        print(변수)
#153 20보다 작은 3의 배수
리스트 = [13,21,12,14,30,18]
for 변수 in 리스트 :
    if (변수 < 20) and (변수 % 3 == 0):
        print(변수)
#154 세 글자 이상의 문자를 화면에 출력
리스트 = ["I", "study", "python", "language", "!"]
for 변수 in 리스트 :
    if len(변수) >= 3 :
        print(변수)
#155 대문자만 화면에 출력
리스트 = ["A","b","c","D"]
for 변수 in 리스트 :
    if 변수.isupper() :
        print(변수)
#156 소문자만 화면에 출력
리스트 = ["A", "b", "c", "D"]
for a in 리스트:
    if a.islower():
        print(a)
#157 첫글자를 대문자로 변경해서 출력
리스트 = ['dog', 'cat', 'parrot']
for 변수 in 리스트:
        print(변수[0].upper() + 변수[1:])
#158 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라. (힌트: split() 메서드)
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for 변수 in 리스트:
    print(변수.split(".")[0])
#159 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라.
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트:
    if 변수.split(".")[1] == 'h' :
        print(변수)
#160 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하라.
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트 :
    if 변수.split(".")[1] == 'c' or 변수.split(".")[1] == 'h' :
        print(변수)
#161 for문과 range 구문을 사용해서 0~99까지 한 라인에 하나씩 순차적으로 출력하는 프로그램을 작성하라.
for a in range(100) :
    print(a)
#162  range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.
for a in range(2002,2051,4):
    print(a)
#163 1부터 30까지의 숫자 중 3의 배수를 출력하라.
for a in range(3,31,3):
    print(a)
#164  99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력하라.
for a in range(100):
    print(99-a)
#165
for a in range(10):
    print(a/10)
#166 구구단 3단출력
for a in range(1,10):
    print(f"3 x {a} = {3*a}")
#167 3단, 홀 수번째만 출력
for a in range(1,10,2):
    print(f"3 x {a}={3*a}")
#168 1~10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라
b=0
for a in range(1,11):
    b=b+a
print("합 : ",b)
#169 ~10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for 문을 사용하여 작성하라.
b=0
for a in range(1,10):
    if a%2==1:
        b+=a
        print("합 : ",b)
b=0
for a in range(1,10,2):
        b+=a
print("합 : ",b)
#170 1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.
b=1
for a in range(1,11):
    b*=a
print("곱",b)
#171 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list[i])
#172 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(i,price_list[i])
#173
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print((len(price_list)-1)-i,price_list[i])
#174
price_list = [32100, 32150, 32000, 32500]
for i in range(1,4):
    print(90+10*i,price_list[i])
#175 my_list를 아래와 같이 출력하라.
my_list = ["가", "나", "다", "라"]
for i in [0,1,2] :
    print(my_list[i]+' '+ my_list[i+1])
my_list1 = ["가", "나", "다", "라"]
for i in range(len(my_list1)-1) :
    print(i,my_list1[i], my_list1[i+1])
my_list2 = ["가", "나", "다", "라"]
for i in range(1, len(my_list2) ) :
  print(my_list2[i-1], my_list2[i])
my_list3 = ["가", "나", "다", "라"]
for i in range(len(my_list3) - 1 ) :
  print(my_list3[i], my_list3[i+1])
#176
my_list = ["가", "나", "다", "라", "마"]
for i in range(len(my_list)-2):
    print(my_list[i],my_list[i+1],my_list[i+2])
for i in range(1, len(my_list) - 1):
    print(my_list[i - 1], my_list[i], my_list[i + 1])
for i in range(2, len(my_list)):
    print(my_list[i - 2], my_list[i - 1], my_list[i])
#177
my_list = ["가", "나", "다", "라"]
for i in range(len(my_list) - 1, 0, -1):
    print(my_list[i], my_list[i-1])
for i in range(len(my_list) - 1):
    print(my_list[len(my_list) - 1 - i], my_list[len(my_list) - 2 - i])
#178
my_list = [100, 200, 400, 800]
for i in range(len(my_list)-1):
    print(my_list[i+1]-my_list[i])
#179
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(1,len(my_list)-1) :
    print((my_list[i-1]+my_list[i]+my_list[i+1]) / 3)
#180
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility =[]
for i in range(len(high_prices)) :
    volatility.append(high_prices[i] - low_prices[i])
print(volatility)
#181 하나의 행을 하나의 리스트로, 총 3개의 리스트를 갖는 이차원 리스트 apart를 정의하라.
apart =[['101호','102호'],['201호','202호'],['301호','302호']]
#182 아래 표에서 하나의 열을 하나의 리스트로, 총 2개의 리스트를 갖는 이차원 리스트 stock을 정의하라.
stock = [["시가",100,200,300],["종가",80,210,330]]
#183 아래 표를 stock 이름의 딕셔너리로 표현하라.시가를 key로 저장하고, 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다. 종가 역시 key로 저장하고 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다.
stock ={"시가":[100,200,300],"종가":[80,210,330]}
#184 아래 표를 stock 이라는 이름의 딕셔너리로 표현하라. 날짜를 key로 저장하고, 나머지 같은 행의 데이터를 리스트로 저장해서 value로 저장한다. 첫 열이 날짜이다.
stock ={"10/10":[80,110,70,90],"10/11":[210,230,190,200]}
#185 리스트에 저장된 데이터를 아래와 같이 출력하라.
apart = [ [101, 102],
          [201, 202],
          [301, 302] ]
for i in apart:
   for j in i :
       print(j,"호")
#186
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::-1]:
    for j in i :
        print(j,"호")
#187
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::-1]:
    for j in i[::-1]:
        print(j,"호")
#188
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(j,'호','\n','-----')
#189
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(j,'호')
    print("-----")
#190
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(j,'호')
print('-----')
#191
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for i in data:
    for j in i:
        print(j+(j*0.014*0.01))
#192  191번의 출력 결과에 행단위로 "----" 구분자를 추가하라.
for i in data:
    for j in i:
        print(j+(j*0.014*0.01))
    print("-"*5)
#193 192 번 문제의 결괏값을 result 이름의 리스트에 1차원 배열로 저장하라.
result=[]
for i in data:
    for j in i:
        result.append(j + (j * 0.014 * 0.01))
print(result)
#194 191번 문제의 결괏값을 result 이름의 리스트에 2차원 배열로 저장하라. 저장 포맷은 아래와 같다. 각 행에 대한 데이터끼리 리스트에 저장되어야 한다.
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result = []
for price in data:
    day_price = []
    for price in price:
        new_p = price + (price * 0.014 *0.01)
        day_price.append(new_p)
    result.append(day_price)
print(result)
#195 ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 화면에 종가데이터를 출력하라.
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:]:
    print(i[3])
#196 종가가 150원보다 큰경우에만 종가를 출력하라.
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:]:
    if i[3] > 150:
        print(i[3])
#197 종가가 시가 보다 크거나 같은 경우에만 종가를 출력하라.
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:]:
    if i[3] >= i[0]:
        print(i[3])
#198  고가와 저가의 차이를 변동폭으로 정의할 때 변동폭을 volatility 이름의 리스트에 저장하라.
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
volatility=[]
for i in ohlc[1:]:
    volatility.append(i[1]-i[2])
print(volatility)
#199 종가가 시가보다 높은 날의 변동성 (고가 - 저가)을 화면에 출력하라.
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for row in ohlc[1:]:
    if row[3] > row[0]:
        print(row[1]-row[2])
#200 시가에 매수해서 종가에 매도 했을 경우 총 수익금을 계산하라.
hap =0
for i in ohlc[1:]:
     cu = i[0]-i[3]
     hap += cu
print(hap)













