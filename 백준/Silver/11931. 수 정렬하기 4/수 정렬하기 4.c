#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
    return (*(int*)b - *(int*)a);
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

    for (int i = 0; i < N; i++) {
        printf("%d\n", num_lst[i]);
    }
}

int main() {
    BOJ11931();
    return 0;
}