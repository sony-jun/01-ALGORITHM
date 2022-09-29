# 1065.
"""
"""
N = int(input())
seq = 0 
for num in range(1, N +1):
    defer = set()
    number = str(num)
    if len(number) <= 2:
        seq += 1
    else:
        for idx in range(len(number)):
            if 1 <= idx + 1 <= len(number) -1:
                defer.add(int(number[idx + 1]) - int(number[idx]))

        if len(defer) == 1:
            seq += 1
            
print(seq)