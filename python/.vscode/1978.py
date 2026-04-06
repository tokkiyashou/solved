N = int(input())
L = list(map(int, input().split()))
total = 0

for i in L:
    if i<2: result=0
    elif i==2: result=1
    else:
        result=1
        for ii in range(2, int(i**0.5)+1):
            if i%ii==0:
                result=0
                break
    if result == 1:
        total += 1

print(total)