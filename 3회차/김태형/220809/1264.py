# 영문 문장을 입력받아 모음의 개수를 세는 프로그램을 작성하시오. 

v = ['a','i','u','o','e']

while True:
    v_count=0
    s=input()
    if s=="#":
        break
    s=s.lower()
    for i in v:
        v_count+= s.count(i)
    print(v_count)