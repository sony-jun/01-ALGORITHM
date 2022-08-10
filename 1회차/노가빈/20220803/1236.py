import sys

input = sys.stdin.readline #처리속도 빠르게 하기 위해 sys이용

n, m = map(int, input().split(' ')) #n,m을 map을 이용해 int로 받기

count = 0 #count를 0으로 최초 선언

for index in range(n):
    i = input().split() # 한 줄씩 받아서
    i = ''.join(i) # 문자열로 바꾼 다음
    if 'X' not in i: # 병사가 없으면
        count += 1 # 병사가 필요한 수 즉 count를 1씩 증가시킨다

print(count) #필요한 병사의 수 출력