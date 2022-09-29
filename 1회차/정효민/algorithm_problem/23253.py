import sys



sys.stdin = open('23253.txt')
n , m = map(int ,input().split())

result = True

for i in range(m):
     x = int(input())
     k = list(map(int , input().split()))
     
     for y in range(x-1):
         if k[y] < k[y+1]:
             result = False
             break

# print('Yes' if result else 'No') 

if result == True:
    print('Yes')
else:
    print('No')



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




