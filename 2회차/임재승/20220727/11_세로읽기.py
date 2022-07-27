# https://www.acmicpc.net/problem/10798

sero = []
length = []
answer = ''

for i in range(5):
    T = input()
    sero.append(T)
    length.append(len(T))

for m in range(max(length)):
    for n in range(5):
        if m < length[n]:
            answer += sero[n][m]

print(answer)