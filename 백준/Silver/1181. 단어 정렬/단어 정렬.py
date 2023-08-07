def wordsort():
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(input())
    set_lst = set(arr)
    arr = list(set_lst)
    arr.sort()
    arr.sort(key=len)
    for i in range(len(arr)):
        print(arr[i])


wordsort()