import sys
sys.stdin = open("7. 일곱난쟁이.txt", "r")

K = [] # 9명 난쟁이 크기 들어갈 리스트
dwarf_1 = 0
dwarf_2 = 0
for _ in range(9):
    n = int(input())
    K.append(n)
    
    # 9명 난쟁이 크기의 합에서 2명의 난쟁이 크기를 뺐을 때 100이 나와야 함.
    # 어느 2개를 빼야 100이 되는지 모르기 때문에 경우의 수를 모두 찾아야 함
    
for i in range(9):
    for j in range(i+1,9):
        if sum(K) - (K[i] + K[j]) == 100: #총 합에서 난쟁이 2명을 골라 뺐을 때 100이면,
            dwarf_1 = K[i]
            dwarf_2 = K[j] # 합이 100이 나왔을 때 뺀 난쟁이 2명을 각각의 변수에 저장.
        
K.remove(dwarf_1)
K.remove(dwarf_2) # 합이 100이 나왔을 때 뺀 난쟁이 2명 리스트에서 제거
K.sort() # 오름차순

for t in K:
    print(t)