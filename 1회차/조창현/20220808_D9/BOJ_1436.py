import sys
sys.stdin = open('1436.txt')
# n은 n번째로 작은 수
n = int(input())
num = 0
cnt = 0
while cnt <= n:
    num += 1
    #print(num)
    if '666' in str(num):
        cnt += 1
        #print(num)
        if cnt == n:
            print(num)