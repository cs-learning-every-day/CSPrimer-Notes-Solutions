; ----------------------------------------------------------------------------------------
; Writes "Hello, World" to the console using only system calls. Runs on 64-bit macOS only.
; To assemble and run:
;
;     nasm -fmacho64 hello_mac.asm && ld -lSystem hello_mac.o && ./a.out
;
; Derived from the NASM tutorial at https://cs.lmu.edu/~ray/notes/nasmtutorial/
; ----------------------------------------------------------------------------------------

          global    _main ; Tells the assembler to include this label in the output for linking

          section   .text ; Defines a section of machine code segments into the text part of memory
_main:    mov       rax, 0x02000004         ; system call for write
          mov       rdi, 1                  ; file handle 1 is stdout
          mov       rsi, message            ; address of string to output
          mov       rdx, 13                 ; number of bytes
          syscall                           ; invoke operating system to do the write
          mov       rax, 0x02000001         ; system call for exit
          mov       rdi, 0                ; exit code 0 - performs an xor on the values of rdi registers (xor-ing always results in 0)
                                            ; The above uses one fewer byte than mov 0
          syscall                           ; invoke operating system to exit

          section   .data
message:  db        "Hello, World", 10      ; note the byte-value for the newline character (10) at the end


; - Hello World is slightly complicated at low leve
;   - We want to write a string to standard out (requires a system call)
; - Disassembly
;   - AT&T vs. Intel Syntax
;       - Intel Syntax is easier to read
;       - Objdump Flag for intel: -M intel
; - Examining registers with lldb
;   - eax vs. rax
;        - eax is the last 4 bytes
;        - rax is the full 8 byte register
;   - You can't use this e syntax other than for the first 8 numbered registers it seems
;        - Works for
;            - rax (eax)
;            - rbx (ebx)
;            - rcx (eax)
;            - rdx (eax)
;            - rdi (eax)
;            - rsi (eax)
;            - rbp (eax)
;            - rsp (esp)
;   - In lldb -> reg re <register> to see value in register


