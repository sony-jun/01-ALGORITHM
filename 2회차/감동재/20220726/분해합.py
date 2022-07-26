n = int(input())

def sum_sit(n):
    total = 0
    while n!=0:
        total += n%10
        n//=10

    return total

cnt = n

while True :
    cnt-=1
    if sum_sit(cnt) + cnt == n:
        break

print(cnt)

