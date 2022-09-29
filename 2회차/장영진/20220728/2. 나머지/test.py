num_list = []
result_ = []

for tc in range(10):
    T = input()
    num_list.append(T)
        
for i in num_list:
    result_.append(int(i) % 42)

print(len(set((result_))))