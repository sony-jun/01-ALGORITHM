# 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다.
# 스택

T = int(input())
for i in range(T):
    vpsCase = input()
    for i in range(len(vpsCase)//2):
        vpsCase = vpsCase.replace("()","")
    if vpsCase=="":
        print("YES")
    else:
        print("NO")