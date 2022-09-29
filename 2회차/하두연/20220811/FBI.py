# 백준 2857

# 5명의 요원 중 FBI 요원을 찾는 프로그램을 작성하시오.

# FBI요원은 요원의 첩보원명에 FBI가 들어있다. 


agent = []

for i in range(5):                              # 5명의 요원 첩보원명을 입력받아 리스트에 저장
    agent.append(input())

cnt = 0                                         

for j in range(len(agent)):                     # 첩보원명에 FBI란 단어가 들어가 있으면 인덱스 번호 + 1을 출력하고 cnt는 1로 갱신
    if 'FBI' in agent[j]:
        print(j+1, end = ' ')
        cnt = 1
    
if cnt == 0:                                    # cnt 값이 0이면 FBI 요원이 없기때문에 'HE GOT AWAY!' 출력
    print('HE GOT AWAY!')
