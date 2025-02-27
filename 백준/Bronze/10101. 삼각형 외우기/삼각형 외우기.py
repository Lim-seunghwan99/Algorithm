# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error
# 를 출력하는 프로그램을 작성하시오.
a, b, c = [int(input()) for i in range(3)]
if a == b == c == 60:
    print("Equilateral")
elif a + b + c == 180:
    if a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")