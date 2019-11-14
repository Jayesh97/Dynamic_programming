## Memory Layout of C Programs



## Text segment

As a memory region, a text segment may be placed below the heap or stack in order to prevent heaps and stack overflows from overwriting it.

the text segment is often read-only, to prevent a program from accidentally modifying its instructions.


## Initialized data segment

initialized read-only area 

* s[] = “hello world”

initialized read-write area.

* char* string = “hello world”

## Uninitialized data segment

uninitialized data starts at the end of the data segment and contains all global variables and static variables that are initialized to zero or do not have explicit initialization in source code.

## Stack

The stack area traditionally adjoined the heap area and grew the opposite direction; when the stack pointer met the heap pointer, free memory was exhausted

A “stack pointer” register tracks the top of the stack; it is adjusted each time a value is “pushed” onto the stack. 

The set of values pushed for one function call is termed a “stack frame”; A stack frame consists at minimum of a return address.

## Heap





