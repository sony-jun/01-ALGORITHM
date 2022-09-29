S = input().upper() # 입력받는 값을 전부 대문자로 받음
A = list(set(S)) # 입력받은 값을 세트에 넣어서 중복 제거 ['M', 'I', 'S', 'P']
cnt = [] # 문자의 개수를 담을 리스트
max = 0 # 담긴 개수 중 최대값을 구할 변수 

for i in A: # ['M', 'I', 'S', 'P'](순서 없음)
    count = S.count(i) # 1, 4, 4, 1 
    cnt.append(count) # [1, 4, 4, 1]

for j in range(len(cnt)): # 카운트 리스트 길이동안
    if max < cnt[j]: # 리스트 내 카운트 중 최대값 구하기
        max = cnt[j]

if cnt.count(max) >= 2: # max인 카운트가 2개 이상 존재할 경우 
    print("?")
else:
    print(A[cnt.index(max)]) # cnt내의 max카운트를 가진 index를 가져오고
                             # A에 인덱스에 해당하는 값을 출력