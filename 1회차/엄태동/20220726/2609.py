a,b = map(int, input().split())
list_a=[]
list_b=[]
# 반복문을 통한 공약수 만들기
def CommonFacotr(a,b):
    for i in range(a):
        if a %(i+1) ==0 and b%(i+1)==0:
            list_a.append(i+1)
    return list_a[-1]
        
# 반복문을 통한 공배수 만들기
def CommonMultiple(a,b):
    if a-b>0:
        num = b
    if a-b<0:
        num =a
    if a-b==0:
        num=a
    i=1
    while 1:
        num1 = num*i
        if (num1) % a ==0 and (num1) % b==0:
            list_b.append(num1)
            break
        i += 1
    return list_b[0]

solution1 = CommonFacotr(a,b)
solution2 = CommonMultiple(a,b)
print(solution1)
print(solution2, end='')

#시간 초과
# 너무 많은 횟수를 반복해야 해서 그런 듯

# a,b = map(int, input().split())
# list_a=[]
# list_b=[]
# # 반복문을 통한 공약수 만들기
# def CommonFacotr(a,b):
#     for i in range(a):
#         if a %(i+1) ==0 and b%(i+1)==0:
#             list_a.append(i+1)
#     return list_a[-1]
        
# # 반복문을 통한 공배수 만들기
# def CommonMultiple(a,b):
#     num = a*b
#     for i in range(num):
#         if (i+1) % a ==0 and (i+1) % b==0:
#             list_b.append(i+1)
#     return list_b[0]

# solution1 = CommonFacotr(a,b)
# solution2 = CommonMultiple(a,b)
# print(solution1)
# print(solution2, end='')


    