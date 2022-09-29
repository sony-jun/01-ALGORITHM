# 2920

words = list(map(int, input().split()))
# print(words)

if words == list(range(1, 9)):
    print('ascending')
    
elif words == list(range(8, 0, -1)):
    print('descending')
    
else:
    print('mixed')