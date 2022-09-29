#백준 FBI 2857
# 5명의 요원 중 FBI 요원을 찾는 프로그램을 작성하시오.
# FBI요원은 요원의 첩보원명에 FBI가 들어있다. 
count = 0
li = []
for i in range(1, 6):
    N = input()
    FBI = N.count('FBI')
    if FBI >= 1:
        count += 1
        li.append(i)
answer = sorted(li)        
if count == 0:
    print('HE GOT AWAY!')
else:
    print(*answer)