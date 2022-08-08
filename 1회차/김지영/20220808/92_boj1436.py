# 종말의 숫자 666

n = int(input())
i = 0
num = 0
while i != n:
     num += 1 # n번째 666까지 커지는 number
     if '666' in str(num): # number에 666이 있으면
        i += 1 # count n
print(num)