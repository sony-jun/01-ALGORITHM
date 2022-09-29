A , B =map(int, input().split())
total = []

for a in range(B+1):
    number = a*[a]
    total += number

print(sum(total[A-1:B]))

