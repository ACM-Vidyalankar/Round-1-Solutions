T = int(input())
for i in range(T):
    n = int(input())
    n1 = str(n)
    n1 = int(n1[::-1])
    sum = n1 + n
    if(sum%2==0):
        print("1")
    else:
        print("0")
