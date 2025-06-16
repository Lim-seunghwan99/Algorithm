#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

void BOJ10804() {
    int a, b;
    int num_lst[20];
    for (int i = 0; i < 21; i++) {
        num_lst[i] = i + 1;
    }
    for (int i = 0; i < 10; i++) {
        scanf("%d %d", &a, &b);
        int left = a - 1;
        int right = b - 1;
        while (left < right) {
            int temp = num_lst[left];
            num_lst[left] = num_lst[right];
            num_lst[right] = temp;
            left++;
            right--;
        }
    }
    for (int i = 0; i < 20; i++) {
        printf("%d ", num_lst[i]);
    }
    printf("\n");
}

int main() {
    BOJ10804();
    return 0;
}