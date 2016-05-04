//http://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
//
//Find the maximum sum of elements such that no two elements in the sum are adjacent to each other in the array
//Time complexity = O(n)
//Space complexity = O(1)

import java.util.Scanner;
import java.lang.*;
import java.lang.Math.*;
class MaxSumWithNoAdjacentElements{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);

        int N = in.nextInt();

        int i, j, k;
        int[] arr = new int[100];
        for(i=0;i<N;i++)
            arr[i] = in.nextInt();
        int ans = maxSum(arr, 0, N);
        System.out.println("Ans is " + ans);
    }
    static int[] memo = new int[1000];
    static int maxSum(int[] arr, int left, int right){
           int sumRight=0;
           int sumLeft=0;

           int i, j, k, curr;
           for(i=right-1;i>=0;i--){
                curr=Math.max(sumLeft, sumRight+arr[i]); 
                sumRight=sumLeft;
                sumLeft=curr;
           }
           return Math.max(sumLeft, sumRight);

    }
}
