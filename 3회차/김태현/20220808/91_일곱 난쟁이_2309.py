import sys
sys.stdin = open("91_일곱 난쟁이_2309.txt", "r")

isBool = True

# 난쟁이 키 리스트
hei_list = []

for _ in range(9):
    hei_list.append(int(input()))

hei_list.sort()

for i in range(8):
    for j in range(i+1, 9):
        if sum(hei_list) - hei_list[i] - hei_list[j] != 100: continue
        else: 
            del hei_list[j]
            del hei_list[i]
            isBool = False
            break
    if isBool == False:
        break

print(*hei_list, sep="\n")