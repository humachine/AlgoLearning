//http://www.geeksforgeeks.org/leaders-in-an-array/
//
//A leader is an element that's greater than all elements to its right in the array. 
//Print all the leaders in a given array
//
//Time Complexity = O(n) - One iteration
//Space Complexity = zero extra space. 
//This is also a streaming algorithm


public class ArrayLeaders {
    public static void main(String[] args){
        int[] arr = {16, 17, 4, 3, 5, 2};
        int i, j, k, max;

        max=arr[arr.length-1];
        System.out.println(max);
        for(i=arr.length-2;i>=0;i--){
            if(arr[i]>max){
                max=arr[i];
                System.out.println(max);
            }
        }
    }
}
