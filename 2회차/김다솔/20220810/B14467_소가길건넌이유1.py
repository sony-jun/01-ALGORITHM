# https://www.acmicpc.net/problem/14467
import sys
sys.stdin = open('B14467.txt')

n = int(input())
dict_ = {} #소번호:위치
cnt = 0 #몇 번 건넜는지
for i in range(n):
    cow, location = map(int, input().split())
    if cow not in dict_: 
        dict_[cow] = location
    else:
        if dict_[cow] == location:
            continue # 안 움직인거니까 아래꺼 쓰루하고 다시 반복문으로
        else:#다르면 길건넜으니까 카운트, 새위치 저장
            cnt += 1
            dict_[cow] = location

print(cnt)