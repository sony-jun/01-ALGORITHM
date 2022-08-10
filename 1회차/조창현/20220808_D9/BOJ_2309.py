import sys
sys.stdin = open('2309.txt')

dwarf = []
dwarf_sum = 0
for i in range(9):
    dwarf.append(int(input()))
    dwarf_sum += dwarf[i]
#print(dwarf, dwarf_sum)

dwarf_rev = dwarf_sum - 100
#print(dwarf_rev)

dwarf_minu = 0
for i in range(9):
    for j in range(i + 1, 9):
        dwarf_minu = dwarf[i] + dwarf[j]
        if dwarf_minu == dwarf_rev:
            #print(dwarf[i], dwarf[j])
            dwarf_one = dwarf[i]
            dwarf_two = dwarf[j]

dwarf.remove(dwarf_one)
dwarf.remove(dwarf_two)
dwarf.sort()

for i in range(len(dwarf)):
    print(dwarf[i])
            
