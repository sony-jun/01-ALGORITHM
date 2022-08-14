s,k,h = map(int,input().split())
universe = {}
universe[s] = 'Soongsil'
universe[k] = 'Korea'
universe[h] = 'Hanyang' 
if s+k+h>=100:
    print('OK')
else:
    print(universe[min([s,k,h])])