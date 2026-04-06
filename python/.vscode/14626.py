# ISBN = list(input())
# total = 0
# emp = -1

# for i in range(12):
#     if ISBN[i].isdigit() == False:
#         emp = i
#         continue
#     elif i%2==0 or i==0:
#         total += int(ISBN[i])
#     else: total += int(ISBN[i])*3

# if emp%2==0 or emp==0:
#     print((10-(total+int(ISBN[12]))%10)%10)
# else:
#     print(((10-(total+int(ISBN[12]))%10)%10)//3)

ISBN = list(input())
total = 0
emp = -1

for i in range(12):
    if ISBN[i].isdigit() == False:
        emp = i
        continue
    elif i%2==0:
        total+=int(ISBN[i])
    else:
        total+=int(ISBN[i])*3

weight=1 if emp%2==0 else 3

for x in range(10):
    if (total+x*weight+int(ISBN[12]))%10==0:
        print(x)
        break