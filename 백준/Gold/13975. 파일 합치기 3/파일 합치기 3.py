import sys
input = sys.stdin.readline
import heapq


def boj13975():
    T = int(input())
    for _ in range(T):
        K = int(input())
        arr = list(map(int, input().split()))
        # 파일을 합칠 때 필요한 비용 : 두 파일 크기의 합
        # 왜 순서 바꾸면 달라지지..? <- 비용이 큰 걸 적게 중복해야함
        hp = []
        for i in range(K):
            heapq.heappush(hp, arr[i])
        ans = 0
        while len(hp) > 1:
            temp1 = heapq.heappop(hp)
            temp2 = heapq.heappop(hp)
            ans += temp1 + temp2
            heapq.heappush(hp, temp1+temp2)
        print(ans)


if __name__ == "__main__":
    boj13975()