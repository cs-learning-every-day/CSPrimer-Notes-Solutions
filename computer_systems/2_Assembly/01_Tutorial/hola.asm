; ----------------------------------------------------------------------------------------
; This is an macOS console program that writes "Hola, mundo" on one line and then exits.
; It uses puts from the C library.  To assemble and run:
;
;     nasm -fmacho64 hola.asm && gcc hola.o && ./a.out
; ----------------------------------------------------------------------------------------

            global      _main
            extern      _puts
            
            section     .text
_main:      push        rbx                     ; Call Stack must be aligned
            lea         rdi, [rel message]      ; Load Effective Address, First argument is address of message. `rel` used to access variables, required when calling C libraries. Loading pointer into this address readies it for a funciton call
            call        _puts                   ; puts(message) - C Function
            pop         rbx                     ; Fix up stack before erturning
            ret

            section     .data
message:    db          "Hola, mundo", 0        ; C strings need a zero byte at the end
