# NASM Tutorial
## Structure of a NASM Program
- NASM 
    - Line-based
    - Programs consist of **directives**, followed by one or more **sections**
    - Lines can have an optional **label**
    - Most lines have an **instruction** followed by zero or more **operands**
    - General Rule
        - You put code in section called .text
        - Put constant data in a section called data

Program: hello.asm
|            |  Labels | Instructions |      Operands         |
|------------|---------|--------------|-----------------------|
| Directives |         |  `global`    |  `_main`              |
| Sections   |         |  `section`   |  `.text`              |
|            | `_main:`|  `mov`       |  `rax, 0x2000004`     |
|            |         |  `mov`       |  `rdi, 1`             |
|            |         |  `mov`       |  `rsi, message`       |
|            |         |  `mov`       |  `rdx, 13`            |
|            |         |  `syscall`   |                       |
|            |         |  `mov`       |  `rax, 0x2000001`     |
|            |         |  `xor`       |  `rdi, rdi`           |
|            |         |  `syscall`   |                       |
| Sections   |         |  `section`   |  `.data`              |
|            |`message`|  `db`        |  `"Hello, World", 10` |

## First Few Instructions
| Instruction | Description                                                 |
| ----------- | ----------------------------------------------------------- |
| `mov x,y`   | Places value of y into x                                    |
| `and x,y`   | Places result of `x & y` into x                             |
| `or x,y`    | Places result of `x | y` into x                             |
| `xor x,y`   | Places result of `xor(x,y)` into x                          |
| `add x,y`   | Places result of `x + y` into x                             |
| `sub x,y`   | Places result of `x - y` into x                             |
| `inc x`     | Places result of `x + 1` into x                             |
| `dec x`     | Places result of `x - 1` into x                             |
| `syscall n` | Invokes operating system routine `n`                        |
| `db`        | *Declares bytes* to be in memory when program runs          |

- Pseudo-Instruction
    - Not real x86 instructions
    - Used in instruction field anyway
        - Because it's the most convenient place to put them
    - Current Pseudo Instructions
        - DB, DW, DD, DQ, DT, DO, DY, DZ
            - Uninitialized Counterparts
                - RESB, RESW, RESD, RESQ, REST, RESO, RESY, RESZ
        - INCBIN
        - EQU
        - TIMES prefix

## Three Kinds of Operands
### Register Operands
- See rest of module notes for what the General Purpose Registers are
- Floating Point Registers (128 bits wide)
    - `XMM0`
    - `XMM1`
    - `XMM2`
    - `XMM3`
    - `XMM4`
    - `XMM5`
    - `XMM6`
    - `XMM7`
    - `XMM8`
    - `XMM9`
    - `XMM10`
    - `XMM11`
    - `XMM12`
    - `XMM13`
    - `XMM15`
### Memory Operands
- Base forms of addressing
    - `[ number ]` 
        - Called the **displacement**
    - `[ reg ]` 
        - Called the **base**
    - `[ reg + reg*scale ]` 
        -  `scale` is 1, 2, 4 or 8 only
        - Register that is scaled up is called the **index**
    - `[ reg + number ]` 
    - `[ reg + reg*scale + number ]` 

Examples:
```nasm
[750]               ; displacement only  
[rbp]               ; base register only  
[rcx + rsi*4]       ; base + index * scale    
[rbp + rdx]         ; scale is 1, index is rdx   
[rbx - 8]           ; displacement is -8 
[rax + rdi*8 + 500] ; all four components
[rbx + counter]     ; uses the address of the variable 'counter' as the displacement 
```

### Immediate Operands
```nasm
200         ; decimal
0200        ; still decimal - leading 0 doesn't make it octal
0200d       ; explicitly decimal - d suffix
0d200       ; also decimal - 0d prefix
0c8h        ; hex - h suffix, but leading 0 is requierd b/c c8h looks like a var
0xc8        ; hex - classic 0x prefix
0hc8        ; hex - for some reason NASM likse 0h
310q        ; octal - q suffix
0q310       ; octal - 0q prefix
11001000b   ; binary - b suffix
0b1100_1000 ; binary - 0b prefix (underscores are allowed throughout)
```

### Basic Instruction Forms
- Instructions with two memory operands are extremly rare
- Most common forms
    - `add reg, reg`
    - `add reg, mem`
    - `add reg, imm`
    - `add mem, reg`
    - `add mem, imm`

### Defining Data and Reserving Space
#### Placing data in memory
```nasm
db 0x55                  ; just the byte 0x55
db 0x55, 0x56, 0x57      ; three bytes in succession
db 'a', 0x55             ; character constants are OK
db 'hello',13,10,'$'     ; So are string constants
dw 0x1234                ; 0x34 0x12
dw 'a'                   ; 0x61 0x00 (just a number)
dw 'ab'                  ; 0x51 0x62 (character constant)
dw 'abc'                 ; 0x61 0x62 0x63 0x00 (string)
dd 0x12345678            ; 0x78 0x56 0x34 0x12
dd 1.234567e20           ; floating-point constant
dq 0x123456789abcdef0    ; eight byte constant
dq 1.234567e20           ; double-precision float
dt 1.234567e20           ; extended-precision float
```

