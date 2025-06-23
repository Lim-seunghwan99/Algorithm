#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

void BOJ11931() {
    int N;
    int temp;
    int *num_lst;
    scanf("%d", &N);

    num_lst = (int*)malloc(N * sizeof(int));
    if (num_lst == NULL) {
        return;
    }

    for (int i = 0; i < N; i++) {
        scanf("%d", &temp);
        num_lst[i] = temp;
    }

    qsort(num_lst, N, sizeof(int), compare);  
    // 시작 주소, 원소 개수, 배열의 각 원소 하나의 크기, 두 요소를 비교하는 사용자 정의 함수

    for (int i = 0; i < N; i++) {
        printf("%d\n", num_lst[i]);
    }
}

int main() {
    BOJ11931();
    return 0;
}