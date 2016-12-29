//
//  160.c
//  euler
//
//  Created by Kristoffer Dalby on 31/12/13.
//  Copyright (c) 2013 Kristoffer Dalby. All rights reserved.
//

#include <stdio.h>

long fact(long n, long facts[])
{
    if (n == 0) {
        return 1;
    } else {
        facts[n] = fact(n-1, facts) * n;
        return facts[n];
    }
}


int main()
{
    long facts[1000];
    long result;
    result = fact(1000, facts);
    printf("%lu\n", result);
    return 0;
}