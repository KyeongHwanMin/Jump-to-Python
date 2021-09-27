# 04. 파이썬 리스트
# 051 리스트 생성
movie_rank = ["닥처 스트레인지","스플릿","럭키"]
#052 리스트에 원소 추가
# 051의 movie_rank 리스트에 "배트맨"을 추가하라.
movie_rank.append("배트맨")
print(movie_rank)

#053 movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다.
# "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1,"슈퍼맨")
print(movie_rank)

#054
# movie_rank 리스트에서 '럭키'를 삭제하라.
#movie_rank.remove("럭키")
del movie_rank[3]
print(movie_rank)

#055 movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
#del movie_rank[-2:]
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

#056  lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
lang1 = ["c","c++","JAVA"]
lang2 = ["Python","Go","C#"]
lang3=lang1+lang2
print(lang3)

#057최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)
nums = [1,2,3,4,5,6,7]
print("max:",max(nums))
print("min:",min(nums))

#058 리스트의 합 출력
nums = [1,2,3,4,5]
print(sum(nums))

#059 저장된 데이터의 개수를 화면에 구하하라.
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

#060 리스트의 평균 출력
nums = [1,2,3,4,5]
avg = sum(nums) / len(nums)
print(avg)

#061 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#062 슬라이싱을 사용해서 홀수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

#063 슬라이싱을 사용해서 짝수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

#064 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

#065
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0],interest[2])

#066 join 메서드
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(' '.join(interest))
interest1 =' '.join(interest)
print(type(interest))
print(type(interest1))

#067 join 메서드
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('/'.join(interest))

#068 join 메서드
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('\n'.join(interest))

#069 문자열 split 메서드
string = "삼성전자/LG전자/Naver"
string=string.replace('/',',')
print(string)

#070 리스트 정렬 (오름차순)
data = [2, 4, 3, 1, 5, 10, 9]
print(sorted(data))
data.sort()