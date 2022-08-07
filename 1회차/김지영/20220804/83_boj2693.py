line = int(input())
for _ in range(line):
    num = list(map(int,input().split()))
    num.sort()
    num = num[::-1]
    print(num[2])