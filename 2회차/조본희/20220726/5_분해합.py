N = int(input())

result = 0
for i in range(1, N+1):
    #없는경우
    if i == N:
        print(0)
        break
    
    test_case = list(map(int, str(i)))
    result = i + sum(test_case)
    if result == N:
        print(i)
        break

