def snail():
    A, B, V = list(map(int, input().split()))
    end = V - A
    cnt = end // (A-B)
    if end % (A-B) > 0:
        cnt += 1
    cnt += 1
    print(cnt)

snail()