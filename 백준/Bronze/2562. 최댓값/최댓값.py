arr = [int(input()) for i in range(9)]
max_i = 0
temp = 0
for k, v in enumerate(arr):
    if max_i < v:
        max_i = v
    if v == max_i:
        temp = k
print(f'{max_i}\n{temp+1}')