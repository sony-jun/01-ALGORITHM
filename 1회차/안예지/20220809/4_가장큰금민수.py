# 1526.
"""
"""
N = int(input())

# 금민수 목록
list_47 = []
for num in range(4, N + 1):
# 4랑 7의 개수
    count_47 = 0
    if True:
        if '4' in str(num):
            count_47 += str(num).count('4')
        if '7' in str(num):
            count_47 += str(num).count('7')
    if len(str(num)) == count_47:
        list_47.append(num)

print(max(list_47))
        
    
