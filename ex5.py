# 05. 파이썬 튜플
# 071 ~080
# 071 my_variable 이름의 비어있는 튜플을 만들라.
my_variable = ()
# 괄호는 튜플을 정의하는 기호입니다.
print(type(my_variable))

# 072
movie_rank = ('닥터 스트레인지', '스플릿', '럭키')

# 073 숫자 1이 저장된 튜플 만들기
my_tuple = (1)
print(type(my_tuple))
# 아래와 같이 괄호와 함께 하나의 정숫값을 저장하면 튜플이 정의 될 것같지만 그렇지 않습니다.
# type()을 출력해보면 파이썬은 튜플이 아닌 정수로 인식합니다.
# 하나의 데이터가 저장되는 경우, 아래와 같이 쉼표를 입력해만 합니다.
my_tuple = (1,)
print(type(my_tuple))

# 074
# >> t = (1, 2, 3)
# >> t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment
# 튜플은 값 수정 불가

# 075
t = 1, 2, 3, 4
# 원칙적으로 튜플은 괄호와 함께 데이터를 정의해야 하지만,
# 사용자 편의를 위해 괄호 없이도 동작합니다.

# 076
# 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
# 새로운 튜플을 만들고 t 라는 변수를 업데이트 해야 합니다.
# 기존의 튜플 ('a', 'b', 'c')은 자동으로 삭제됩니다.

# 077 다음 튜플을 리스트로 변환하라.
interest = ('삼성전자', 'LG전자', 'SK Hynix')
change = list(interest)
print(type(change))

# 078 리스트 -> 튜플
interest = ['삼성전자', 'LG전자', 'SK Hynix']
change = tuple(interest)
print(type(change))

# 079 튜플 언팩킹
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

# 080 range 함수
# 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.
# (2, 4, 6, 8 ... 98)
ran=tuple(range(2,99,2))
print(ran)
