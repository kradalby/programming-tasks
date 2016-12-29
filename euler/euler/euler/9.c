//
//  main.c
//  9
//
//  Created by Kristoffer Dalby on 29/12/13.
//  Copyright (c) 2013 Kristoffer Dalby. All rights reserved.
//

#include <stdio.h>
#include "math.h"

int create_pyth(int m, int n)
{
    int a = pow(n, 2) - pow(m, 2);
    int b = 2 * n * m;
    int c = pow(n, 2) + pow(m, 2);
    if (pow(a, 2) + pow(b, 2) == pow(c, 2)) {
        printf("a: %d b: %d c: %d\n", a, b, c);
        return a+b+c;
    }
    return 0;
}


int main(int argc, const char * argv[])
{

    int r = 0;

    
    for (int m = 0; m < 50; m++) {
        for (int n = 0; n < 50; n++) {
            if (m < n) {
                r = create_pyth(m, n);
                if (r != 0) {
                    printf("m: %d n: %d r: %d\n", m,n,r);
                    if (r == 1000) {
                        break;
                    }
                }
            }
        }
    }
//    r = create_pyth(1, 2);
//    printf("m: %d n: %d r: %d\n", m,n,r);

    
    return 0;
}

