# T = int(input())
# for test_case in range(1,T+1):
    
#     print(f'#{test_case}',result)
s=input()
s = s.replace('b','1')
s = s.replace('d','2')
s = s.replace('1','d')
s = s.replace('2','b')
s = s.replace('p','1')
s = s.replace('q','2')
s = s.replace('1','q')
s = s.replace('2','p')
print(s[::-1])