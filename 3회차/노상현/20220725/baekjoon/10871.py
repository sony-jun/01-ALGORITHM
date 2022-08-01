n, x = map(int, input().split())    # map 함수를 이용하여 정수로 입력받는다.
num = list(map(int, input().split()))   # num 변수를 만들어 숫자들을 리스트, 인트로 집어넣는다.

for i in range(n):  # for문을 이용해서 레인지를 돌려준다 n = 10 이므로 i는 0-9 까지 입력된다. 
    if num[i] < x:  # if 문을 이용해서 넘 리스트에 있는 숫자들이 x보다 작을때 프린트로 출력.
        print(num[i], end = ' ')     # end 로 한칸씩 뛰어서 출력.