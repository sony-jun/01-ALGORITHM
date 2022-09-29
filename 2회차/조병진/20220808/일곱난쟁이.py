# 일곱 난쟁이 🐳
# 문제 : 아홉 명의 난쟁이 중 백설 공주의 난쟁이 7명 구하기, 7명의 키의 합은 100

N = 9
dwarf = [int(input()) for _ in range(N)]

total = sum(dwarf)  # 140
a, b = 0, 0
for i in range(N - 1):  # 가짜 난쟁이 2명 찾기
    for j in range(i + 1, N):
        if total - (dwarf[i] + dwarf[j]) == 100:
            a, b = dwarf[i], dwarf[j]

dwarf.remove(a)
dwarf.remove(b)
dwarf.sort()

print(*dwarf, sep='\n')
