## 4.1 Write out the code for the earlier sum function.

➡️ [View sum function with recursion implementation](../code/sum_recursive.py)

## 4.2 Write a recursive function to count the number of items in a list.

➡️ [View count function with recursion implementation](../code/count_recursive.py)

## 4.3 Find the maximum number in a list.

➡️ [View maximum number function with recursion implementation](../code/maxnum_recursive.py)


## 4.4 Remember binary search from chapter 1? It’s a divide-and-conquer algorithm, too. Can you come up with the base case and recursive case for binary search?

The base case is when the number of guesses is one. The recursive case is dividing the number of chances by 2 and eliminates half of the elements.

# How long would each of these operations take in Big O notation?


## 4.5 Printing the value of each element in an array. 

O(n)

## 4.6 Doubling the value of each element in an array.

O(n)

## 4.7 Doubling the value of just the first element in an array. 

O(1)

## 4.8 Creating a multiplication table with all the elements in the array. So if your array is [2, 3, 7, 8, 10], you first multiply every element by 2, then multiply every element by 3, then by 7, and so on.

O(n²)