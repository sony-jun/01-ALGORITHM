


num1, num2 = map(int, input().split())
max_num = max(num1,num2)
min_num = min(num1,num2)

def gcd(num1, num2): #gcd 최대공약수

    if max_num % min_num == 0:
        return min_num
    else:
        return max_num % min_num


def lcm(num1, num2): #lcm 최소공배수
  
    if max_num % min_num == 0:
        return max_num
    elif max_num % min_num == 1:
        return min_num * max_num
    else:
        r = max_num % min_num 
        q1 = max_num // r
        q2 = min_num // r
        return  r*q1*q2
    

print(gcd(num1,num2))
print(lcm(num1,num2))