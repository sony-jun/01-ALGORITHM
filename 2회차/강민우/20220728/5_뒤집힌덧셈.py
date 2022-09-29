X , Y =map(int, input().split())

def rev(num) :
    num_list = list(str(num))
    num_list.reverse() 
    num_list = ''.join(num_list)
    return int(num_list)

print(rev(rev(X) + rev(Y)))