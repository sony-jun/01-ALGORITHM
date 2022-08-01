n,m = map(int,input().split(' '))

book = []
books = 0 #교과서더미
for i in range(m):
    temp = int(input())
    if books < temp :
        books = temp
    book.append(list(map(int,input().split(' '))))
print(book)

resultbooks = []

for j in range(m):
    for i in range(len(book)):
        resultbooks.append(book[i][m-1-j])

ox = 'no'
        
for i in range(books):
    if books % 2 == 1:
        if resultbooks[0] == 1 :
            ox = 'yes'
            print('y')
            pass
        else:
            break
    print(i)
    print(books)
    
            




print(resultbooks)