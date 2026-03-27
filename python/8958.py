T = int(input())
for i in range(0, T):
    input_score = str(input())
    output_score=0
    count=0
    for ii in input_score:
        if ii=="O":
            count+=1
            output_score+=count
        elif ii=="X":
            count=0
    print(output_score)