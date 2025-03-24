import sys
input = sys.stdin.readline
def boj15665():
    N, M = list(map(int, input().split()))
    arr = list((map(int, input().split())))
    arr = sorted(set(arr))
    # N개의 자연수 중에 M개를 고른 수열
    # 같은 수를 여러 번 골라도 된다.
    answer = set()
    def back(answer_list):
        if len(answer_list) == M:
            answer.add(tuple(answer_list))
            return

        for i in range(len(arr)):
            answer_list.append(arr[i])
            back(answer_list)
            answer_list.pop()


    back([])
    [print(*ans) for ans in sorted(answer)]


if __name__ == "__main__":
    boj15665()