import sys
input = sys.stdin.readline

def dwarfFinder(dwarf):
    dwarf = list(dwarf)
    fake = sum(dwarf) - 100

    for i in range(9):
        for j in range(i+1, 9):
            if dwarf[i] + dwarf[j] == fake:
                a, b = dwarf[i], dwarf[j]
                dwarf.remove(a)
                dwarf.remove(b)
                return dwarf

dwarf = [int(input()) for _ in range(9)]
ans = dwarfFinder(dwarf)
ans.sort()

for i in ans:
    print(i)