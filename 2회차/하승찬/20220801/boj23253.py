import sys
# sys.stdin = open("input.txt", "r")
# n,m= map(int,input().split())

# books =[]
# for __ in range(m):
#     book_ea=input()
#     list_=[]
#     list_=list(map(int,input().split()))
#     books.append(list_)


# print(books[0],type(books[0]))
# for sq in range(1,n+1):
#        for sq1 in range(m):
#         if books[sq1].pop(books[0]) == sq: #리스트안의 리스트는 pop매서드 적용이안됨.
#             pass
#         else:
#             print('NO')
#             break
# print('YES')
import sys
input = sys.stdin.readline

n,m= map(int,input().split())


num= 0
for __ in range(m):
    book_ea=input()
    list_=[]
    list_=list(map(int,input().split()))
    if list_ != sorted(list_,reverse=True):
        num += 1


if num == 0:
    print('YES')
else:
    print('NO')


# for r in range(n):
#     if pop=