//
//  main.c
//  439
//
//  Created by Kristoffer Dalby on 28/12/13.
//  Copyright (c) 2013 Kristoffer Dalby. All rights reserved.
//

#include <stdio.h>

long d(long k)
{
    long r = 0;
    for (long i = 1; i<k+1; i++) {
        if (k % i == 0) {
            r += i;
            //prlongf("%d,%d\n", k, i);
        }
    }
    return r;
}

long s(long k){
    long r = 0;
    for (long i = 1; i<k+1; i++) {
        for (long j = 1; j<k+1; j++) {
            r += d(j*i);
            printf("%lu\n",r);
        
        }
    }
    
    return r;
}

int main(int argc, const char * argv[])
{
    long result;
    result = s(100);
    printf("%lu\n", result);
    return 0;
}

