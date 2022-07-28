# import sys
# sys.stdin = open("1_나머지.txt", 'r')

rest_dict = {}
for i in range(10):
    n = int(input())
    rest = n % 42
    
    if rest in rest_dict:
        rest_dict[rest] += 1
    else:
        rest_dict[rest] = 1
        
print(len(rest_dict))