import sys
sys. stdin = open("36_영화감독.txt")

n = int(input())
cnt = 0
num = 666

while True:
    if '666' in str(num): # 666이 들어가는 수만 count
        cnt += 1 # 시즌 1 = 666, 시즌 2 = 1666

    if cnt == n:
        break

    num += 1

print(num)