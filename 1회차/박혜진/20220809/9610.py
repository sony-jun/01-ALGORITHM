four = {
    'Q1' : 0,
    'Q2' : 0,
    'Q3' : 0,
    'Q4' : 0,
    'AXIS' : 0
}

for _ in range(int(input())) :
    # x, y 값 입력받기
    x, y = map(int, input().split())

    if x > 0 and y > 0 :
        four['Q1'] += 1

    elif x < 0 and y > 0 :
        four['Q2'] += 1
        
    elif x < 0 and y < 0 :
        four['Q3'] += 1

    elif x > 0 and y < 0 :
        four['Q4'] += 1

    else :
        four['AXIS'] += 1

print('Q1:', four['Q1'])
print('Q2:', four['Q2'])
print('Q3:', four['Q3'])
print('Q4:', four['Q4'])
print('AXIS:', four['AXIS'])