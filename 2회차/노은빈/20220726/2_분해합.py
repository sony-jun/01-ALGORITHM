n = int(input())

for m in range(1, n+1):
    l = list(map(int, str(m)))  #m은 생성자
    # str(m) - m인 숫자를 문자열로 만들어줌
    # map(int, str(m)) - 문자열로 되어있는 각 자릿수를 정수로 변경
    # ex) 234->2,3,4로 바꿈
    res = m + sum(l)  #i와 리스트의 합은 결과
    if n == res :  
        print(m)
        break
else :
    print('0')
