def solution(s):

    

    answer = 0
    return answer

mixed = '12'
mixed_list = list(mixed)
restore_num = []

for i in range(len(mixed_list) - 2):
    #print(i)
    if 48 < ord(mixed_list[i]) <57:
        #print(mixed_list[i])
        restore_num.append(mixed_list[i])
    elif mixed_list[i] == 'z' and mixed_list[i + 1] == 'e' and mixed_list[i + 2] == 'r':
        #print(0)
        restore_num.append(0)
    elif mixed_list[i] == 'o' and mixed_list[i + 1] == 'n' and mixed_list[i + 2] == 'e':
        #print(1)
        restore_num.append(1)
    elif mixed_list[i] == 't' and mixed_list[i + 1] == 'w' and mixed_list[i + 2] == 'o':
        #print(2)
        restore_num.append(2)
    elif mixed_list[i] == 't' and mixed_list[i + 1] == 'h' and mixed_list[i + 2] == 'r':
        #print(3)
        restore_num.append(3)
    elif mixed_list[i] == 'f' and mixed_list[i + 1] == 'o' and mixed_list[i + 2] == 'u':
        #print(4)
        restore_num.append(4)
    elif mixed_list[i] == 'f' and mixed_list[i + 1] == 'i' and mixed_list[i + 2] == 'v':
        #print(5)
        restore_num.append(5)
    elif mixed_list[i] == 's' and mixed_list[i + 1] == 'i' and mixed_list[i + 2] == 'x':
        #print(6)
        restore_num.append(6)
    elif mixed_list[i] == 's' and mixed_list[i + 1] == 'e' and mixed_list[i + 2] == 'v':
        #print(7)
        restore_num.append(7)
    elif mixed_list[i] == 'e' and mixed_list[i + 1] == 'i' and mixed_list[i + 2] == 'g':
        #print(8)
        restore_num.append(8)
    elif mixed_list[i] == 'n' and mixed_list[i + 1] == 'i' and mixed_list[i + 2] == 'n':
        #print(9)
        restore_num.append(9)
if len(mixed_list) >= 2 and 48 < ord(mixed_list[len(mixed_list) - 2]) <57:
    #print(mixed_list[len(mixed_list) - 1])
    restore_num.append(mixed_list[len(mixed_list) - 2])
if len(mixed_list) >= 1 and 48 < ord(mixed_list[len(mixed_list) - 1]) <57:
    #print(mixed_list[len(mixed_list) - 1])
    restore_num.append(mixed_list[len(mixed_list) - 1])

print(''.join(map(str, restore_num)))