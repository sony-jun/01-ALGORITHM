total_score = 0
lst = []
lst2 = []
for i in range(10):
    score = int(input())
    total_score+=score

    if total_score > 100:

        if abs(100-lst[-1]) < abs(100-total_score):
            lst2.append(lst[-1])
        else:
            lst2.append(total_score) 
            
    elif total_score <= 100:    
        lst.append(total_score)

print(lst2[0]) if total_score > 100 else print(total_score)