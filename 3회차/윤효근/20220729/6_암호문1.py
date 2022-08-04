import sys

sys.stdin = open("암호문1.txt", "r")

for i in range(10):

    n = int(input())
    original = input().split()

    c_cnt = int(input())
    command = input().split()

    result = original

    for j in range(len(command)):
        if command[j] == 'I':
            start = int(command[j+1])
            length = int(command[j+2])
            result = result[:start] + command[j+3: j+3+length] + result[start:]
    print(f'#{i+1}',end=' ')
    for k in range(10):
        print(result[k], end=' ')

