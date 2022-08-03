number_list = [int(input()) for i in range(10)]
# print(number_list)
result = 0

for i in number_list:
    result+=i
    if result > 100 :
        if result-100 > 100 - (result-i):
            result-=i
            break
        else:
            result=result
            break
print(result)
            
                       
# num_list = [int(input()) for i in range(10)]
# # print(number_list)
# result = 0

# for i in num_list:
#     result+=i
#     if result>100:

#         if result-100 > 100-(result-i):
#             result-=i
#             break
#         elif result-100 <= 100-(result-i):
#             result=result
#             break
# print(result)
            

# score=0
# for i in range(10):
#     n=int(input())
#     score+=n
#     if score>=100:
#         if score-100 > 100 - (score -n):
#             score-=n
#         break
# print(score)


# # arr = []
# # sum = 0

# # for i in range(10):
# #     arr.append(int(input()))

# # if 100 in arr:
# #     print('100')
# # else:
# #     for i in arr:
# #         sum += i
# #         if sum >= 100:
# #             if sum - 100 > 100 - (sum - i):
# #                 sum -= i
# #                 break

# #     print(sum)