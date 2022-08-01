#SASA 모형을 
s, a = map(int, input().split())

# if s >= 2 and a >= 2: # 두 수가 2개 이상이면
if s < a: # 더 작은 수의 절반을 출력
    print(s//2)
else:
    print(a//2)
# else: # 두수가 1이면 SASA를 못만드니까 0출력
#     print(0) 