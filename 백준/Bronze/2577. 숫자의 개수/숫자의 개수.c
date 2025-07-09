#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <math.h>

void BOJ2577() {
    int A, B, C;
    scanf("%d", &A);
    scanf("%d", &B);
    scanf("%d", &C);
    int nums = A * B * C;
    char str_nums[13];
    // 정수를 문자열로 바꾸는 방법 sprintf
    sprintf(str_nums, "%d", nums);
    int len = strlen(str_nums);
    int ans[11] = {0};
    for (int i = 0; i < len; i++) {
        ans[str_nums[i] - '0']++;
    }
    for (int i = 0; i <= 9; i++) {
        printf("%d\n", ans[i]);
    }
    
    
    
}

int main() {
    BOJ2577();
    return 0;
}