#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>


void BOJ2443() {
    int N;
    scanf("%d", &N);

    for (int i = 0; i < N * 2 - 1; i++) {
        for (int j = 0; j < i; j++) {
            printf(" ");
        }
        for (int j = 0; j < 2 * (N - i) - 1; j++) {
            printf("*");
        }
        printf("\n");
    }
}

int main() {
    BOJ2443();
    return 0;
}