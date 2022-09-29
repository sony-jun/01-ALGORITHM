def gcd(n, m):
    big = n if n > m else m
    small = m if n > m else n
    
    while small != 0:
        temp = small
        small = big % small
        big = temp
       
    return big
    
    
def lcm(n, m):
    return n // gcd(n, m)  * m

n, m = map(int, input().split())

print(gcd(n, m))
print(lcm(n, m))