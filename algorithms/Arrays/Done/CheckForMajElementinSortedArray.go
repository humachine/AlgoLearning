//http://www.geeksforgeeks.org/check-for-majority-element-in-a-sorted-array/
/* Given a sorted array A and a number x, check if x is the majority element in A (Maj element = count(x) > len(A)/2
Time Complexity = O(logn)
Space Complexity = O(1) extra space
*/

package main

import "fmt"

func binSearchMin(arr[100] int, X, left, right int) int {
    mid:=(left + right)/2
    for mid > left {
        //fmt.Println(left, mid, right)
        if arr[mid] < X{
            left=mid
        }else{
            right=mid
        }
        mid=(left + right)/2
    }
    //fmt.Println(left, mid, right)
    return mid
}
func binSearchMax(arr[100] int, X, left, right int) int {
    mid:=(left + right)/2
    for mid > left {
        //fmt.Println(left, mid, right)
        if arr[mid] <= X{
            left=mid
        }else{
            right=mid
        }
        mid=(left + right)/2
    }
    //fmt.Println(left, mid, right)
    return mid

}


func main() {
    var N int
    fmt.Scanf("%d", &N)

    var arr[100] int
    for i:=0; i<N; i++{
        fmt.Scanf("%d", &arr[i])
    }

    var X int
    fmt.Scanf("%d", &X)

    fmt.Println(arr[:N])
    leftlim:=(binSearchMin(arr, X, 0, N))

    if arr[leftlim]==X {
        if arr[leftlim+N/2]==X{
            fmt.Println(X, "is the majority element")
        }
    }else {
        if arr[leftlim+N/2+1]==X{
            fmt.Println(X, "is the majority element")
        }
    }
}
