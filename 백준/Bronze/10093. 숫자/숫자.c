#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100001

void BOJ10093() {
    long long num1, num2;
    scanf("%lld %lld", &num1, &num2);

    if (num1 > num2) {
        long long temp = num1;
        num1 = num2;
        num2 = temp;
    }

    if (num1 == num2) {
        printf("0\n");
        return;
    }

    long long cnt = num2 - num1 - 1;
    printf("%lld\n", cnt);

    if (cnt > 0) {
        long long numbers[MAX_SIZE];

        for (int i = 0; i < cnt; ++i) {
            numbers[i] = num1 + i + 1;
        }

        for (int i = 0; i < cnt; ++i) {
            printf("%lld ", numbers[i]);
        }
        printf("\n");
    }
}

int main() {
    BOJ10093();
    return 0;
}