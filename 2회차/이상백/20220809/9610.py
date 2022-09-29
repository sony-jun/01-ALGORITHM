T = int(input())

result1 = 0
result2 = 0
result3 = 0
result4 = 0
result5 = 0

for i in range(1, T+1):
    x, y = map(int, input().split())

    if x > 0 and y > 0:
            result1 += 1
    if x < 0 and y > 0:
            result2 += 1
    if x < 0 and y < 0:
            result3 += 1
    if x > 0 and y < 0:
            result4 += 1
    if x == 0 or y == 0:
            result5 += 1
        
print('Q1:', result1)
print('Q2:', result2)
print('Q3:', result3)
print('Q4:', result4)
print('AXIS:', result5)
