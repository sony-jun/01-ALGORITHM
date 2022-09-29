import sys
input = sys.stdin.readline

n = int(input())
f = [] #첫번째 점수 리스트
s = [] #두번째 점수 리스트
t = [] #세번째 점수 리스트

for _ in range(n): #n만큼 반복
    a, b, c= map(int,input().split()) #공백을 포함한 값 input
    f.append(a) #첫번째 점수를 f 리스트에 넣기
    s.append(b)
    t.append(c)

for i in range(n): 
    result = 0
    if f.count(f[i]) == 1:  #숫자를 입력한 값이 자신 밖에 없으면
        result += f[i]
    if s.count(s[i]) == 1:
        result += s[i]
    if t.count(t[i]) == 1:
        result += t[i]
    print(result)