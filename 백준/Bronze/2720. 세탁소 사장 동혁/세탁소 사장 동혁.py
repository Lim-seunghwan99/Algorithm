def baek2720():
    T = int(input())
    for i in range(T):
        money = int(input())
        Quarter = 25
        Dime = 10
        Nickel = 5
        cnt_D = cnt_N = cnt_P = cnt_Q = 0
        cnt_Q = money // Quarter
        money = money % Quarter
        cnt_D = money // Dime
        money = money % Dime
        cnt_N = money // Nickel
        cnt_P = money % Nickel
        print(cnt_Q, cnt_D, cnt_N, cnt_P)


baek2720()