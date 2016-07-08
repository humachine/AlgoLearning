//http://www.geeksforgeeks.org/leaders-in-an-array/
//
//Write a program to print all the LEADERS in the array. An element is leader if it is greater than all the elements to its right side.
//
//Input: Array of numbers
//Output: Elements that are leaders in the array
//
//Complexity = O(n)


import static java.lang.System.out;
import java.util.Scanner;

public class ArrayLeaders{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);

        int T = in.nextInt();

        int i, j, k;
        int N;
        
        for(i=0;i<T;i++){
            N=in.nextInt();

            int[] arr = new int[1000];
            for(j=0;j<N;j++)
                arr[j]=in.nextInt();
            Leader(arr, N);
        }
    }
    static void Leader(int[] arr, int N){
        int i, maxSoFar;
        maxSoFar=arr[N-1];
        System.out.println(maxSoFar);
        if(N==1)
            return;

        for(i=N-2;i>=0;i--){
            if(arr[i]>maxSoFar){
                maxSoFar = arr[i];
                System.out.println(maxSoFar);
            }
        }
    }
}
