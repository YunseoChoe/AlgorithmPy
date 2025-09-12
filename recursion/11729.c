#include <stdio.h>

void Hanoi(int n, int a, int b, int c);
int k = 0; // 옮긴 횟수

int main() {
    int n; // 원판 개수
    scanf("%d", &n);
    Hanoi(n, 1, 2, 3);
    
    return 0;
}

void Hanoi(int n, int a, int b, int c) {
    if (n == 1) {
        k += 1;
        printf("%d %d\n", a, c);
    }
    else {
        Hanoi(n - 1, a, c, b);
        Hanoi(1, a, b, c);
        Hanoi(n - 1, b, a, c);
    }
}