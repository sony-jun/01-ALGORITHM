A , B = map(int ,input().split())
max_com = 0
for a in range(1 , min(A,B)+1) :
    if A % a ==0 and  B % a == 0:
        great_com = a
     
max_com = (A * B) // great_com

print(great_com,max_com)


        