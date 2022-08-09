# 백준 1526

# 은민이는 4와 7을 좋아하고, 나머지 숫자는 싫어한다. 금민수는 어떤 수가 4와 7로만 이루어진 수를 말한다.

# N이 주어졌을 때, N보다 작거나 같은 금민수 중 가장 큰 것을 출력하는 프로그램을 작성하시오.


n = int(input())

while True:                                                     # 입력값보다 작거나 큰 금민수 중에서 가장 큰 수를 구해야 하기 때문에 입력값에서부터 -1씩 해줌
    result = True
    for i in str(n):                                            # 검색해보니 4, 7 을 찾기위해서 str로 변환해야한다고 나왔음.. 
        if i!="4" and i!="7":   
            result = False                                      # 입력수를 str로 변환해 '4'이거나 '7'이 아닌 경우 result는 False
            n -= 1
            
    if result:                                                  # result가 True일 경우에 n을 출력하게 된다. 
        print(n)
        break