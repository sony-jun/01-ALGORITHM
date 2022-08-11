import sys
input=sys.stdin.readline
def switch(array,index0,index1):
    if(index0<index1<len(array)):
        temp=array[index0]
        array[index0]=array[index1]
        array[index1]=temp
        return 1
    else:
        return 0
def quick_sort(array,start,end):
    idx0=start+1
    idx1=end
    idx=start
    if(start<end):
        while idx0<=idx1:
            if(array[idx]<=array[idx0]):
                idx0+=1
            else:
                switch(array,idx0,idx1)
                idx1-=1
        switch(array,idx,idx0-1)
        quick_sort(array,start,idx0-2)
        quick_sort(array,idx0,end)
        return 1
    else:
        return 0
array0=[]
array1=[]
N=int(input())
for i in range(N):
    array=list(map(int,input().split()))
    array=array[1:]
    array.sort()
    array=array[::-1]
    num0=array[0]
    num1=0
    max=0
    for k in array:
        num1=num0
        num0=k
        if(abs(num0-num1)>max):
            max=abs(num0-num1)
    array0.append(array)
    array1.append(max)
m=0
for i in array0:
    print("Class",m+1)
    print("Max",array0[m][0],end=', ')
    print("Min",array0[m][len(array0[m])-1],end=', ')
    print("Largest gap",array1[m])
    m+=1