import sys # 이 방법이 더 느리고, sys.stdin.readline()이 더 빠른데 
sys.stdin = open('B23253.txt')  # 굳이라고함

# N, M = map(int, input().split())
# for i in range(1, M+1):
#     k = int(input())
#     i = list(map(int, input().split()))
#     for l in range(k-1):
#         if i[l] < i[l+1]:
#             print['Yes']
#         else:
#             print('No')

s
for stack in stack_list: 
comparison = stack.pop()
while len(stack) != 0 # 스택 하나 남을때까지 반복
    if stack[-1] > comparison:
        comparison = stack.pop()
    else:
        answer = 'No'
        break
    
    # if answer == 'No':
        # break 답제출엔 괜찮지만 앞으로 효율좋은 개발자가 되려면 이런거 써주면 좋음!
print(answer)    
    