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