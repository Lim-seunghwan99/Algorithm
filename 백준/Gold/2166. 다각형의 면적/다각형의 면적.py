import sys
input = sys.stdin.readline


def boj2166():
    N = int(input())
    # n각형 넓이 구하기 2차원 배열에서
    # 신발끈 공식(Shoelace Formula)
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    sv1 = 0
    sv2 = 0
    arr.append(arr[0])
    for i in range(N):
        sv1 += arr[i][0] * arr[i+1][1]
        sv2 += arr[i][1] * arr[i + 1][0]
    area = abs(sv1 - sv2) / 2
    print(f"{area:.1f}")


if __name__ == "__main__":
    boj2166()