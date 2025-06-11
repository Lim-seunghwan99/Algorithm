#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void BOJ2576() {
	// 홀수인 자연수를 골라 합을 고르고, 홀수들 중 최솟값을 찾는 프로그램
	// 홀수가 없으면 -1
	int num;
	int sv = 0;
	int mn = 1000000000;
	for (int i = 0; i < 7; i++) {
		scanf("%d", &num);
		if (num % 2 == 1) {
			sv += num;
			if (mn > num) {
				mn = num;
			}
		}
	}
	if (sv > 0) {
		printf("%d\n", sv);
		printf("%d\n", mn);
	}
	else {
		printf("%d", -1);
	}
}

int main() {
	//BOJ2490();
	BOJ2576();
}