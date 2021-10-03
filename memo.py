import sys

option = sys.argv[1] # 입력
memo = sys.argv[2] # 출력

if option == '-a':
    f = open('memo.txt','a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)

