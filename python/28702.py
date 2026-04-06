# 연속된 세 개의 문자열 중 맨 끝부터 차례대로 숫자인지 검증함
# 숫자라면? -> i만큼 더해서 수를 구함, break
# 문자라면? -> 정체를 알 수 없으니 다음숫자로 패스
# 
# 숫자가 나왔다면 정해진 조건문을 검증함

L = [input() for i in range(3)]
L = list(reversed(L))

for i in L:
    if i.isdigit():
        next = int(i)+(L.index(i)+1)
        break

if next%3==0 and next%5==0:
    print("FizzBuzz")
elif next%3==0 and next%5!=0:
    print("Fizz")
elif next%3!=0 and next%5==0:
    print("Buzz")
else:
    print(next)