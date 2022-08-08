a = []
total = 0

for _ in range(9): # 난쟁이 9명 
    dwarf = int(input()) # 난쟁이들의 키 값을 입력받는다
    a.append(dwarf) # 리스트에 난쟁이들의 키를 추가
    total += dwarf # 난쟁이들 키의 합 

    for i in range(len(a)): # a의 길이 범위 
        for j in range(i+1, len(a)): # a의 다음 길이 범위
            if 100 == total - (a[i] + a[j]): # 전체에서 난쟁이와 그 다음 난쟁이의 합을 뺐을 때 100이라면? 
                no_dwarf1, no_dwarf2 = a[i], a[j] # 얘들은 난쟁이가 아님. 


a.remove(no_dwarf1)
a.remove(no_dwarf2)
a.sort() # 오름차순 정렬 
for k in range(len(a)):
    print(a[k])



