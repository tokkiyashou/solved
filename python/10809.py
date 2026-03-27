S = str(input())
result = []
for i in range(97, 123):
    found = -1
    for ii in range(len(S)):
        if S[ii] == chr(i):
            found = ii
            break
    result.append(found)
print(*result)