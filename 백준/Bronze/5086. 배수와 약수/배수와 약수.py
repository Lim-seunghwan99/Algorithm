def baek5086():
    while True:
        x, y = list(map(int, input().split()))
        if x == 0 and y == 0:
            break
        elif y % x == 0:
            print('factor')
        elif x % y == 0:
            print('multiple')
        else:
            print('neither')
baek5086()