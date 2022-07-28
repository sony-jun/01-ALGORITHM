apb = input()
nums = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
sec = 0

for i in range(len(apb)):
    for n in nums:
        if apb[i] in n:
            sec += nums.index(n) + 3
print(sec)
