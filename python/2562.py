L = []
for _ in range(9):
    L.append(int(input()))

M = max(L)

print(M)
print(L.index(M)+1)