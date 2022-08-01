# 자료구조는 정말 최고야

#N = 1~n 맨 위에 교과서만 꺼낼수 있음 (스택)
#N 교과서 수 , M 더미 수 
# M*2 더미 정보
import sys
sys.stdin = open('자료구조.txt','r')

n, m = map(int, sys.stdin.readline().split())

book = []
for _ in range(m*2):
    book.append(list(map(int,sys.stdin.readline().split())))
    #book = [['3'], ['3', '5', '1'], ['2'], ['4', '2']]
b_sort = (sorted(book[1]+book[3]))
# print(b)
stack_ = []
for i in range(n):
    # print(i)
    if len(book[1]) > 0 and len(book[3]) > 0:
        # print(book[1],book[3])
        if book[1][-1] < book[3][-1]:
            stack_.append(book[1].pop())
            
        else:
            stack_.append(book[3].pop())
# print(len(book[3]))
if len(book[1]) > 0:
    stack_+= book[1]
    if b_sort == stack_:
        print('Yes')
    else:
        print('No')
if len(book[3]) > 0:
    stack_+= book[3]
    if b_sort == stack_:
        print('Yes')
    else:
        print('No')
