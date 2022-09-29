# 두 집합의 대칭 차집합의 원소의 개수를 출력하는 프로그램을 작성하시오.
# 차집합들을 더한다.
# setA-setB : 차집합. setA|setB : 합집합

N = map(int,input().split())
A = set(map(int,input().split())) # 빈 set에 입력값을 더한다.
B = set(map(int,input().split()))
print(len((A-B)|(B-A))) # 차집합의 합집합의 길이를 구한다.