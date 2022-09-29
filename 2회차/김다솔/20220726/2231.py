# https://www.acmicpc.net/problem/2231
# 1~n= i, i+i자리수 합계 = n 이면 그게 분해합 멈추기 
# 끝가지했는데 없으면 0 출력 

n = int(input())
for i in range(1, n+1): # 모든 경우의 수를 돌려보는 방법 = brute force
    ctor = i + sum(map(int, str(i))) # i 문자열로 바꾸고 하나씩 인티저로 바꿔서 리스트화
    
    if n == ctor:
        print(i)
        break
    
    elif i >= n: # else: print(0) 하니까 반복문 돌면서 아닐때 계속 0 나옴ㅜ 
        print('0')
        
# for-else 도 활용 가능