
n, m = map(int, input().split())
p = True

for _ in range(m): # 2번 반복
    i = int(input()) # 3입력 
    k = list(map(int, input().split())) # 3, 5, 1 입력 
    for j in range(i-1): # 2번 반복 (인풋값 3-1니까)
        if k[j] < k[j+1]: # 0, 1 각 인덱싱 값 비교 
            p = False # 5가 크니깐 p는 거짓 
            break
        if not p : break # p가 아니면 멈추기
print('Yes' if p else 'No') # p가 트루가 아니므로 no 출력 

