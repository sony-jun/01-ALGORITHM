from sys import stdin
N, M = map(int, stdin.readline().split()) # N권, M개의 더미

is_order_possible = True # 정렬 가능 여부

for _ in range(M):
    stdin.readline()
    input_list = list(map(int, stdin.readline().split())) # 책 더미 입력
    if input_list != sorted(input_list, reverse = True): # 책 더미의 정렬 여부 확인
        is_order_possible = False # 정렬이 불가할 때 # 기입 후 break
        break

if is_order_possible:
    print('Yes')
else:
    print('No')