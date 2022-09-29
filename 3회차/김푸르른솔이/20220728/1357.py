a, b = map(str, input().split())
sum_ = str(int(a[::-1]) + int(b[::-1]))
print(int(sum_[::-1]))

# a, b = map(str, input().split())
# a = int(a[::-1]) 
# b = int(b[::-1]) 
# print(int(str(a+b)[::-1])) 