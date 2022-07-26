# N = M + m0 + m1 + m2 ~ ...
# N > M

N = int(input())    # N = 216

result = 0
for i in range(1, N + 1): # range(1, 217) -> 1~216까지 뽑음
    list_ = list(map(int, str(i))) # 1~216을 하나씩 str -> int -> list화 -> [2, 1, 3] [2, 1, 4]~~
    result = i + sum(list_) # 198 + (1 + 9 + 8)
    if result == N: # 더한 값들이 N과 같으면 i 출력.
        print(i)
        break