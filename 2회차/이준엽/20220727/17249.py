n = input()
left = 0
right = 0

for i in n:
    if i == '@':
        left+=1
    elif i == '(':
        break      
        
for i in n[::-1]:
    if i == '@':
        right+=1
    elif i ==')':
        break
print(left,right)
        