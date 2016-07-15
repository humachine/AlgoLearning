//http://www.geeksforgeeks.org/find-the-missing-number/
//
//Given a list of N-1 numbers from 1 to N find the missing number.
//Input: Array of N-1 numbers
//Output: Missing Number
import java.util.Scanner;

public class MissingNumber{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);

        int T = in.nextInt();
        int N;
        int temp, result, i, j;

        for(i=0;i<T;i++){
            N=in.nextInt();
            result=0;

            for(j=0;j<N-1;j++){
                temp=in.nextInt();
                result=result^temp;
                result=result^(j+1);
            }
            result=result^N;
            System.out.println(result);
            
        }
    }
}
