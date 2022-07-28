A, B = map(int, input().split())
l = []

for i in range(B+1): #B구간 까지 수열 만들기
    for j in range(i): # i의 값이 0인 경우 j의 값은 없음
        l.append(i) # B구간 까지의 수열을 리스트에 넣기

print(sum(l[A-1:B])) # A부터 B까지의 수를 합하기
