# 1.2.1 연습 문제: 파일 크기 계산
# 문제
# 파일을 다운로드할 때의 평균 속도(average rate)를 이라 하고, 다운로드하는 데 걸린 시간(time)을 라고 할 때,
# 다운로드한 파일의 용량은 r x t 로 계산할 수 있습니다.
#
# 다운로드 속도가 초당 800kB이고 다운로드하는 데 걸린 시간이 110초라고 할 때, 다운로드한 파일의 크기는 몇 MB일까요?
# 단, 1MB = 1000kB 로 계산합니다.

average_rage = 800
time = 110

down = average_rage * time / 1000
print(down)

# 1.6.1 연습 문제: 제곱
# 문제
# 사용자에게 정수를 입력받아, 그 수의 제곱을 계산해 출력하는 파이썬 스크립트를 작성하세요.

print("정수를 입력 하시오. : ")
num = int(input())
print(num * num)