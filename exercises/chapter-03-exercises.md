## 3.1 Suppose I show you a call stack like this. 

GREET2 (name: maggie)   ← top of stack
GREET  (name: maggie)

What information can you give me, just based on this call stack? 

1️⃣ greet2 is currently executing

- Because it’s on the top of the stack, greet2 hasn’t finished yet.

2️⃣ greet called greet2

- Since greet is below greet2, that means:
- greet() was running
- Inside greet(), it called greet2()
- Execution moved to greet2()

## 3.2 Suppose you accidentally write a recursive function that runs forever. As you saw, your computer allocates memory on the stack for each function call. What happens to the stack when your recursive function runs forever?

If a recursive function runs forever, it keeps adding new function calls to the call stack. Since each call uses memory, the stack keeps growing until it reaches its memory limit. When this happens, a stack overflow occurs and the program crashes.