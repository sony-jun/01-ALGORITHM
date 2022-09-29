# 당신은 SASA 연못에서 알파벳 S 모양의 블록 N개와 알파벳 A 모양의 블록 M개를 건졌다. 
# 태영이는 연못에서 건진 블록을 이용해 학교에 전시할 SASA 모형을 최대한 많이 만들려고 한다.


S,A = map(int,(input().split())) 
S_result = S//2 
A_result = A//2  
                

if S_result < A_result: 
    print(S_result)
else:
    print(A_result)


 # 
#     S_result += "S"
# print(S_result)

# A_result = []
# for j in range(A):
#     A_result += "A"
# print(A_result)

# D= ("S"+"A")
# print(D)
#



# SASA 모형 1개를 만들기 위해서는, 알파벳 S 모양의 블록 2개와 알파벳 A 모양의 블록 2개가 필요하다.
#  태영이가 만들 수 있는 SASA 모형 개수의 최댓값을 구하라.

# 입력
# 첫째 줄에 알파벳 S 모양의 블록의 개수 N과 알파벳 A 모양의 블록의 개수 M이 공백으로 구분되어 주어진다.