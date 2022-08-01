#2902_ kmp는 왜 kmp일까
name = list(map(str,input().split('-')))  #이름의 값을 리스트로 받아온다

for i in name:  #name 리스트에서
    print(i[0], end='')  
      #i가 각 이름의 값이 오기 때문에 i[0]을 하면 첫번째 알파벳만 구할 수 있음
      #모든 값을 print해서 값 찾아냈다,,,;


#14720 _우유축제 

#아래는 잘못된 코드
n = int(input())
milk = list(map(int, input().split()))
cnt = 0

for i in range(len(milk)) : 
    if i+1 > i :
        cnt += 1  #0 1 2 다음에 2에서 0으로 계산이 안 됨
    else :
        cnt = 0
    
print(cnt)

#고친 코드
cnt = 0

length = int(input())
menu = list(map(int, input().split()))

order = [0, 1, 2]
for i in range(length):
    if menu[i] == order[cnt % 3]:  #0 1 2 이므로 3으로 나눈 나머지가 같으면 cnt += 1 로 만들기
        cnt += 1

print(cnt)