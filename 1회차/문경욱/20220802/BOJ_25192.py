import sys
input = sys.stdin.readline

N = int(input())

list_ = []
set_ = set()
gom_cnt = 0


for i in range(N):
    T = input()
    if T == 'ENTER\n':
        gom_cnt += len(set(list_))
        list_ = []
        continue

    elif i == N-1 and T != 'ENTER\n':
        list_.append(T)
        gom_cnt += len(set(list_))

    else:
        list_.append(T)

print(gom_cnt)