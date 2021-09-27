# 파이썬 문자열
# 021 ~030
# 021 문자열 인덱싱
# letters가 바인딩하는 문자열에서 첫번재와 세번째 문자를 출력하세요.
letters = 'python'
print(letters[0],letters[2])
#파이썬 문자열에서 한 글자를 가져오는 것을 인덱싱이라고 부릅니다. 파이썬 인덱싱은 0부터 시작합니다.

# 022 문자열 슬라이싱
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
license_plate = "24가 2210"
print(license_plate[4:])
print(license_plate[-4:])
#문자열에서 여러 글자를 가져오는 것을 슬라이싱이라고 부릅니다.
# 음수 값은 문자열의 뒤에서부터 인덱싱 또는 슬라이싱함을 의미합니다.
# 슬라이싱에서 시작 인덱스를 생락혀면 0으로 간주하고 끝 인덱스를 생략하면 문자열의 끝을 의미합니다.

#023 문자열 인덱싱
# '홀'만 출력
string = "홀짝홀짝홀짝"
print(string[::2])
print(string[0],string[2],string[4],sep="")
print(string[::-2])

#024 문자열 슬라이싱
# 문자열을 거꾸로 뒤집어 출력하세요.
string = "PYTHON"
print(string[::-1])

#025 문자열 치환
# 전화번호에서 하이푼('-')을 제거하고 출력
phone_number = "010-1111-2222"
p1=phone_number.replace("-"," ")
print(phone_number[4]) # 문자열 불구하고, 자바의 리스트 처럼 출력됨
print(p1[4])
print(p1)
#파이썬 문자열에서 replace 메서드를 사용하면
# 문자열을 일부를 치환할 수 있습니다.
# 문자열은 수정할 수 없는 자료형이므로
# 기존 문자열은 그대로 두고 치환된
# 새로운 문자열이 리턴됩니다.

# 26 문자열 다루기
#25번 전화번호를 붙여 출력하기
p2=phone_number.replace("-","")
print(p2)

#27 문자열 다루기
#url에 저장된 웹 페이지 주소에서 도메인을 출력.
url = "http://sharebook.kr"
print(url[-2:])

#28 문자열은 immutable
lang = 'python'
#lang[0] = 'p'
print(lang)
#문자열은 수정할 수 없습니다.
# 실행 결과를 확인해보면 문자열이
# 할당(assignment) 메서드를 지원하지 않음을 알 수 있습니다.

#029 replace 메서드
# 소문자'a'를 대문자 'A'로 변경하세요.
string = 'abcdfe2a354a32a'
print(string.replace('a',"A"))

#030 replace 메서드
string = 'abcd'
string.replace('b','B')
print(string)
#문자열은 수정할 수 없습니다.