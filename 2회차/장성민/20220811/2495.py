import sys
sys.stdin = open('2495.txt')

for _ in range(3):
    line = input()

    result = 0
    for i in range(len(line)):
        start = line[i]

        cnt = 1
        for j in range(i + 1, len(line)):
            if start != line[j]:
                break
            if start == line[j]:
                cnt += 1

        result = max(result, cnt)

    print(result)
