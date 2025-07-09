#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h> 

void BOJ2475() {
    int arr[6];
    int tmp;
    int ans = 0;
    

    for (int i = 0; i < 5; i++) {
        scanf("%d", &tmp);
        arr[i] = tmp;
        ans += tmp * tmp;
    }
    printf("%d", ans % 10);
    
}

int main() {
    BOJ2475();
    return 0;
}