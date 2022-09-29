number = int(input())
#666이 값에 있는지를 확인하기 위한 변수
n = 0 
#666이 있으면 하나씩 더해줄 변수
result = 0
# while 문을 사용한다.
while True:
    #만약 666이나 n을 int형으로 사용하면 not iterable이라서 str으로 처리해줬다.
    if "666" in str(n):
        result += 1
    #만약 결과값이 입력값과 일치하면 해당 값을 출력해준다.
    if result == number:
        print(n)
        break
    #일치하지 않으면 n에 계속 1을 해줘서 완전탐색을 통해서 계속 돌아준다.
    n += 1