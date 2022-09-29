lst = []
start ,end = input().split()
start = int(start)
end = int(end)

for i in range(1,1000):
    lst.append(i)
    for j in range(0,i-1):
        lst.append(i)
print(sum(lst[start-1:end]))