#### Reserving space in memory (without initializing)
- Should go in `.bss` section, will throw an error if you try to put them in `.text`
```nasm
buffer:       resb 64     ; reserve 64 bytes
wordvar:      resw 1      ; reserve a word
realarray:    resw 1      ; array of ten reals
```

### Using a C Library
- See hola.asm
- Requirements
    - C functions (or any function exported from one module to another)
        - Must be prefixed with underscores
    - Call stack (rsp) must be aligned on a 16-byte boundary
    - When accessing named variables, `rel` prefix is required

### Understanding Calling Conventions
- Calling Conventions set by AMD64 ABI Reference
- Pass as many parameters as will fit in registers
    - Order in which registers are allocated
        - Integers and Pointers
            - rdi, rsi, rdx, rcx, r8, r9
        - Floating Point (float, double)
            - xmm0, xmm1, xmm2, xmm3, xmm4, xmm5, xmm6, xmm7
    - Additional Parameters
        - Pushed on the stack (rsp), right to left
        - *Removed by the caller* after the call
        - After parameters are pushed, call instruction is made
            - Return address is at [rsp]
            - First memory parameter is at [rsp+8]
        - Stack pointer `rsp` must be aligned to a 16 byte boundary before making a call
            - You have to push something, or subtract 8 from `rsp`
- Registers the called function is required to preserve (caller-save registers)
    - `rbp`, `rbx`, `r12`, `r13`, `r14`, `r15`
    - All others are free to be changed by the called function
- Integers are returned in `rax` or `rdx:rax` 
    - Floating point values are returned in `xmm0` or `xmm1:xmm0`

### Fibonacci Program
- See fib.asm
- New Instructions
    - `push x`
        - Decrement `rsp` by the size of the operand, then store `x` in `[rsp]`
    - `pop x`
        - Move `[rsp]` into `x`, then increment `rsp` by the size of the operand
    - `jnz label`
        - If the processor's Z (zero) flag is set, jump to the given label
    - `call label`
        - Push the address of the next instruction, then jump to the label
    - `ret`
        - Pop into the instruction pointer

## Mixing C and Assembly Language
- Consider the following Assembly Program
```asm
; -----------------------------------------------------------------------------
; A 64-bit function that returns the maximum value of its three 64-bit integer
; arguments.  The function has signature:
;
;   int64_t maxofthree(int64_t x, int64_t y, int64_t z)
;
; Note that the parameters have already been passed in rdi, rsi, and rdx.  We
; just have to return the value in rax.
; -----------------------------------------------------------------------------

        global  maxofthree
        section .text
maxofthree:
        mov     rax, rdi                ; result (rax) initially holds x
        cmp     rax, rsi                ; is x less than y?
        cmovl   rax, rsi                ; if so, set result to y
        cmp     rax, rdx                ; is max(x,y) less than z?
        cmovl   rax, rdx                ; if so, set result to z
        ret                             ; the max will be in rax
```

- C Progrma that calls this function
```C
/*
 * A small program that illustrates how to call the maxofthree function we wrote in
 * assembly language.
 */

#include <stdio.h>
#include <inttypes.h>

int64_t maxofthree(int64_t, int64_t, int64_t);

int main() {
    printf("%ld\n", maxofthree(1, -4, -7));
    printf("%ld\n", maxofthree(2, -6, 1));
    printf("%ld\n", maxofthree(2, 3, 1));
    printf("%ld\n", maxofthree(-2, 4, 3));
    printf("%ld\n", maxofthree(2, -6, 5));
    printf("%ld\n", maxofthree(2, 4, 6));
    return 0;
}
```

- To compile the asm code and execute the C program (Linux)
    - `nasm -felf64 maxofthree.asm && gcc callmaxofthree.c maxofthree.o && ./a.out`
    

## Conditional Instructions
- After arithmetic or logic instruction, or `cmp` instruction, the processor set or clear bits in `rflags`
    - Interesting flags
        - `s` -> sign
        - `z` -> zero
        - `c` -> carry
        - `o` -> overflow
- This allows us to perform a jump, move or est based on the new flag settings
- Examples
    - `jz L`
        - Jump to Label L if the result of the previous operation was zero
    - `cmovno x,y`
        - x <- y if the last operation did not overflow
    - `setc x`
        - x <- 1 if the last operation had a carry, but x <- 0 otherwise
        - x must be a byte-size register or memory location
- There base forms for conditional instructions
    - `j` -> Conditional Jump
    - `cmov` -> Conditional Move
    - `set` -> Conditional Set
- Conditional Instruction suffixes
    - Examples
        - le -> Less or equal
        - z -> zero
        - nz -> not zero


## Command Line Arguments
- In C
    - `main` function is -> `int main(int argc, char** argv)`
- In assembly
    - `argc` is in `rdi`
    - `argv` (pointer) is in `rsi
- See `echo.asm`
