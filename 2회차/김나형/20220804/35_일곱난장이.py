import sys
sys. stdin = open("35_일곱난장이.txt")

N = 9

S = list(int(input()) for _ in range(N))
all = sum(S) # 난쟁이 키의 합

for i in range(N):
    for j in range(i + 1, N):
        
        if all - (S[i] + S[j]) == 100:  # 이중 for문으로 리스트에서 두 명씩 키의 합을 총 합에서 빼준다.
            num_1, num_2 = S[i], S[j]
            S.remove(num_1)
            S.remove(num_2)
            S.sort()
            print(*S, sep='\n')
            break
    if len(S) < 9:
        break
