#include <stdio.h>

int main(void) {
    int height;   /* Variable declaration */
    printf("Enter height => ");
    scanf("%d", &height); /* Get height */
    if ( height > 120 ) {
        printf("Buy a full ticket!\n");
    }
    else {
        printf("Buy a half ticket!\n");
    }

    return 0;
}
