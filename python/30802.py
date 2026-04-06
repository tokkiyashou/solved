# 티셔츠 한 장과 펜 한 자루가 포함된 웰컴키트
# 티셔츠 같은 사이즈 T장과 펜 P묶음을 나눠줌
# 티셔츠는 남아도 되지만 부족하면 안됨
# 펜은 부족하면 안되고 정확히 수대로 준비되어야 함

N = int(input()) # 참가자 수
sizes = list(map(int, input().split())) # S, M, L, XL, XXL, XXXL 각 사이즈별 신청자 수
T, P = map(int, input().split()) # 티셔츠와 펜의 묶음 수

# 티셔츠의 수
total_t = 0
for i in sizes:
    if i==0: continue # 신청자가 없다면
    elif i<T: total_t+=1 # T보다 값이 작다면 한 묶음만 필요
    elif (i//T)*T==i: total_t+=i//T # 주어진 값이 T보다 크며 (i//T)*T과 같은 경우
    else: total_t+=(i//T)+1 # 주어진 값이 T보다 크며 (i//T)*T보다 큰 경우

print(total_t)

# 펜의 수
total_pack = N//P
total_each = N%P

print(total_pack, total_each)