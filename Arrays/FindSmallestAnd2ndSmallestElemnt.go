//http://www.geeksforgeeks.org/to-find-smallest-and-second-smallest-element-in-an-array/

// Print the 2 smallest numbers in an array in a single pass
// Time complextiy O(n)
// Space complexity O(1) - Streamable
package main

import "fmt"

func main() {
    b := [6]int{12, 13, 1, 10, 34, 1}
    smallest:=0
    second:=0

    if b[0] < b[1] {
        smallest= b[0]
        second = b[1]
    } else{
        smallest=b[1]
        second=b[0]
    }
    for i:=2; i<len(b); i++{
        if b[i] < smallest{
            second=smallest
            smallest=b[i]
        } else{
            if b[i] < second && b[i] < smallest{
                second=b[i]
            }        else{
            }
        }
    }
    fmt.Println("Smallest is", smallest, "\nsecond smallest is", second)
}
