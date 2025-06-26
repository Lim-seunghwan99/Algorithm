#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h>


void BOJ34027() {
    int T;
    scanf("%d", &T);
    int N;
    for (int i = 0; i < T; i++) {
        scanf("%d", &N);
        double temp = sqrt(N);
        int root_int = (int)temp;
        if (root_int * temp == N) {
            printf("1\n");
        }
        else {
            printf("0\n");
        }
    }
    
}

int main() {
    BOJ34027();
    return 0;
}