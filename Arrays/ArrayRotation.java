//http://www.geeksforgeeks.org/array-rotation/
//
//Given an array, rotate the array. (i.e imagine array as a circular list and push list forward 'd' steps. 
//Eg with d=2 and arr={1,2,3,4,5}, soln={4, 5, 1, 2, 3}
//
//Time Complexity = O(n)
//
//If using extra array, space complexity = O(n)
//If doing dynamic series of swaps, algorithm can be performed in place

import static java.lang.System.out;
import java.util.Scanner;

public class ArrayRotation {
    public static void main(String[] args){
        int[] array= {1, 2, 3, 4, 5, 6, 7, 8, 9};
        int d = 3;
        arrayRotate(array, d);
    }
    static void arrayRotate(int[] array, int d){
        //Static series of swaps
        int length = array.length;
        int i, j, k, temp;
        int pos;
        for(i=0;i<length;i++){
            pos=(i+d)%length;
            temp=array[i];
            array[i]=array[pos];
            array[pos]=temp;
        }

        for(i=0;i<length;i++)
            System.out.println(array[i]);

        

    }
    
}

