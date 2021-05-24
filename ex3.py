letters="python"
print(letters[0],letters[2])

license_plate="24가 2210"
print(license_plate[-4:])

string="홀짝홀짝홀짝"
print(string[::2])

string="PYTHON"
print(string[::-1])

phone_number ="010-1111-2222"
phone_number1=phone_number.replace("-"," ")
print(phone_number1)

phone_number1=phone_number.replace("-","")
print(phone_number1)

url="http://sharebook.kr"
url_split=url.split('.')
print(url_split[-1])

lang='python'
#lang[0]='p'
print(lang)

string='abcdefghijklmn'
string=string.replace('a','A')
print(string)

string='abcd'
string.replace('b',"B")
print(string)