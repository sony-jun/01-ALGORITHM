N = int(input())
qurter = {
    'Q1' : 0,
    'Q2' : 0,
    'Q3' : 0,
    'Q4' : 0,
    'AXIS' : 0
}
for a in range(N):
    x, y = map(int, input().split())
    if x * y > 0:
        if y > 0:
            qurter['Q1'] = qurter.get('Q1') + 1
        if y < 0:
            qurter['Q3'] = qurter.get('Q3') + 1
    
    if x * y < 0:
        if y > 0:
            qurter['Q2'] = qurter.get('Q2') + 1
        if y < 0:
            qurter['Q4'] = qurter.get('Q4') + 1
    
    if x * y == 0:
        qurter['AXIS'] = qurter.get('AXIS') + 1

for a in qurter:
    print(f'{a}: {qurter.get(a)} ')