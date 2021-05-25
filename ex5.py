ticker="btc_krw"
ticker=ticker.upper()
print(ticker)

ticker="BTC_KRW"
ticker2=ticker.lower()
print(ticker2)

str="hello"
str1=str.capitalize()
print(str1)

#45 여려개의 문자열로 끝나는지 확인
file_name="보고서.xls"
print(file_name.endswith("xlsx"))
print(file_name.endswith(("xlsx","xls")))

file_name="2020_보고서.xlsx"
print(file_name.startswith("2020"))

a="hello world"
a=a.split()
print(a)

ticker="btc_krw"
ticker1=ticker.split("_")
print(ticker1)

date="2020-05-01"
date1=date.split("-")
print(date1)

date="039490              "
print(date.rsplit())


