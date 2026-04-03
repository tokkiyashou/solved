H, M = map(int, input().split())

def clock(dum):
    print(dum//60, dum%60)

dum = (60*H+M)-45
if dum>=0: clock(dum)
else:
    dum = 24*60+dum
    clock(dum)