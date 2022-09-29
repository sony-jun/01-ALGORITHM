# import sys 

# input = sys.stdin.readline

# n, m = map(int, input().split())
# flag = False

# for _ in range(m):
#     book_len = int(input())
#     books = list(map(int, input().split()))
    

#     for i in range(book_len-1):
#         if books[i] < books[i + 1]:
#             print("No")
#             flag = True # flag는 변한다
#             break
#     if flag: # if flag == True이면 break 
#         break
# #케이스 변화가 있으면 두개가 출력되고 케이스 변화가 없으면 그대로 출력된다.
# if flag == False:  
#     print("Yes")

# import sys 

# input = sys.stdin.readline

# n, m = map(int, input().split())

# for _ in range(m):
#     book_len = int(input())
#     books = list(map(int, input().split()))
    

#     for i in range(book_len-1):
#         if books[i] < books[i + 1]:
#             print("No")
#             #테스트케이스를 아예 끝내버린다
#             exit()

# print("Yes")


from inspect import stack
import sys 

input = sys.stdin.readline

n, m = map(int, input().split())

answer = "Yes"
for _ in range(m):
    book_len = int(input())
    books = list(map(int, input().split()))
    #비교할 값을 먼저 pop해준다
    comparison = books.pop()
    #books의 요소가 남아있을 때까지
    while len(books) != 0:
        #top이 comparsion보다 크다면
        if books[-1] > comparison:
            #comparsionn에 books의 탑을 pop해준것을 할당해준다
            comparison = books.pop()
        # 아니면 No를 해주고 break해준다
        else:
            answer = "No"
            break
#맞으면 yes
print(answer)


