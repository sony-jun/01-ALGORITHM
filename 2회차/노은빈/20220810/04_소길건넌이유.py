#소가 길을 건너간 이유1
import sys
input = sys.stdin.readline

cnt = 0 #소가 건넌 횟수
N = int(input()) #관찰 횟수
where = dict()

for i in range(N) :
    n, p =map(int,input().split())
    if n in where: #해당 번호에 소가 있을 때
        if where[n] != p:
            cnt += 1
            where[n] = p
    else: #해당 번호에 소가 없을 때
        where[n] = p

print(cnt)
