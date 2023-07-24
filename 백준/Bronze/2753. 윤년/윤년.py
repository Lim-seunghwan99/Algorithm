def yer():
    n = int(input())
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        return 1
    else:
        return 0


print(yer())