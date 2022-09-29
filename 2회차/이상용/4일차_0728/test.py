# 코드 간소화 ver2
x, y = map(int, input().split())
numbers = [i for i in range(1, y+1) for j in range(i)]
print(sum(numbers[x-1:y]))