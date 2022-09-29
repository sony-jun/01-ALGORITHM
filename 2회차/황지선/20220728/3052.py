# 3052번 나머지

n= []

for i in range(10):
    # 수를 10번 입력받는다.
    a= int(input())
    # 입력받은 수를 42로 나눈 나머지를 b에 저장한다.
    b= a % 42
    # 리스트 n에 b를 넣는다.
    n.append(b)

# 리스트를 set으로 중복을 제거한 후 길이를 출력한다.
x= set(n)
print(len(x))