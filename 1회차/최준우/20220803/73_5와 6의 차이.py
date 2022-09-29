# https://www.acmicpc.net/problem/2864

N, M = map(str, input().split())
newN = ''
newM = ''
min_result = 0
max_result = 0

for i in N:
    if i == '6':
        newN += '5'
    else:
        newN += i
for i in M:
    if i == '6':
        newM += '5'
    else:
        newM += i
min_result = int(newN) + int(newM)

newN = ''
newM = ''
for i in N:
    if i == '5':
        newN += '6'
    else:
        newN += i
for i in M:
    if i == '5':
        newM += '6'
    else:
        newM += i
max_result = int(newN) + int(newM)

print(min_result, max_result)