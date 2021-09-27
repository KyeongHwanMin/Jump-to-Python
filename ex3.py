# 파이썬 문자열
# 021 ~050
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

#031 문자열 합치기
a = "3"
b = "4"
print(a+b)
#032 문자열 곱하기
print("Hi"*3)
#033 문자열 곱하기
# 화면에 '-'를 80개 출력하세요.
print('-'*80)

# 034 문자열 곱하기
# 변수에 다음과 같은 문자열이 바인딩 되어 있습니다.
t1 = 'python'
t2 = 'java'
# python java python java python java python java 출력
print((t1+' '+t2+' ') *4)

# 035 문자열 출력
# %fromatting 을 사용
name1 = "김민수"
age1 = 10
name2 = "이철희"
age = 10
print("이름 : %s 나이 : %d" %(name1, age1))

# 036 문자열 출력
# 문자열의 format() 메서드를 사용해서 35번 문제 풀기
print(format("이름: {} 나이 : {}".format(name1,age1)))
#037 문자열 출력
# f-string 사용
print(f"이름: {name2} 나이: {age}")
#f-string은 문자열 앞에 f가 붙은 형태입니다.
# f-string을 사용하면 {변수}와 같은 형태로
# 문자열 사이에 타입과 상관없이 값을 출력할 수 있습니다.

# 038 컴마 제거하기
# 컴마를 제거한 후 정수 타입으로 변환
상장주식수 = "5,969,782,550"
# 상장주식수=상장주식수.replace(",",'')
# 상장주식수 = int(상장주식수)
# print(상장주식수,type(상장주식수))
#
# #039 문자열 슬라이싱
# # '2020/03'만 출력하기
# 분기 = "2020/03(E) (IFRS연결)"
# print(분기[0:7])
#
# #040 strip 메서드
# # 문자열의 좌우 공백 제거
# data = "  삼성전자   "
# print(data)
# print(data.strip())
#
# # 041 upper 메서드
# 대문자 BTC_KRW로 변경
ticker = "btc_krw"
print(ticker.upper())

# 042 lower 메서드
ticker = "BTC_KRW"
print(ticker.lower())

# 043 capitalize 메서드
a = 'hello'
print(a.capitalize())

# 044 endswith 메서드
#파일 이름이 문자열로 저장되어 있을 때
# endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
file_name = "보고서.xls"
print(file_name.endswith("xlsx"))

# 045 endswith 메[서드
print(file_name.endswith(("xlsx", "xls")))

# 046 startswith 메서드
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))

# 047 split 메서드
a = "hello world"
print(a.split())

# 048 split 메서드
ticker = "btc_krw"
print(ticker.split('_'))

# 049 split 메서드
date = "2020-05-01"
print(date.split('-'))

# 050 rstrip 메서드
date = "03940         "
date.rstrip("03940         ")
print(date)
date1 = "        03940"
print(date1.lstrip())