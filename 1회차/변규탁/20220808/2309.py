# shorts = []

# for _ in range(9):
#     cm = int(input())
#     shorts.append(cm)

# shorts.sort()    
# total = sum(shorts) - 100

# left, right = 0, len(shorts) - 1
# while left < right :
#     if shorts[left] + shorts[right] == total:
#        shorts.remove(shorts[left])
#        shorts.remove(shorts[right-1])
#        break
#     elif shorts[left] + shorts[right] > total:
#         right -= 1
#     elif shorts[left] + shorts[right] < total:
#         left += 1


# print(*shorts, sep ='\n')


shorts = []

for _ in range(9):
    cm = int(input())
    shorts.append(cm)
sum_ = sum(shorts)

shorts.sort()
a, b = 0,0
for i in range(9):
    for j in range(i+1,9):
        if sum_ - (shorts[i]+shorts[j]) == 100:
            a = shorts[i] 
            b = shorts[j] 
            break

shorts.remove(a)
shorts.remove(b)

print(*shorts, sep='\n')
    



