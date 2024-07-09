N, K = map(int, input().split())
arr = list(map(int, input().split()))

def f1(N, K, arr):
    res = sorted(arr)
    return res[K-1]

print(f1(N, K, arr))