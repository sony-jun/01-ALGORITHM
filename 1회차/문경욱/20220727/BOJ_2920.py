#N = list(map(int, input().split()))
N = [1,2,3,4,5,6,7,8]
gap_N = []
result = ''

for i in range(7):
    gap_N.append(N[i+1]-N[i])

for i in range(7):
    if gap_N[i] != 1 or gap_N[i] != -1:
        result = 'mixed'
        break
    elif gap_N[i] == 1 and -1 not in gap_N:
        result = 'ascending'
    elif gap_N[i] == -1 and -1 not in gap_N:
        result = 'descening'

print(result)