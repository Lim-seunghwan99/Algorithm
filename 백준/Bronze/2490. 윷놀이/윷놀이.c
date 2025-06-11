#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void BOJ2490()
{
	int num, sv_cnt;

	for (int i = 0; i < 3; i++) {
		sv_cnt = 0;
		for (int j = 0; j < 4; j++) {
			scanf("%d", &num);
			if (num == 0)
				sv_cnt++;
		}
		switch (sv_cnt) {
		case 0:
			printf("E\n");
			break;
		case 1:
			printf("A\n");
			break;
		case 2:
			printf("B\n");
			break;
		case 3:
			printf("C\n");
			break;
		case 4:
			printf("D\n");
			break;
		}
	}

	return 0;
}

int main() {
	BOJ2490();
}