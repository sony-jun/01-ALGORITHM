S = list(input())

answer = 0

for i in S:
    # A ~ Z : 65 ~ 90
    temp = ord(i) % 65
    # temp : 0 ~ 25, S, V, Y, Z는 예외처리 해야한다.
    # Y를 빼먹었다.
    if temp == 18 or temp == 21 or temp >= 24:
        answer += temp // 3 + 2
    else:
        answer += temp // 3 + 3
    
print(answer)