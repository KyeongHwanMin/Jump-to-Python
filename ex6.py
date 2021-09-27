#파이썬 딕셔너리는 순서는 없지만 key와 value 형태로 데이터를 저장합니다.
#특히 key는 데이터의 레이블(label)을 지정하는 용도로 자주 사용됩니다.
# 081 ~100
#081 별 표현식
#기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 합니다.
# 하지만 star expression을 사용하면 변수의 개수가 달라도 데이터 언패킹을 할 수 있습니다.
# 튜플에 저장된 데이터 중에서 앞에 있는 두 개의 데이터만 필요할 경우 나머지 데이터의 언패킹 코드를 작성할 필요가 없습니다.
# >> a, b, *c = (0, 1, 2, 3, 4, 5)
# >> a
# 0
# >> b
# 1
# >> c
# [2, 3, 4, 5]
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score,a,b=scores
print(valid_score)
print(a)
print(b)
scores.sort()
print(scores)
min,*scor,max = scores
print(f"최저점 : {min} 최고점 : {max}")
print(f"나머지 : {scores}")

#082 start expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a,b,*valid_score = scores
print(valid_score)

#083 start expression을 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a,*valid_score,b = scores
print(valid_score)

#084 비어있는 딕셔너리
#temp 이름의 비어있는 딕셔너리를 만들라.
temp ={}

#085
dic = {"메로나":1000,"폴라포":1200,"빵빠레":1800}
print(dic)

#086 085 번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.
dic["죠스바"] = 1200
dic["월드콘"] = 1500
print(dic)
print(dic["죠스바"])

#087 딕셔너리를 사용하여 메로나 가격을 출력하라.
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print(f"메로나 가격: {ice['메로나']}")
print("메로나 가격 :",ice['메로나'])

#088 딕셔너리에서 메로나의 가격을 1300으로 수정하라.
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
ice['메로나'] = 1300
print(ice['메로나'])

#089 다음 딕셔너리에서 메로나를 삭제하라.
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
#ice.pop('메로나')
del ice['메로나']
print(ice)

#90 다음 코드에서 에러가 발생한 원인을 설명하라.
# >> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# >> icecream['누가바']
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     icecream['누가바']
# KeyError: '누가바'
# 누가바에 키값이 없음.

#091 딕셔너리 생성
inventory ={"메로나":[300, 200],
            "비비빅":[400,3],
            "죠스바":[250,100]
            }
print(inventory)

#092 딕셔너리 인덱싱
# inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.
print(inventory["메로나"][0],'원')

#093 딕셔너리 인덱싱
#inventory 딕셔너리에서 메로나의 재고를 화면에 출력하라.
print(inventory["메로나"][1],'개')

#094 딕셔너리 추가
inventory["원드콘"] = [500,7]
print(inventory)

#095 딕셔너리 keys() 메서드
# 다음의 딕셔너리로부터 key 값으로만 구성된 리스트를 생성하라.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(icecream.keys())
ice = icecream.keys()

#096 딕셔너리 values() 메서드
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice_v = icecream.values()
print(type(ice_v))
price = list(icecream.values())
print(price,type(price))

#097 딕셔너리 values() 메서드
#icecream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(sum(icecream.values()))

#098 딕셔너리 update 메서드
#아래의 new_product 딕셔너리를 다음 icecream 딕셔너리에 추가하라.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

#099 zip과 dict
#아래 두 개의 튜플을 하나의 딕셔너리로 변환하라. keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장한다.
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
#result = {[keys] : [vals]}
result = dict(zip(keys,vals))
print(result,type(result))

#100 zip과 dict
#date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date,close_price))
print(close_table)




