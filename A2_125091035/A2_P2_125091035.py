n,q=map(int, input().split())
jobs=[]
time=[0]*n
queue=[]
head=0
front=1

for i in range(n):
    a, t = map(int, input().split())
    jobs.append([a, t, i])

T=jobs[0][0]
queue.append(jobs[0])

while head < len(queue):  
    a, t, i = queue[head]
    head+=1 
    
    work=min(t, q)
    T+=work
    t-=work
    
    while front<len(jobs) and jobs[front][0] <= T:
        queue.append(jobs[front])
        front+=1
    
    if t:
        queue.append([a, t, i])
    else:
        time[i]=T
    
    if head >= len(queue) and front<len(jobs):
        T = jobs[front][0]
        while front<len(jobs) and jobs[front][0] <= T:
            queue.append(jobs[front])
            front+=1

print(' '.join(map(str, time)))