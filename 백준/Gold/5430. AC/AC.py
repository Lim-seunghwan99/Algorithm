def boj5430():
    import sys
    from collections import deque
    input = sys.stdin.readline
    # R은 뒤집기, D는 버리기
    # 배열이 비었을 때, D는 error
    T = int(input())
    for case in range(T):
        p = input().strip()
        n = int(input())
        arr = deque(input().strip()[1:-1].split(","))

        if n == 0:
            arr = deque()

        rev = False
        chk = True
        for i in p:
            if i == "R":
                rev = not rev
            elif i == "D":
                if not arr:
                    print("error")
                    chk = False
                    break
                if rev:
                    arr.pop()
                else:
                    arr.popleft()

        if chk:
            if rev:
                arr.reverse()
            print("[" + ",".join(arr) + "]")


if __name__ == "__main__":
    boj5430()