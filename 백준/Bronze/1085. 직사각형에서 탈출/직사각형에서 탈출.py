def escapeRectangle():
    x, y, w, h = list(map(int, input().split()))
    # x, y에서 대각선이 0,0 w,h 인 직사각형 경계선 까지의 거리 최솟값
    # 0 - 5
    a = []
    a.append(abs(x - w)) # x = 6  // 6,5,4,3
    a.append(x - 0)
    a.append(abs(y - h)) # y = 2
    a.append(y - 0)
    print(min(a))
escapeRectangle()