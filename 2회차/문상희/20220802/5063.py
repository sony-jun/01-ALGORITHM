test_case = int(input())
answer =''

for test in range(test_case):
    r, e, c = map(int, input().split())
    if r > e - c:
        answer = 'do not advertise'
    elif r == e - c:
        answer = 'does not matter'
    else:
        answer = 'advertise'
    print(answer)