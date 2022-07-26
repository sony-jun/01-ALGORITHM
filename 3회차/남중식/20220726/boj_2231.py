N = int(input())

# 분해합의 생성자는 원래 수보다는 작을 것.
for i in range(1, N):
    # 생성자를 통해 분해합을 구하는 식
    decom_i = i+sum(map(int, str(i)))
    
    if decom_i == N:
        print(i)
        break
else:
    print(0)
        