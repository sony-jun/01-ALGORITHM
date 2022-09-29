# https://www.acmicpc.net/problem/2846
import sys
sys.stdin = open('2846.txt', 'r')

n = int(input())
height = list(map(int, input().split()))
uphill = []
gap = 0

for i in range(n - 1):
    
    if height[i] < height[i + 1]: #[i - 1]를 하면 젤 첫번째 반복에서 에러 뜸
        gap += height[i + 1] - height[i]
        # 첫값과 끝값을 빼야하기 때문에 값누적해서 최종값이 오르막길 높이
    if height[i] >= height[i + 1]:
        uphill.append(gap)
        gap = 0
        
uphill.append(gap) # 이 라인이 없으면 오르막길인채로 끝났을때꺼 반영 안 됨
# 오르막길이 아니면 0 출력

 
print(max(uphill)) # 반복문 끝나고 넣어도 됨
