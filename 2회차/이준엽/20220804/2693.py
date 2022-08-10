t = int(input())
for i in range(t):
    numbers = list(map(int,input().split()))
    numbers.sort(reverse=True)
    print(numbers[2])