#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

void reverse_string(const char* src, char* dest) {
    int len = strlen(src);
    for (int i = 0; i < len; i++) {
        dest[i] = src[len - 1 - i];
    }
    dest[len] = '\0';
}


int compare(const void* a, const void* b) {
    long long val_a = *(long long*)a;
    long long val_b = *(long long*)b;

    if (val_a < val_b) {
        return -1;
    } else if (val_a > val_b) {
        return 1;
    } else {
        return 0;
    }
}


void BOJ5648() {
    int N;
    scanf("%d", &N);
    long long* num_lst;
    char nums[15];
    char reverse_nums[15];

    num_lst = (long long*)malloc(N * sizeof(long long));

    for (int i = 0; i < N; i++) {
        scanf("%s", &nums);
        reverse_string(nums, reverse_nums);
        num_lst[i] = atoll(reverse_nums);
    }
    qsort(num_lst, N, sizeof(long long), compare);

    for (int i = 0; i < N; i++) {
        printf("%lld\n", num_lst[i]);
    }
}

int main() {
    BOJ5648();
    return 0;
}