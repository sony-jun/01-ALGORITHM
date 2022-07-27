num = input()

for i in range(int(num)) :
    vs = i
    for j in str(i) :           # i의 분해합 만들기.
        vs += int(j)

    if vs == int(num) :          # i의 분해합 vs가 num과 같다면 i는 num의 생성자. 
        print(i)
        break                   #  최솟값만 프린트하기 위해 break을 씀 

    elif i == int(num)-1 :        # 앞에서 break없이 i가 끝까지 돌았다면 num의 생성자가 없는 것.
        print(0)
        break