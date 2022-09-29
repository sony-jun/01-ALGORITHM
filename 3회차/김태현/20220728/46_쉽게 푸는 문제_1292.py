import sys
sys.stdin = open("46_쉽게 푸는 문제.txt", "r")

a, b = map(int, input().split())

li = []
cnt = 1

while len(li) <= 1000: # A, B가 1000 이하의 정수이므로 리스트 길이 <= 1000
    for j in range(cnt): # '숫자' 만큼 반복하기 위해 range(cnt)
        li.append(cnt)
    cnt += 1

print(sum(li[a-1: b]))