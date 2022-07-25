# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())
for test_case in range(1 , T+1):
    test = input()
    test_list = []
    test_list.extend(test)

    for a in range(len(test_list)):
        if test_list[a] == 'O' :
            test_list[a] = 1
        else :
            test_list[a] = 0 
        if a >0 :
            if   0 < test_list[a] <=test_list[a -1]  :
             test_list[a] = test_list[a -1] + 1          
    print(sum(test_list))

                
