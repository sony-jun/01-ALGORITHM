# https://www.acmicpc.net/problem/2609
# A,B의 최대공약수가 G이고, 최소공배수가 L일때
# A = a*G, B = b*G (a,b는 서로소), L = a*b*g, A*B = G*L

a, b = map(int,input().split())
nums = []
for i in range(1, a+b+1):
    if a % i == 0 and b % i == 0:
        nums.append(i)

G = max(nums)
L = (a * b) // G   
print(G, L, sep='\n')

