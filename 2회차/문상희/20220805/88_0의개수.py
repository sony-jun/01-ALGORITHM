test_case = int(input())

for test in range(test_case):
    check = list(map(int, input().split()))
    cnt = 0
    for i in range(check[0], check[1] + 1):
        if '0' in list(str(i)):
            cnt += list(str(i)).count('0')
    
    print(cnt)