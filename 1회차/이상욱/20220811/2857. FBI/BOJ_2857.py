import sys
sys.stdin = open('2857.txt')

n = 5
name = [' ']
cnt = 0
for _ in range(n):
    name.append(input())

for i in range(len(name)):

    if 'FBI' in name[i]:
        print(name.index(name[i]), end=' ')
        cnt += 1
if cnt == 0:    
    print('HE GOT AWAY!')