def location(x1, y1, r1, x2, y2, r2):
    XY = ((x1-x2)**2)+((y1-y2)**2)
    R_sum = (r1+r2)**2
    R_diff = (r1-r2)**2
    if XY==0: # 원의 중심이 같다면 V
        if r1==r2: return -1 # 반지름이 같다면 = 무한
        else: return 0 # 반지름이 같지 않다면 = 0
    elif XY>R_sum: return 0 # 원의 중심 거리가 반지름 거리보다 길다면 = 0
    elif XY==R_sum: return 1 # 원의 중심 거리가 반지름 거리와 같다면 = 1
    elif XY > R_diff: return 2 # 원의 중심 거리가 반지름 차이보다 길다면 = 2
    elif XY == R_diff: return 1 # 원의 중심 거리가 반지름 차이와 같다면 = 1
    else: return 0


T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    a = location(x1, y1, r1, x2, y2, r2)
    print(a)