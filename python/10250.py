T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    a = 1
    b = 1
    for ii in range(1, N):
        if a<H: a+=1
        elif a==H:
            a=1
            b+=1
    if b<10: print(str(a)+'0'+str(b))
    else: print(str(a)+str(b))