# https://www.acmicpc.net/problem/2941

input_ = input() # ljes=njak
list_ = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

cnt = 0


for i in range(len(input_)):
    if input_[i] == 'c' and input_[i+1] == '=':
        #i+1말고 2칸 뛰어 넘어서 for문돌림
        cnt += 2
    elif input_[i] == 'c' and input_[i+1] == '=':

        cnt += 2
    elif input_[i] == 'd' and input_[i+1] == 'z' and input_[i+2] == '=':
         cnt += 3
    elif input_[i] == 'd' and input_[i+1] == '-':
        cnt += 2
    elif input_[i] == 'l' and input_[i+1] == 'j':
        cnt += 2
    elif input_[i] == 'n' and input_[i+1] == 'j':
        cnt += 2
    elif input_[i] == 's' and input_[i+1] == '=':
        cnt += 2
    elif input_[i] == 'z' and input_[i+1] == '=':
        cnt += 2
    print(len(input_) - cnt)
    
        
        
        













# for i in range(len(input_)):
#     #슬라이싱2개씩...?> 안됨 3개짜리도 있음...
#     if input_[i:i+2] in list_:
#         cnt+=1
# print(len(input_) - cnt*2  + cnt)


