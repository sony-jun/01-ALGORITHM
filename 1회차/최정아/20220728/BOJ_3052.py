# set은 집합 선언하고, {} 형태로 저장된다
# set은 중복되는 값들은 1개로 처리
a=set()

# add() 사용해서 집합 요소 추가
for i in range(10):
    # input을 통해 받은 값을 정수형으로 바꾸고 
    # 42로 나눈 나머지 값을 추가
    # 이 때 중복되는 값들은 1개로 처리
    a.add(int(input())%42)

print(len(a))