n = int(input())
coord = {
    'Q1': 0,
    'Q2': 0,
    'Q3': 0,
    'Q4': 0,
    'AXIS':0
}
for i in range(n):
    x,y = map(int,input().split())
    if x>0 and y>0:
        coord['Q1']+=1
    elif x<0 and y>0:
        coord['Q2']+=1
    elif x<0 and y<0:
        coord['Q3']+=1
    elif x>0 and y<0:
        coord['Q4']+=1
    elif x == 0 or y == 0:
        coord['AXIS']+=1
for co in coord:
    print(f'{co}: {coord[co]}')
