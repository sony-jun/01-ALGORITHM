num = sum(map(int, input().split()))
winner = 1

for i in range(2, 6):
    temp = sum(map(int, input().split()))

    if num < temp:
        winner = i
        num = temp

print(winner, num)