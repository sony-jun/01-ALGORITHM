from re import A
import sys

sys.stdin = open("input2957.txt")

number_FBI = [] #FBI요원의 번호

for i in range(5): #반복문을 통해 FIB 5명의 첩보원명을 체크.
    word = list(map(str, sys.stdin.readline().strip()))
    # print(word) ; ['N', '-', 'F', 'B', 'I', '1']
    #반복문과 if문을 통해 FBI요원을 찾는다.
    for j in range(len(word)): 
        #FBI요원을 찾으면 number에 추가해주고 break
        if word[j] == 'F' and word[j+1] == 'B' and word[j+2]== 'I': # 각 요소별로 꺼내야 함
            number_FBI.append(i +1)
            break

if number_FBI:
    print(*number_FBI) #리스트 형식을 푸는건데? 
else:
    print("HE GOT AWAY!")

#==============값에러

# number_FBI = [] #FBI요원의 번호

# for i in range(5): #반복문을 통해 FIB 5명의 첩보원명을 체크.
