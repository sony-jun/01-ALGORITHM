#더 적은 개수의 알파벳 기준으로 2를 나눈 몫 = 만들 수 있는 모형의 최대값

S, A = map(int, input().split())

#print(S,A) 4 5

if S <= A:
    print(S // 2)
else:
    print(A // 2)