#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>


void BOJ2443() {
    int N;
    scanf("%d", &N);
    
    for (int i = 0; i < 2 * N - 1; i++) {
        if (i < N) {
            for (int j = 0; j < i; j++) {
                printf(" ");
            }
            for (int j = 0; j < 2 * (N - i) - 1; j++) {
                printf("*");
            }
            printf("\n");
        }
        //else if (i == N) {
        //    printf("*\n");
        //}
        
        else {
            // 6일때 빈칸 3개, 7일때 2개, 8일때 1개 
            for (int j = 0; j < 2 * N - i - 2; j++) {
                printf(" ");
            }
            // 6-> 3, 7 -> 5, 8-> 7, 9-> 9
            for (int j = 0; j < 2 * (i - N) + 3; j++) {
                printf("*");
            }
            printf("\n");
        }
    }
}

int main() {
    BOJ2443();
    return 0;
}