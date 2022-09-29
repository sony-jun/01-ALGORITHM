#학교를 입력받아준다.
u1, u2, u3 = map(int, input().split())

#만약 세 학교의 참여도 합이 100 이상이면 ok를 출력
if u1 + u2 + u3 >= 100:
    print("OK")
#아니면 압박을 넣어준다.
else:
    #기준값이 100이니까 변수에 받아주고
    rate = 100
    #기준값보다 미만인 학교들은 값을 담아준다. 
    name = ""
    if rate > u1:
        rate = u1
        name = "Soongsil"
    
    if rate > u2:
        rate = u2
        name = "Korea"
    
    if rate > u3:
        rate = u3
        name = "Hanyang"

    print(name)