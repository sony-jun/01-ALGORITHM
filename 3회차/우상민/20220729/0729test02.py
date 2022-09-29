# 소득불균형

T = int(input())

for i in range(1, T+1):
    N = int(input())
    count = 0
    result = 0
    total = 0
    earn = map(int,(input().split()))
    li = []
    for idx in earn:
        count += idx
        li.append(idx)
    total = count // N
    
    for index in li:
        if total >= index:
            result += 1
    print(f'#{i}',result)

