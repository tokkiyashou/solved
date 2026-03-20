# def fibonacci(n):
#     if n==0:
#         return 1, 0
#     elif n==1:
#         return 0, 1
#     else:
#         zero1, one1 = fibonacci(n-1)
#         zero2, one2 = fibonacci(n-2)
#     return zero1+zero2, one1+one2

# T = int(input("Test case time: "))
# for i in range(0, T):
#     N = int(input("Input N: "))
#     print(fibonacci(N))

def fibonacci(n):
    if n==0: return 1, 0
    if n==1: return 0, 1

    DP = [(0, 0)]*(n+1)
    DP[0] = (1, 0)
    DP[1] = (0, 1)

    for i in range(2, n+1):
        DP[i] = (DP[i-1][0]+DP[i-2][0], DP[i-1][1]+DP[i-2][1])

    return DP[n]

T = int(input())
for i in range(T):
    N = int(input())
    a, b = fibonacci(N)
    print(a, b)