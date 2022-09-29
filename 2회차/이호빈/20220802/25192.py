A = int(input())
gom = 0
set_ = set()
for i in range(A):
    log_list = list(map(str, input().split()))
    for log in log_list:
        if log == "ENTER":
            set_.clear()
        else:
            if log not in set_:
                set_.add(log)
                gom += 1

print(gom)
    
    

    


