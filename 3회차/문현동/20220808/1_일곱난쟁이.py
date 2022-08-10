'''
import sys
sys.stdin = open("1_일곱난쟁이.txt", 'r')

h = set()
dwarf = []

for _ in range(9):
    dwarf.append(int(sys.stdin.readline()))

for a in range(3): # 0 부터 시작하고 자기 번호(3)는 포함하지 않기 때문에 9-7 이 아닌 9-6 부터 시작
    for b in range(a + 1, 4):
        for c in range(b + 1, 5):
            for d in range(c + 1, 6):
                for e in range(d + 1, 7):
                    for f in range(e + 1, 8):
                        for g in range(f + 1, 9):
                            if dwarf[a] + dwarf[b] + dwarf[c] + dwarf[d] + dwarf[e] + dwarf[f] + dwarf[g] == 100:
                                h.add((dwarf[a], dwarf[b], dwarf[c], dwarf[d], dwarf[e], dwarf[f], dwarf[g]))
h = sorted(list(h)[0])
for i in h:
    print(i)
'''
import sys
sys.stdin = open("1_일곱난쟁이.txt", 'r')

dwarf = []

for _ in range(9):
    dwarf.append(int(sys.stdin.readline()))

for left_out_1 in dwarf: # range(9) 를 해서 dwarf[i] 같이 하면 remove 할 때마다 범위가 달라져서 안된다.
    for left_out_2 in dwarf:
        if sum(dwarf) - left_out_1 - left_out_2 == 100 and left_out_1 != left_out_2:
            dwarf.remove(left_out_1)
            dwarf.remove(left_out_2)
            break
        
dwarf.sort()
for i in dwarf:
    print(i)