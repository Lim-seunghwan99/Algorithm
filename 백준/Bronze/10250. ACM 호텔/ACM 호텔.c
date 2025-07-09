#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

void BOJ10250() {
    int T, H, W, N;
    int ans;
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        scanf("%d %d %d", &H, &W, &N);
        int chk = (N - 1) % H + 1;
        int room = (N - 1) / H + 1;
        ans = chk * 100 + room;
        printf("%d\n", ans);
    }
}

int main() {
    BOJ10250();
    return 0;
}