def boj3151():
    import sys
    N = int(sys.stdin.readline())
    arr = sorted(list(map(int, sys.stdin.readline().split())))
    
    count = 0
    for i in range(N - 2):
        left = i + 1      
        right = N - 1     
        target = -arr[i]  

        while left < right: # left와 right가 교차하면 종료
            current_sum = arr[left] + arr[right]

            if current_sum == target:
                if arr[left] == arr[right]:
                    num_elements = right - left + 1
                    count += num_elements * (num_elements - 1) // 2
                    break 
                else:
                    l_start = left
                    while left < right and arr[left] == arr[l_start]:
                        left += 1
                    count_left = left - l_start 

                    r_start = right
                    while right >= left and arr[right] == arr[r_start]:
                        right -= 1
                    count_right = r_start - right #

                    count += count_left * count_right

            elif current_sum < target:
                left += 1
            else: 
                right -= 1

    print(count)

if __name__ == "__main__":
    boj3151()