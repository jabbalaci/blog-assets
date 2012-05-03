#include <stdio.h>
#include <stdlib.h>

/**
 * generate random numbers from the interval [1, 10]
 * in a non-deterministic way
 */

int main()
{
    int UPPER = 10;
    int i;

    srand((unsigned)time(NULL));

    for (i = 0; i < 10; ++i)
    {
        printf("%d ", (int)(random() % UPPER + 1));
    }
    printf("\n");

    return 0;
}
