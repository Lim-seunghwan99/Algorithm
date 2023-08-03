def baekmath():
    x = int(input())
    a = 0
    cnt = 0
    while a < x:
        cnt += 1
        a += cnt
    cur = x - (a - cnt)
    x_b = cnt-cur+1

    if cnt % 2 == 0:
         print(f'{cur}/{x_b}')
    else:
         print(f'{x_b}/{cur}')
baekmath()