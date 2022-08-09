# 영문 문장을 입력받아 모음의 개수를 세는 프로그램을 작성하시오. 

v = ['a','i','u','o','e'] # 모음 리스트

while True:
    v_count=0
    s=input() # 문자열 입력
    if s=="#": # 멈추고
        break
    s=s.lower()
    for i in v: 
        v_count+= s.count(i) # 모음의 개수 저장 
    print(v_count) # 모음의 개수 출력