num = input()
disassem_num = []
disassem_sum = 0
disassem_none = 0

#disassem_sum = int(num) + sum(map(int, num))
#print(disassem_sum)

for i in range(1, int(num) + 1):
    disassem_sum = i + sum(map(int, str(i)))
    #print(disassem_sum)
    if disassem_sum == int(num):
        disassem_num.append(i)
        break
    else:
        disassem_num.append(0)        
print(disassem_num[-1])
