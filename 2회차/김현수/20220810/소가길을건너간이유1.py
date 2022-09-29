import sys

sys.stdin = open("소가길을건너간이유1.txt")

N = int(input()) #소관잘 횟수
where = dict() #소가 어디있는가 dict()
cnt = 0

for _ in range(N):
    a, b = map(int,input().split()) #소번호 + 소위치
    if a in where: 
        if where[a] != b:
            cnt += 1
            where[a] = b
            print('변화관찰:',where,cnt)
    else: #해당 번호 소가 없을 경우
        where[a] = b
        print('첫관찰  :',where,cnt)
print('카운팅',cnt)