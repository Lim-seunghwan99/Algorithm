#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>


void BOJ2441() {
    int N;
    scanf("%d", &N);

    for (int i = 0; i <= N; i++) {
        for (int j = 0; j < i; j++) {
            printf(" ");
        }
        for (int j = 0; j < N - i; j++) {
            printf("*");
        }
        printf("\n");
    }
}

int main() {
    BOJ2441();
    return 0;
}