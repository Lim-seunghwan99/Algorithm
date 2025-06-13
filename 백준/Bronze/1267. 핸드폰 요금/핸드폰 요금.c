#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

void BOJ1267() {
    int N;
    scanf("%d", &N); // 싼 요금제 이름
    // 1. 30초마다 10원씩 청구
    // 2. 60초마다 15원
    int num1;
    int sv1 = 0;
    int sv2 = 0;
    for (int i = 0; i < N; ++i) {
        scanf("%d", &num1);
        sv1 += ((num1 / 30) + 1) * 10;
        sv2 += ((num1 / 60) + 1) * 15;
    }
    if (sv1 == sv2) {
        printf("Y M %d", sv1);
    }
    else if (sv1 > sv2) {
        printf("M %d", sv2);
    }
    else {
        printf("Y %d", sv1);
    }

}

int main() {
    BOJ1267();
    return 0;
}