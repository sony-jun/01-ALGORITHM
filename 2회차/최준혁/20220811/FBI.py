#첫째 줄에 FBI 요원을 출력한다. 
#이때, 해당하는 요원이 몇 번째 입력인지를 공백으로 구분하여 출력해야 하며,
#오름차순으로 출력해야 한다. 만약 FBI 요원이 없다면 "HE GOT AWAY!"를 출력한다.
a = []
cnt = 0
for _ in range(5):
    S = input()
    a.append(S)

for i in range(len(a)):
    if "FBI" in a[i]:
        a[i] = a[i].replace("FBI", "*")
        print(a.index(a[i])+1, end = ' ')
    else:
        cnt += 1
    
if cnt == 5:
    print("HE GOT AWAY!")
    

    


