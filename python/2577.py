A = int(input())
B = int(input())
C = int(input())
cal = A*B*C
cal = str(cal)

for i in range(10):
    print(cal.count(str(i)))