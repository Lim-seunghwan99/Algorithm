#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h> 

void BOJ10867() {
    int n, tmp;
    int arr[2001] = { 0, };

    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%d", &tmp);
        arr[tmp + 1000]++; 
    }

    for (int i = 0; i < 2001; i++) { 
        if (arr[i] != 0) { 
            printf("%d ", i - 1000);
        }
    }
    printf("\n");
}

int main() {
    BOJ10867();
    return 0;
}