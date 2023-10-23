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
