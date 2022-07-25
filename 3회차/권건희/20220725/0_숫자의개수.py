# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")
a=int(input())
b=int(input())
c=int(input())
multi=a*b*c
# 멀티를 str로 변환하고 {}생성, 인덱스로 접근, 해당 밸류에 +1하자
multi=str(multi)
numbers={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
for n in multi:
    for i in range(10):
        if n==str(i):
            numbers[str(i)]+=1
for i in range(10):
    print(numbers[str(i)])            