import sys
input = sys.stdin.readline

n = int(input())
inputs = list(map(int, input().split()))
tails = [inputs[0]]

for i in range(1, n):
    cur_val = inputs[i]

    if tails[-1] < cur_val:
        tails.append(cur_val)
    else:
        start = 0
        end = len(tails) - 1
        tar_idx = 0
        while start <= end:
            middle = (start + end) // 2
            if tails[middle] >= cur_val:
                tar_idx = middle
                end = middle - 1
            else:
                start = middle + 1
        tails[tar_idx] = cur_val
        
print(len(tails))