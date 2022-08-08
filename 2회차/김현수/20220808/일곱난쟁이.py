import sys
sys.stdin = open("일곱난쟁이.txt")

list_ = [int(input()) for _ in range(9)]
dist = sum(list_) - 100
cnt = 0
for a in range(9-1):
    for b in range(a+1,9):
        twosum = list_[a] + list_[b]

        if dist == twosum:
            list_.remove(list_[b])
            list_.remove(list_[a])
            cnt = 1
            break
    if cnt == 1:
        break

list_.sort()

for _ in list_:
    print(_)