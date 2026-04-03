N, X = map(int, input().split())
L = list(map(int, input().split()))
L = [i for i in L if i<X]
print(*L)