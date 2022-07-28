A, B = input().split()

adding = str(int(A[::-1]) + int(B[::-1])) #문자열로 슬라이싱 해서 뒤집고 int형으로 해서 더해기

print(int(adding[::-1]))