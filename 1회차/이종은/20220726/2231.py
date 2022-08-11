# 분해합
n = int(input())

result = 0
for i in range(1, n+1):
    a = list(map(int, str(i)))
    result = i + sum(a)
    
    #  1~ 198 까지 리스트로 출력
    # print(result) 1~216 두개씩 건너뛰어서 출력
    # print(i) 1~216
    if result == n: #n값 216과 result 값 같을 떄 i값 출력 
        print(i)
        break