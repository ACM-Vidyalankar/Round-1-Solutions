def main():
    fi=[]
    for _ in range(int(input())):
        d={num:chr(num+96) for num in range(1,27)}
        
        n=int(input())
        a=list(map(int,input().split()))
        su=0
        s2=0
        for i in range(len(a)):
            if i%2==0:
                su+=ord(d[a[i]])
            else:
                s2+=ord(d[a[i]])
        fi.append((su,s2))
    for (a,b) in fi:
        print(a,b)
        
main()
