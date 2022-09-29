N = int(input())
customers = list(map(int, input().split()))

pc = [0] * 101
count = 0
for customer in customers:
    if pc[customer] == 0:
        pc[customer] = customer
    elif pc[customer] != 0:
        count += 1

print(count)