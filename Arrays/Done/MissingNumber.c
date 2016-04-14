//http://www.geeksforgeeks.org/find-the-missing-number/
//Given a set of numbers betweeen integers A and B, exactly one of these integers is missing. (A<B)
//There are no duplicates in the list. Find the missing number
//
//Time Complexity  = 2*O(n)
//Space Complexity = O(1)
//Streaming Algorithm

#include<stdio.h>

int main()
{
    int arr[100];
    int A; int B;
    scanf("%d %d", &A, &B);

    int N=B-A;
    int i, j, k;
    int xor=0;
    for(i=A;i<=B;i++)
        xor=xor^i;

    int xorans=0;
    for(i=A;i<B;i++){
        scanf("%d", &N);
        xorans^=N;
    }
    printf("%d is the missing number.. .", xorans^xor);


    return 0;
}
