; ----------------------------------------------------------------------------------------
; This is an macOS console program that writes a little triangle of asterisks to standard
; output. Runs on macOS only.
;
;     nasm -fmacho64 triangle.asm && gcc hola.o && ./a.out
; ----------------------------------------------------------------------------------------

; NOTES
; cmp -> Comparison
; je (jump if equal) -> Jumps to a label if previous comparison was equal. Lots of versions like jne (jump not equal), jng (jump not greater), etc.
; equ -> Not a real instruction; defines an abbreviation for the assembler itself to use. It is used to give names to constants, which can be used elsewhere in the program
; .bss section -> Writable data


            global  _main
            section .text
_main:
            mov     rdx, output         ; rdx holds address of next byte to write
            mov     r8, 1               ; initial line length
            mov     r9, 0               ; number of stars written on line so far
line:
            mov     byte [rdx], '*'     ; write single star
            inc     rdx                 ; advance pointer to next cell to write
            inc     r9                  ; "count" number so far on line
            cmp     r9, r8              ; did we reach the number of stars for this line?
            jne     line                ; not yet, keep writing on this line
lineDone:
            mov     byte [rdx], 10      ; write a new line char
            inc     rdx                 ; move pointer to where next char goes
            inc     r8                  ; next line will be one char longer
            mov     r9, 0               ; reste count of stars written on this line
            cmp     r8, maxlines        ; wait, did we already finish the last line?
            jng     line                ; if not, begin writing this lin e
done:
            mov     rax, 0x02000004     ; system call for write
            mov     rdi, 1              ; file handle 1 is stdout (Syscall Param 1)
            mov     rsi, output         ; address of string to output (Syscall Param 2)
            mov     rdx, dataSize       ; number of bytes (Syscall Param 3)
            syscall                     ; invoking operating system to do the write
            mov     rax, 0x02000001     ; system call for exit
            xor     rdi, rdi            ; exit code 0
            syscall                     ; invoke operating system to exit

; This section sets up constants and uninitializes memory addresses we want to write to (i.e. output

            section .bss
maxlines    equ     8
dataSize    equ     44
output:     resb    dataSize


        
