from collections import deque

n = int(input())

queue_ = deque(list(range(1,n+1))) 
list_ = []

while len(queue_) > 1:
        
    list_.append(queue_.popleft())
    a = queue_.popleft()
    queue_.append(a)
        
    
list_.append(queue_[0])
print(*list_)