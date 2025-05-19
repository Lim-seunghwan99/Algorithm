def boj10845():
    from collections import deque

    def push(lst, num):
        lst.append(num)

    def pop(lst):
        if lst:
            print(lst.popleft())
        else:
            print(-1)

    def size(lst):
        print(len(lst))

    def empty(lst):
        if len(lst) > 0:
            print(0)
        else:
            print(1)

    def front(lst):
        if lst:
            print(lst[0])
        else:
            print(-1)

    def back(lst):
        if lst:
            print(lst[-1])
        else:
            print(-1)

    command_map = {
        "push": push,
        "pop": pop,
        "size": size,
        "empty": empty,
        "front": front,
        "back": back,
    }

    N = int(input())
    q = deque()
    for _ in range(N):
        cmd = input().split()
        if cmd[0] == "push":
            command_map["push"](q, int(cmd[1]))
        else:
            command_map[cmd[0]](q)




if __name__ == "__main__":
    boj10845()