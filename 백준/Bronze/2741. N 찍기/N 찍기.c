#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h> 

void BOJ2741() {
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        printf("%d\n", i + 1);
    }
    
}

int main() {
    BOJ2741();
    return 0;
}