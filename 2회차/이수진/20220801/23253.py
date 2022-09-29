import sys
input = sys.stdin.readline
n,m=map(int, input().split())
res='Yes'
for _ in range(m):
    input()
    book = list(map(int, input().split()))
    for i in range(len(book)-1) :
        if book[i] < book[i+1]:
            res='No'
            break
    if res == 'No':
        break
print(res)

# 책의 순서를 스택으로 비교할 필요 없이
# 각 책더미의 책들이 오름차순으로 쌓여있는지만 확인하면 됨.