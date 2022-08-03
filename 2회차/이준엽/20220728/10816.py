n = int(input())
n_numbers = list(map(int,input().split()))

m = int(input())
m_numbers = list(map(int,input().split()))

result = {}

for i in m_numbers:
    result[i] = 0

for i in n_numbers:
    if i in result:
        result[i] += 1

for i in m_numbers:
    print(result[i],end=' ')

















# n = int(input())
# numbers = list(map(int,input().split()))

# m = int(input())
# solnumbers = list(map(int,input().split()))

# result = {}

# for j in numbers:
#     if j not in result:
#         result[j] = 1
#     else:
#         result[j] += 1

# for i in solnumbers:
#     print(result.get(i,0), end = ' ')



# import sys
# input=sys.stdin.readline

# n = int(input())
# numbers = list(map(int,input().split()))
# m = int(input())
# solnumbers = list(map(int,input().split()))

# result = {}

# for i in solnumbers:
#     result[i] = 0

# for j in numbers:
#     if j in solnumbers:
#         result[j]+=1

# for i in list(result.values()):
#     print(i, end=' ')


# ####  2.

# n = int(input())
# have_card = list(map(int, input().split()))

# m = int(input())
# check_card = list(map(int, input().split()))

# count_dic = {}

# for i in have_card:
#     if i not in count_dic:
#         count_dic[i] = 1
#     else:
#         count_dic[i] += 1

# for i in check_card:
#     print(count_dic.get(i, 0), end=' ')