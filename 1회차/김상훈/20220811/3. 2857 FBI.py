import sys
sys.stdin = open("3. FBI.txt", "r")

input = sys.stdin.readline

agent_list = []
agent_number = []

for _ in range(5): # 5번 반복
    agent = input() # 요원 이름 입력
    agent_list.append(agent) # 요원 이름들을 리스트에 저장

for i in range(len(agent_list)): # 리스트 길이만큼 반복 (5번)
    if 'FBI' in agent_list[i]: # 순회하는 리스트 요소마다 'FBI'가 있으면.
        agent_number.append(i) # agent_number 리스트에 인덱스 값(i)을 저장
        
if not agent_number: # agent_number 리스트에 아무것도 없다면
    print('HE GOT AWAY!') # FBI 요원이 없는 것.
    
else: # 리스트에 무언가 있으면,
    for i in agent_number: 
        print(i+1,end=' ') # FBI 요원의 번호를 공백을 두고 이어 출력함.