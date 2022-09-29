import sys
sys.stdin = open("5. 가장 큰 금민수.txt", "r")
input = sys.stdin.readline

#   N보다 작거나 같은 금민수(4와 7로만 이루어진 수) 중 가장 큰 것을 출력 

N = int(input()) # 자연수 입력
number = []
for i in range(N+1):
    # 0부터 N까지 반복
    
    if len(str(i)) == str(i).count('4') + str(i).count('7'):
    # 문자열(i)의 길이 = 문자열 i의 4의 갯수 + 문자열 i의 7의 갯수
    # '474747' 6  /     '4' 3개       /      '7' 3개         6 = 3 + 3  
    #   474   3   /     '4' 2개       /      '7' 1개         3 = 2 + 1   
    
        number.append(i)
    # 순회해서 위 조건에 맞는 값들을 number 리스트에 저장    
number.sort(reverse=True)
# 내림차순 정렬 (제일 큰 값이 맨 앞)
print(number[0]) 
# 맨 앞 값 출력
   
        
    