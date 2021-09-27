# 자료형
print("hello world")

a = 1
print(a)
print(type(a))

a = 3
b = 4

print(a / b)
print(a // b)  # 몫을 출력
print(a % b)

a = "python's favorite  \n food is perl"
b = "python's favorite  \t food is perl"
c = """ python's favorite  
         food is perl"""
print(a)
print(b)
print(c)

# 인덱싱
a = "python's favorite food is perl"
print(a[0])
print(a[-1])
# ==================
# 슬라이싱 [이상:미만:간격]
print(a[3:8])
b = "1234567"
print(b[::3])
# ==================
a = "I eat %d apples." % 3
print(a)
number = 10
day = "three"
a = "I aet %d apples. so I weas sick for %s days." % (number, day)
print(a)

a = "abcde {} sdfsdf".format("안녕")
b = "abide {name} sdfsdf".format(name=" 민경환")
c = "abide {age} sdfsdf{name}".format(name=" 민경환", age=30)
name = "int"
d = f"나의 이름은 {name} 입니다"
print(a)
print(b)
print(c)
print(d)

a = "%0.2f" % 3.431342324
print(a)

a = "hobbby"
print(a.count('b'))
print(a.find('b'))  # 0부터 시작
print(a.index('b'))

a = ",".join("abcd")
print(a)
a = ",".join(["a", "b", "c"])
print(a)

a = " hi "
print(a.upper())
print(a.strip())

a = "Life is too short"
print(a.replace("Life", "Your leg"))
print(a.split())  # 리스트로 반환

# 리스트
a = ["이시영", "문재성", "int", "김정현"]
print(a)
print(a[1])

a = [1, 2, "이시영", "문재성", ["int", "김정현"]]
print(a)
print(a[4])
print(a[4][1])

a = [1, 2, 3, 3, 3, 3, 4, 5]
b = [1, 2, 3, 4, 5]
print(a[0:3])
print(a + b)
a[0:2] = [10, 20]
print(a)
a[0:2] = []
print(a)
a.append(400)
print(a)
a.sort()
a.reverse()
print(a)
print(a.index(400))
a.insert(1, 500)
print(a)
a.remove(3)
print(a)
print(a.pop())  # 마지막 값 빼내기
a.extend([6, 7])
print(a)

# 4강 자료형2
# 리스트 , 튜플
# a = [1,2,3] a=[8,2,3] 리스트 변경가능
# 튜플 b=(1,2,3) 튜플 변경불가능 (길이,값 고정)

t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
print(t1[0:2])
print(t1 + t2)
t2 = t2 * 3
print(t2)

# 딕셔너리(사전)
# ex)Json(API)
# 연관 배열 또는 해시
# Key를 통해 Value를 얻는다.

dic = {'name': 'Eric', 'age': 15}
print(dic['name'])

a = {1: 'a'}
a['name'] = "익명"  # 딕셔너리 추가하기
print(a)

del a[1]  # 키 값으로 삭제
print(a)

a = {1: 'a', 1: 'b'}  # 마지막 값이 나옴
print(a)

a = {1: '파랑구름', 2: '이현준', 3: "민경환"}
print(a.keys())
print(a.values())
print(a.items())

for k, v in a.items():
    print("키는 : " + str(k))
    print("벨류는 :" + v)
# a.clear()
# print(a.items())
print(a.get(1))
print(a.get(4))  # None 출력 # print(a[4]) == 에러
print(a.get(4, '없음'))
print(4 in a)  # 키 찾기
print(1 in a)

# 집합
# 집합에 관련된 것들을 쉽게 처리하기 위해 만들어진 자료형
# 중복을 허용하지 않는다.
# 순서가 없다
s1 = set([1, 2, 3])
s1 = {1, 2, 3}
print(type(s1))

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
# 자바로 하면 이중 for문 돌려야함.
print(s1 & s2)  # s1과 s2의 교집합
print(s1.intersection(s2))  # s1과 s2의 교집합
print(s1 | s2)  # 합 집합
print(s1.union(s2))
print(s1 - s2)  # 차 집합
s1.add(10)
print(s1)
s1.update([11, 12, 13, 1])
print(s1)
s1.remove(1)
print(s1)

# 불 boolean  (문자열,리스트 등)값이 있으면 참, 없으면 거짓
a = True
print(type(a))
a = "안녕"
if a:
    print(a)
a = [1, 2, 3, 4]
while a:
    a.pop()  # 마지막 요소 없애고 출력
    print(a)
############# 변수
# a = 3
# 3이라는 값을 가지는 정수 자료형(객체)이 자동으로 메모리에 생성
# 변수 a는 객체가 저장된 메모리의 위치를 가리키는 레퍼런스(Reference)
# a라는 변수는 3이라는 정수형 객체를 가리키고 있다.
# https://pythontutor.com/live.html#mode=edit
a = [1, 2, 3]
b = a
a[1] = 4
print(id(a))  # id == 주소 값
print(id(b))
print(a is b)  # 같은 주소를 같는지 확인

a = [1, 2, 3]
b = a[:]  # a의 값을 슬라이싱(주소x)
a[1] = 4
print(a)
print(b)
print(id(a))  # id == 주소 값
print(id(b))

from copy import copy  # 값을 복사

a = [1, 2, 3]
b = copy(a)
a[1] = 4
print(a)
print(b)
print(id(a))  # id == 주소 값
print(id(b))
# 튜플을 이용한 변수 값 할당
a, b = ('python', 'life')
(a, b) = 'python', 'life'
# 리스트를 이용한 변수 값 할당
[a, b] = ['python', 'life']
a = b = 'hello'
print(a)
print(b)
# 값 바꿔서 넣기
a = 3
b = 5
a,b = b,a
print(a)
print(b)

################# 5강 (3장)제어문 ##############

