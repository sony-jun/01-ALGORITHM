# 2609
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
# input 24 18  

x ,y = map(int,input().split())
def GCD(x,y):
    while(y):  # y 가 자연수일 때
        x,y = y, x%y
    return x
print(GCD(x,y))

def LCM(x,y):
    result = (x*y)//GCD(x,y)
    return result

print(LCM(x,y))
        





