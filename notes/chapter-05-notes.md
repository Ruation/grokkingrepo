# Hash Tables

A hash table is a data structure used to store key–value pairs and provide very fast lookup, insertion, and deletion operations.
Instead of searching through all elements, a hash table uses a hash function to compute an index where the value should be stored.

This allows most operations to run in constant time.


## How Hash Tables Work

A hash table has two main components:
- Array
- Hash function

The hash function takes a key as input and returns an index in the array.

## Example:

hash("apple") → 3
The value associated with "apple" is stored at position 3 in the array.

Example

Suppose we store phone numbers:
"alice" → 555-1234
"bob"   → 555-9876

The hash function maps each name to an index in the array where the phone number is stored.


## Time Complexity

Average case:
Search	O(1)
Insert	O(1)
Delete	O(1)

Worst case:
Search	O(n)
The worst case happens when many keys map to the same index.


## Collisions

A collision happens when two keys produce the same array index.

Example:

hash("alice") → 2
hash("alex")  → 2

Two common ways to handle collisions are:

- Chaining
Each array slot stores a linked list of elements.

- Open Addressing
The algorithm searches for another empty position in the array.


## Load Factor

The load factor measures how full the hash table is.

load factor = number of elements / number of slots

If the load factor becomes too high, performance decreases.

To solve this, hash tables resize and create a larger array.


## Advantages

- Very fast lookups
- Efficient insertions and deletions
- Ideal for key–value data


## Common Uses

Hash tables are widely used in programming:

- Dictionaries / maps
- Caches
- Databases
- Counting frequencies
- Storing user information

# Chapter 5 exercises

➡️ [Exercises](../exercises/chapter-05-exercises.md)