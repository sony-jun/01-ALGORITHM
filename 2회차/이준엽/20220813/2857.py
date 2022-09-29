cnt = 0
result = []
for i in range(1,6):
    fbi = input()
    if 'FBI' in fbi:
        result.append(i)
if result:
    print(*result)
else:
    print('HE GOT AWAY!')