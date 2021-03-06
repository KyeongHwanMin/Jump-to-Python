# https://wikidocs.net/7014
# 001 ~ 010
# 001 화면에 Hello World 문자열 출력하세요.
print("Hello World")
# 002 화면에 Mary's cosmetics을 출력하세요. (중간에 '가 있음에 주의하세요)
print("Mary's cosmetics")
# 003 화면에 아래 문장을 출력하세요. (중간에 "가 있음에 주의하세요.)
# 신씨가 소리질렀다. "도둑이야".
print('신씨가 소리질렀다. "도둑이야".')
# 004 화면에 "C:\Windows"를 출력하세요.
print('"C:\Wiondows"')
# 005 다음 코드를 실행해보고 \t와 \n의 역할을 설명해보세요.
print("안녕하세요.\n만나서\t\t반갑습니다.")  # \t는 탭을 의미하고 \n'은 줄바꿈을 의미합니다.

# 006 print 함수에 두 개의 단어를 입력한 예제입니다. 아래 코드의 출력 결과를 예상해봅시다.
print("오늘은", "일요일")
# 007 print() 함수를 사용하여 다음과 같이 출력하세요.
# naver;kakao;sk;samsung
print("naver", "kakao", "sk", "samsung", sep=";")
# print 함수의 sep 인자로 ";"를 입력하면 출력되는 값들 사이에 한 칸의 공백대신 세미콜론이 출력됩니다.
# 008 print() 함수를 사용하여 다음과 같이 출력하세요.
# naver/kakao/sk/samsung
print("naver", "kakao", "sk", "samsung", sep="/")
# 009 다음 코드를 수정하여 줄바꿈이 없이 출력하세요. (힌트: end='') print 함수는 두 번 사용합니다. 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.
# print("first");print("second")
print("first", end="");print("second")
# 010 5/3의 결과를 화면에 출력하세요.
print(5 / 3)
