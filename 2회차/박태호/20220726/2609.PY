a, b = map(int, input().split())

def gcd(a,b): #유클리드 호제법 
    while b != 0:
        a,b = b,a%b  
    # 24,18 = 18,6
    # 18,6 = 6,0 여기서 b가 0이라 a 반환
    return a 
def lcm(a,b):
    return a*b // gcd(a,b)
  
print(gcd(a,b)) #최대공약수
print(lcm(a,b))  #최소공배수