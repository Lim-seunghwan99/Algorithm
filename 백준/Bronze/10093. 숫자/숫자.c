#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100001

void BOJ10093() {
	int num1, num2;
	scanf("%d %d", &num1, &num2);
	
	if (num1 > num2) {
		int temp = num1;
		num1 = num2;
		num2 = temp;
	}

	if (num1 == num2) {
		printf("%d", 0);
		return;
	}
	else {
		printf("%d\n", abs(num1 - num2) - 1);
	}
	
	int cnt = (num2 - num1) - 1;
	if (cnt > 0) {
		int numbers[MAX_SIZE];

		for (int i=0; i < cnt; ++i) {
			numbers[i] = num1 + i + 1;
		}

		for (int i = 0; i < cnt; ++i) {
			printf("%d ", numbers[i]);
		}
	}

}
 
int main() {
	BOJ10093();
	return 0;
}