T = int(input())
for test_case in range(1,T+1):
    length = list(map(int,input().split()))
    if length[0] == length[1]:
        result = length[2]
    elif length[1] == length[2]:
        result = length[0]
    elif length[0] == length[2]:
        result = length[1]
    elif length[0] == length[1] == length[3]:
        result = length[0]

    print(f'#{test_case}',result)
