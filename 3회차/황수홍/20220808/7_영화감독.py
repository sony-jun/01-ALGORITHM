N = int(input())
cnt = 0
number = 0

while 1:
    number += 1
    if str(number).count('666') >= 1:
        cnt += 1
    if cnt == N:
        break
print(number)