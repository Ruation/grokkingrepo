## 1.1 Suppose you have a sorted list of 128 names, and you're searching through it using bynary search. What's the maximum number of steps it would take?

maximum_number = log₂(128) = 7

## 1.2 Suppose you double the size of the list. What's the maximum number of steps now?

new_maximum = log₂(256) = 8

# Give the run time for each of these scenarios in terms of Big O

## 1.3  You have a name, and you want to find the person’s phone number in the phone book.

O(log n), because you can use binary search.

## 1.4 You have a phone number, and you want to find the person’s name in the phone book. (Hint: You’ll have to search through the whole book!)

O(n), because the book is sorted by name, not by phone number.
You must scan the entire book in the worst case.

## 1.5 You want to read the numbers of every person in the phone book.

O(n)

## 1.6 You want to read the numbers of just the As. (his is a tricky one! It involves concepts that are covered more in chapter 4. Read the answer—you may be surprised!)

O(n), because Big O notation measures the worst-case scenario. In the worst case, all names could start with the letter A, so you may need to read every entry in the list.