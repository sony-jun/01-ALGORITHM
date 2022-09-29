# n = int(input())
# numbers = list(map(int,input().split()))
# higher = numbers[0]
# lower = numbers[0]

# result = []
# # 12 2 1 0 1 2 3 4
# for i in numbers:
#     if i > higher:
#         if higher>lower:
#             lower = lower
#             higher = i
#             result.append(higher-lower)
#         else:
#             lower = higher
#             higher = i
#             result.append(higher-lower)
#     else:
#         higher = i
#         lower = i

# if result == []:
#     print(0)
# else:
#     print(max(result))


n = int(input())
list_ = list(map(int,input().split()))

sum_ = 0

sum_list = []

for i in range(1,len(list_)):
    if list_[i] > list_[i-1]:
        sum_+=list_[i]-list_[i-1]
        sum_list.append(sum_)
    else:
        sum_=0
if sum_list != []:
    print(sum_list)
else:
    print(0)