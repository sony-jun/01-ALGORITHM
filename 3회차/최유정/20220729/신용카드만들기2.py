T = int(input())

for i in range(1,T+1):
    cardnum = input()
    str = cardnum.replace('-', '')#-제거
    
   
    if len(str) == 16 and str[0] in ['3','4','5','6','9']:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')
   