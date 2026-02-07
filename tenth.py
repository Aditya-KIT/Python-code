include <stdio.h>
include <stdlib.h>

int main() {
    int a;              // size of array
    int b = 0;          // sum
    int *c;             // pointer to array

    scanf("%d", &a);

    c = (int *)malloc(a * sizeof(int));

    for (int d = 0; d < a; d++) {
        scanf("%d", &c[d]);
        b = b + c[d];
    }

    printf("%d", b);

    free(c);

    return 0;
}
