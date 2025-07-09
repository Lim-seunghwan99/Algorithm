#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

void BOJ31403() {
    int A, B, C;
    scanf("%d %d %d", &A, &B, &C);
    printf("%d\n", A + B - C);

    int count = (B == 0) ? 1 : floor(log10((double)B)) + 1;
    long long ans2 = (long long)A * pow(10, count) + B;
    printf("%lld\n", ans2 - C);
}

int main() {
    BOJ31403();
    return 0;
}