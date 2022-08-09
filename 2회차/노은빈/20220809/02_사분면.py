import sys
input = sys.stdin.readline

n = int(input())  #점의 개수
axis = 0
q1 = 0
q2 = 0
q3 = 0
q4 = 0

for i in range(n) : #점의 개수만큼
    x, y = map(int, input().split()) #점의 위치 input 받기
    
    if x == 0 or y == 0: #x와 y 둘 중 하나라도 0이라면 
        axis += 1
    elif x > 0 and y > 0 :
        q1 += 1
    elif x < 0 and y > 0 :
        q2 += 1
    elif x < 0 and y < 0 :
        q3 += 1
    else:
        q4 += 1
   

print('Q1:', q1) 
print('Q2:', q2) 
print('Q3:', q3) 
print('Q4:', q4) 
print('AXIS:', axis)
#print(f'Q1 : {q1} \nQ2 : {q2} \nQ3 : {q3} \nQ4 : {q4} \nAXIS : {axis}')

#print 위치 주의,,
