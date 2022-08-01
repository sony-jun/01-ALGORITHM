import sys

input = sys.stdin.readline

N, M = map(int, input().split())

pos = []
for m in range(M):
    qty = int(input())
    b_num = list(map(int, input().split()))
    for i in range(len(b_num) - 1):
        if b_num[i] > b_num[i + 1]:
            pos.append(1)
        else:
            pos.append(0)

if 0 in pos:
    print('No')
else:
    print('Yes')




# n, m = map(int, input().split())
# p = True
# for _ in range(m):
#     i = int(input())
#     k = list(map(int, input().split()))
#     for j in range(i-1):
#         if k[j] < k[j+1]:
#             p = False
#             break
#     if not p: break

# print('Yes' if p else 'No') 





# n ,m = map(int,input().split())
# answer = []
# for i in range(m):
#     cnt = int(input())
#     books = list(map(int,input().split()))
#     for i in range(len(books)-1):
#         if books[i] < books[i+1]:
#             answer.append('No')
#             break
#         else:
#             answer.append('Yes')
#             continue
# if 'No' in answer:
#     print('No')
# else:
#     print('Yes')