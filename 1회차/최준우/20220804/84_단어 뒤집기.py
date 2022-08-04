# https://www.acmicpc.net/problem/9093

T  = int(input())

for test_case in range(T):
    sentence = list(map(str, input().split()))
    result = ''

    for i in range(len(sentence)):
        result += sentence[i][::-1]
        result += ' '
    print(result)