#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <math.h>

void BOJ2920() {
    // 1 ~ 8로 증가하면 axcending, 반대면 내림차순, else : mixed
    int nums[8];
    for (int i = 0; i < 8; i++) {
        scanf("%d", &nums[i]);
    }
    int ascending = 1;
    int descending = 1;
    for (int i = 0; i < 7; i++) {
        if (ascending && nums[i + 1] != nums[i] + 1) {
            ascending = 0;
        }
        if (descending && nums[i + 1] != nums[i] - 1) {
            descending = 0;
        }
    }
    if (ascending > 0) {
        printf("ascending");
    }
    else if (descending > 0) {
        printf("descending");
    }
    else {
        printf("mixed");
    }
}

int main() {
    BOJ2920();
    return 0;
}