#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <math.h>

void BOJ30802() {
    // 참가자 수
    int N;
    scanf("%d", &N);

    // 사이즈별 신청자의 수
    int user[6];
    for (int i = 0; i < 6; i++) {
        scanf("%d", &user[i]);
    }
    // 티셔츠와 펜의 묶음 수
    int tshirts, pen;
    scanf("%d %d", &tshirts, &pen);
    
    int ans = 0;
    for (int i = 0; i < 6; i++) {
        if (user[i] % tshirts > 0) {
            ans += 1;
        }
        ans += user[i] / tshirts;
    }
    printf("%d\n", ans);
    printf("%d %d", N / pen, N % pen);
}

int main() {
    BOJ30802();
    return 0;
}