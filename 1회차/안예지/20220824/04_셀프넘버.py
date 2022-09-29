# 4673

def self_number(x):
    answer.append(x + sum(map(int, str(x))))
    
answer = []
for i in range(1, 10001):
    self_number(i)
    if i not in answer:
        print(i)