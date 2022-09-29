# 은민 love 4,7
n = int(input())
set_n = set(str(n))
# print(set_n)
while True:
    if n == 0:
        break
    
    set_n = set(str(n))
    if  set_n == {'4'} or set_n =={'7'} or set_n =={'4','7'}:
        break
    n -= 1
print(n)