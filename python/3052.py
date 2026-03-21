L = []
for i in range(0, 10):
    W = int(input())
    L.append(W%42)

L = list(set(L))
print(len(L))