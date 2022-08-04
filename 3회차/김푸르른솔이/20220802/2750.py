num = int(input())
a = []

for _ in range(num):
    x = int(input())
    a.append(x)
    
a.sort() #오름차순 정렬

for i in a: #정렬한 숫자 한개씩 추력
    print(i)