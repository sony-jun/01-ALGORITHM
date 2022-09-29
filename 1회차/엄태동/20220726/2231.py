# Number = int(input())
# # 216 = num1 +(num1의 일의자리들의 합)
# list_a=[]
# for i in range(1,Number+1):
#     n = i
#     # print(i,'======')
#     sum_=0
#     # i의 일의 자리의 합 구하기
#     while 1:
#         n1 = n % 10
#         sum_ += n1
#         n = n//10
#         # print(sum_)
#         if n == 0:
#             break
#     if Number == (i + sum_):
#         # print("======")
#         list_a.append(i)
# print(list_a[0], end='')

# 아래 코든는 시간이 좀 걸림 1312ms 시간 줄일 수 있는 방법?
Number = int(input())
list_a=[]
for i in range(1,Number+1):
    n = i
    sum_=0
    while 1:
        n1 = n % 10
        sum_ += n1
        n = n//10
        if n == 0:
            break
    if Number == (i + sum_):
        list_a.append(i)
        print(list_a[0], end='')
        break
if len(list_a) == 0:
    print(0, end='')