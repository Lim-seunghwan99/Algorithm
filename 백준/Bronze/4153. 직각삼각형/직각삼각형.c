#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

void BOJ4153() {
    // 참가자 수
    int arr[3];
    while (1) {
        scanf("%d %d %d", &arr[0], &arr[1], &arr[2]);
        if (arr[0] == 0 && arr[1] == 0 && arr[2] == 0) {
            break;
        }
        qsort(arr, 3, sizeof(int), compare);
        if (arr[0] * arr[0] + arr[1] * arr[1] == arr[2] * arr[2]) {
            printf("right\n");
        }
        else {
            printf("wrong\n");
        }
    }
    

    
}

int main() {
    BOJ4153();
    return 0;
}