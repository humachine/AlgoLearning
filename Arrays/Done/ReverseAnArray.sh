#!/bin/bash
#http://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/
#Reversing an array in bash. O(n)
read numelem
read -a elements

echo hello
for (( i=$(($numelem-1)); i>=0; i-- ))
do
    echo ${elements[$i]}
done
