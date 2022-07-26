
a, b = map(int,input().split())
i1 = 0
result = []
for i in range(1,min(a,b)+1):
    if a % i == 0 and b % i == 0:
        i1 = i
print(i1)
print(i1*a//i1*b//i1)

# a, b = map(int,input().split())

# result = []
# for i in range(1,min(a,b)+1):
#     if a%i == 0 and b%i == 0:
#         result.append(i)

# print(max(result))
# print(max(result)*(a//max(result))*(b//max(result)))

