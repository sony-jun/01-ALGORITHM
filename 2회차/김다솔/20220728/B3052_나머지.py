import sys
sys.stdin = open('B3052.txt')


r_list = [] #나머지 넣을 리스트
for i in range(10): #어차피 숫자 10개니까 
    num = int(input())
    #print(num)
    r = num % 42
    if r not in r_list:
        r_list.append(r)
    
print(len(r_list))