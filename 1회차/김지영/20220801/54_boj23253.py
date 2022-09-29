# 교과서 N권을 M개의 더미로..?
# 번호순 나열
# i번째 더미 첫번재 줄, 더미에 쌓인 교과서 수 ki, 
# 교과서넘버 공백구분

n,m = map(int,input().split())  # 교과서 몇권? ,# 교과서 몇더미? 
book = []
result = 'Yes'
for i in range(m):
    bunch = int(input())
    book_num = list(map(int,input().split()))
    book.append(book_num)
# n,m = 4,2
# book = [[3,1],[4,2]]
for stack in book:
    comp = stack.pop()
    while len(stack) != 0:
        if stack[-1] > comp:
            comp = stack.pop()
        else :  
            result = "No"
            break
        print(stack,comp)
print(result)
