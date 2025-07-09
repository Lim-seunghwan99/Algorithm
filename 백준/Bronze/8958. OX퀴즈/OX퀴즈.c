#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <math.h>

void BOJ8958() {
    int n;
    char ox[81];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int ans = 0;
        int tmp = 0;
        scanf("%s", ox);
        for (int i = 0; i < strlen(ox); i++) {
            if (ox[i] == 'O') {
                tmp += 1;
                ans += tmp;
            }
            else {
                tmp = 0;
            }
        }
        printf("%d\n", ans);
    }
}

int main() {
    BOJ8958();
    return 0;
}