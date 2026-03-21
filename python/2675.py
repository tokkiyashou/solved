# T = int(input())
# for i in range(0, T):
#     repeat, word = map(str, input().split())
#     repeat = int(repeat)
#     L = []
#     for ii in word:
#         L.append(ii*repeat)
#         print(*L, sep='')

T = int(input())
for _ in range(T):
    repeat, word = input().split()
    print(''.join(c*int(repeat) for c in word))