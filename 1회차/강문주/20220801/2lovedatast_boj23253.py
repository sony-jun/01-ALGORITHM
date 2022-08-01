                                                                 
n, m = map(int, input().split()) # 책 수, 더미 수 입력받기
p = True #가능여부확인
for _ in range(m):
    i = int(input()) #더미 갯수
    k = list(map(int, input().split())) #책 순서
    for j in range(i-1): # 더미 갯수까지 책순서 비교했을때 
        if k[j] < k[j+1]: #뒤쪽값이 크면 
            p = False #순차출력이 불가능
            break

print('Yes' if p else 'No')