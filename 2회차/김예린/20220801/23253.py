# 미완성

N, M = map(int, input().split())

for test_case in range(M):
    M_info = int(input())
    books = list(map(int, input().split()))

    for i in books:
        if books[i] > books[i+1]: # IndexError: list index out of range
            books = books.pop()
            break

        else:
            continue           # 아니면 걍 넘어가

if books.isEmpty() == True:
    print('YES')

else:
    print('NO')
 