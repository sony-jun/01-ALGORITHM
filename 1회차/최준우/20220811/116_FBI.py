# https://www.acmicpc.net/problem/2857

result = []

for i in range(5):
    name = input()

    if 'FBI' in name:
        result.append(i+1)

if len(result) > 0:
    for i in result:
        print(i, end = ' ')
else:
    print('HE GOT AWAY!')