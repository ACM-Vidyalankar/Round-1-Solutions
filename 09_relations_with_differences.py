fi=[]
for _ in range(int(input())):
    
    n=int(input())
    x=list(map(int,input().split()))
    k=int(input())
    z=[]
    for i in range(n-1):
        z.append(abs(x[i+1]-x[i]))
    q=set(z)
    v=list(q)
    
    if len(v)>1:
        fi.append((sum(v)))
    else:
        fi.append((v[0]+k))
for k in fi:
    print(k)
