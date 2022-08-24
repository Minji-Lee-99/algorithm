# 직사각형
for _ in range(4):
    x1, y1, x2, y2, xx1, yy1, xx2, yy2 = map(int, input().split())
    # 점으로 만나는 경우
    if (x2 == xx1 and y2 == yy1) or (x2 == xx1 and y1 == yy2) or\
            (x1 == xx2 and y2 == yy1) or (x1 == xx2 and y1 == yy2):
        result = 'c'
    # 선으로 만나는 경우
    elif (x2 == xx1 and y2 > yy1 > y1) or (xx2 == x1 and yy2 > y1 > yy1) or\
            (y2 == yy1 and x2 > xx1 > x1) or (yy2 == y1 and xx2 > x1 > xx1):
        result = 'b'
    # 안겹치는 경우1
    elif y2 < yy1 or yy2 < y1 or x2 < xx1 or xx2 < x1:
        result = 'd'
    # 사각형으로 만나는 경우
    else:
        result = 'a'
    # 결과 출력
    print(result)
