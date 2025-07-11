#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


void BOJ15829() {
    int L;
    scanf("%d", &L);

    char* str = (char*)malloc(sizeof(char) * (L + 1));
    scanf("%s", str);
    
    long long hash_value = 0;
    long long R = 1;

    const long long r = 31;
    const long long M = 1234567891;

    for (int i = 0; i < L; i++) {
        long long num = str[i] - 'a' + 1;
        hash_value = (hash_value + num * R) % M;
        R = (R * r) % M;
    }

    printf("%lld\n", hash_value);
}

int main() {
    BOJ15829();
    return 0;
}