import sys

sys.stdin = open("91.일곱 난쟁이.txt")


list_n = [int(input()) for tc in range(9)]

list_n.sort()
sum_n = sum(list_n)

for i in range(9):
    for j in range(9):

        if sum_n - (list_n[i]+list_n[j]) == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                else:
                    print(list_n[k])
            exit()