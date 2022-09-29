n, m = map(int, input().split())

cards = list(map(int, input().split()))

# n = 5
# m = 21
# cards = [5, 6, 7, 8, 9]

total = 0
maxtotal = 0

for i in range(3):
    for j in range(i + 1, 4):
        for k in range(j + 1, 5):
            total = cards[i] + cards[j] + cards[k]

            if maxtotal < total <= m:
                maxtotal = total
                # print(maxtotal)

            if total == m:
                maxtotal = total
                # print(maxtotal)
                break
print(maxtotal)
