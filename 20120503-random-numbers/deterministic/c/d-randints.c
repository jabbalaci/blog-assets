#include <stdio.h>
#include <stdlib.h>

/**
 * generate random numbers from the interval [1, 10]
 */

int main()
{
    int UPPER = 10;
    int i;

    for (i = 0; i < 10; ++i)
    {
        printf("%d ", (int)(random() % UPPER + 1));
    }
    printf("\n");

    return 0;
}
