# https://www.acmicpc.net/problem/2439

n = int(input())
star = ''
for i in range(1, n + 1):
    star += '*'
    print(star.rjust(n))
    
# 왼쪽정렬 ljust()
# 오른쪽정렬 rjust()
# 중간정렬 center()