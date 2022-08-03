import sys
sys.stdin = open('B2902.txt')

names = list(input().split('-'))
# print(names)
for i in names:
    #a = list(i) 문자열도 인덱싱 
    print(i[0], end='')
    
   # .isupper()