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
print(a.get(4,'없음'))
print(4 in a)# 키 찾기
print(1 in a)

# 집합
# 집합에 관련된 것들을 쉽게 처리하기 위해 만들어진 자료형
# 중복을 허용하지 않는다.
# 순서가 없다
