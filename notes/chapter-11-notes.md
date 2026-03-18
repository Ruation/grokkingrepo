# Other Important Algorithms and Concepts

## Trees

A **tree** is a hierarchical data structure made of nodes connected by edges.  
It has a **root node**, and each node may have children.

Trees are widely used to represent hierarchical data such as file systems, databases, and decision processes.

Common types include:

- Binary trees
- Binary search trees
- Heaps
- B-trees

---

## Inverted Index

An **inverted index** is a data structure used by search engines.

Instead of mapping documents to words, it maps **words to the documents that contain them**.

Example:

apple → [doc1, doc4]  
banana → [doc2]

This structure allows search engines to quickly find documents containing specific terms.

---

## Fourier Transform

The **Fourier Transform** is a mathematical technique that converts a signal from the **time domain** to the **frequency domain**.

It is used in areas such as:

- Signal processing
- Image compression
- Audio analysis

It helps identify the different frequencies that make up a signal.

---

## Parallel Algorithms

**Parallel algorithms** divide a task into smaller parts that can run **simultaneously on multiple processors**.

This approach speeds up computation and is widely used in high-performance computing and large-scale data processing.

Challenges include coordinating tasks and managing communication between processors.

---

## MapReduce

**MapReduce** is a programming model used to process large datasets across many computers.

It has two main phases:

- **Map:** process and transform data into key–value pairs
- **Reduce:** combine results with the same key

MapReduce allows large-scale data processing in distributed systems.

---

## Bloom Filters and HyperLogLog

**Bloom filters** are probabilistic data structures used to test whether an element is in a set.

They are very memory-efficient but may produce **false positives**.

**HyperLogLog** is another probabilistic algorithm used to **estimate the number of unique elements** in a large dataset.

Both are commonly used in large-scale data systems.

---

## SHA Algorithms

The **SHA (Secure Hash Algorithm)** family consists of cryptographic hash functions.

They convert data into a fixed-length hash value.

Properties:

- Deterministic
- Fast to compute
- Hard to reverse
- Small changes in input produce very different hashes

They are used in:

- Password storage
- Data integrity
- Cryptography
- Blockchain systems

---

## Diffie–Hellman Key Exchange

The **Diffie–Hellman key exchange** is a cryptographic method that allows two parties to securely share a secret key over an insecure channel.

Both parties generate private numbers and exchange derived values.

Using mathematical properties, they can compute the same shared secret without transmitting it directly.

This method is widely used in secure communication protocols.

---

## Linear Programming

**Linear programming** is a mathematical method used to optimize a linear objective function subject to linear constraints.

It is used to find the best possible outcome in problems such as:

- Resource allocation
- Production planning
- Transportation optimization

The goal is to maximize or minimize a value while respecting constraints.
