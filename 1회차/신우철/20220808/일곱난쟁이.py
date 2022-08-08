import sys
sys.stdin = open("일곱난쟁이.txt")
ki = [int(input()) for i in range(9)]
max_total = sum(ki)
for i in range(9):
    for j in range(1, 9):
        if 100 == max_total - (ki[i] + ki[j]):
            n1 = ki[i]
            n2 = ki[j]            
            ki.remove(n1)
            ki.remove(n2)
            ki.sort()
           
            for i in range(len(ki)):
               print(ki[i])
            break

    if len(ki)<9:
        break   

            
            

            
        