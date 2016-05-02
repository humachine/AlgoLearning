//http://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
import java.util.Scanner;
import java.lang.*;
class MaxSumWithNoAdjacentElements{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);

        int N = in.nextInt();

        int i, j, k;
        int[] arr = new int[100];
        for(i=0;i<N;i++)
            arr[i] = in.nextInt();
        for(i=0;i<N;i++)
            System.out.println(arr[i]);
        int ans = maxSum(arr, 0, N);
        System.out.println("Ans is " + ans);
    }
    static int[] memo = new int[1000];
    static int maxSum(int[] arr, int left, int right){
        if(memo[left]>0)
            return memo[left];
        if(left<right){
            memo[left] = Math.max(arr[left]+maxSum(arr, left+2, right), maxSum(arr, left+1, right));
            return memo[left];
        }
        return 0;
    }
}
