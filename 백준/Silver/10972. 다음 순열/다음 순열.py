import sys

# 내림차순이 끝나는 지점을 찾고, 오름차순이 되는 수를 찾아서 두 수 교환 후
# 순열 정렬하면 시간복잡도를 줄일 수 있다.
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

i = n - 1
while i > 0 and nums[i - 1] > nums[i]:
    i -= 1

if i <= 0:
    print(-1)
    exit()

j = n - 1
while nums[j] < nums[i - 1]:
    j -= 1

nums[i - 1], nums[j] = nums[j], nums[i - 1]

print(*(nums[:i] + nums[i:][::-1]))