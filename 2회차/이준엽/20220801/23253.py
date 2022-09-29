import sys
input = sys.stdin.readline

n,m = map(int,input().split())
stack_list = []
answer = 'Yes'
for i in range(m):
    cnt = int(input())
    books = list(map(int,input().split()))
    stack_list.append(books)

for stack in stack_list:
    comparison = stack.pop()
    
    while len(stack) != 0:
        if stack[-1] > comparison:
            comparison = stack.pop()
        else:
            answer = 'No'
            break
    if answer == 'No':
        break
print(answer)



# import sys
# input = sys.stdin.readline

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



# import sys
# input = sys.stdin.readline

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
