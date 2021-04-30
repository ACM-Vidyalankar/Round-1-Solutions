n = int(input())
for i in range(n):
    w, p = input().split(' ')
    w = int(w)
    p = int(p)
    bed = 0
    for j in range(1, w+1):
        bed = bed + j*3
    if(bed >= p):
        print(p)
    else:
        print(bed)