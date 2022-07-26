#1
n = int(input())
re = 0

for i in range(1, n+1):
    a=list(map(int, str(i)))
    boon=i+sum(a)
    if (boon==n):
        re=i
        break
print(re)

#2
n = int(input())
s = max(n-9*len(str(n)), 0) #n의 자릿수에 9를 곱한 값에 n을 뺀 값의 쵀대값
r = []

for i in range(s, n): # s에서 n-1의 범위로 정해서 좀 더 효율적으로 찾을 수 있다.
    if n==sum(map(int, str(i)))+i: # 범위 내의 숫자들 중에 분해합의 값이 n과 같은 경우
        r.append(i)  #r이라는 list에 넣어두기
if len(r)==0: #분해합이 없는 경우
    print('0')
else: # 분해합이 있는경우
    print(min(r)) # 그 중에 최소값을 출력