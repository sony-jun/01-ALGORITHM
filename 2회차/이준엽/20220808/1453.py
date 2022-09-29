n = int(input())
numbers = list(map(int,input().split()))
cnt = 0
favorite = []
for number in numbers:
    if number in favorite:
        cnt+=1
    else:
        favorite.append(number)
print(cnt)