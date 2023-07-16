def hand():
    a, b = map(int, input().split())
    if(a==1 and b==2) or (a==2 and b==3) or (a==3 and b==1):
        print('B')
    if (a == 2 and b == 1) or (a == 3 and b == 2) or (a == 1 and b == 3):
        print('A')
hand()