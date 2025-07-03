#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MAX_LENGTH 100

void BOJ2999() {
    // R <= C이고, R * C인 R과 C를 고른다, 여러개라면, R이 큰 값을 선택한다.
    // 루트 N이 R의 최대값
    // R만큼 출력, 나머지 +1 출력 이런식
    char* password;
    password = (char*)malloc(sizeof(char) * (MAX_LENGTH + 1));

    scanf("%100s", password);
    size_t len_password = strlen(password);
    int R = 0;
    int C = 0;

    for (int i = (int)floor(sqrt(len_password)); i >= 1; i--){
        if (len_password % i == 0) {
            R = i;
            C = len_password / i;
            break;
        }
    }

    char* decrypted_message = (char*)malloc(sizeof(char) * (len_password + 1));
    if (decrypted_message == NULL) {
        return;
    }
    int decrypted_idx = 0;

    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            decrypted_message[decrypted_idx++] = password[i + j * R];
        }
    }
    decrypted_message[decrypted_idx] = '\0';

    printf("%s\n", decrypted_message);
}

int main() {
    BOJ2999();
    return 0;
}