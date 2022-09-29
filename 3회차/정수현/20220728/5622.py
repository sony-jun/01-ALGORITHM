# PQRS / TUV / WXYZ
# 8      9     10

pn = input()
seconds = 0
for i in pn:
    if ord(i) >= 87:
        seconds += 10    
    elif ord(i) >= 84:
        seconds += 9
    elif ord(i) >= 80:
        seconds += 8    
    else:
        seconds += (ord(i) - ord('A'))//3 + 3
print(seconds)