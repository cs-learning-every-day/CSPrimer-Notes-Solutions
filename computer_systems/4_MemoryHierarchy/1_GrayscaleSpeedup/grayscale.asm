
0000000100003bd0 <_grayscale>:
100003bd0: d10083ff     sub     sp, sp, #32             ; Allocate 32 bytes on the stack
100003bd4: f9000fe0     str     x0, [sp, #24]          ; Store argument x0 at [sp + 24]
100003bd8: b90017e1     str     w1, [sp, #20]          ; Store argument w1 at [sp + 20]
100003bdc: b90013e2     str     w2, [sp, #16]          ; Store argument w2 at [sp + 16]
100003be0: b9000fff     str     wzr, [sp, #12]         ; Store zero at [sp + 12]
100003be4: 14000001     b       0x100003be8 <_grayscale+0x18>  ; Branch to the next instruction
100003be8: b9400fe8     ldr     w8, [sp, #12]          ; Load the value at [sp + 12] into w8
100003bec: b94017e9     ldr     w9, [sp, #20]          ; Load the value at [sp + 20] into w9
100003bf0: 6b090108     subs    w8, w8, w9            ; Subtract w9 from w8 and update flags
100003bf4: 1a9fb7e8     cset    w8, ge                ; Set w8 to 1 if result is greater than or equal, 0 otherwise
100003bf8: 37000928     tbnz    w8, #0, 0x100003d1c <_grayscale+0x14c>  ; Branch if the result is not zero
100003bfc: 14000001     b       0x100003c00 <_grayscale+0x30>  ; Branch to the next instruction
100003c00: b9000bff     str     wzr, [sp, #8]          ; Store zero at [sp + 8]
100003c04: 14000001     b       0x100003c08 <_grayscale+0x38>  ; Branch to the next instruction
100003c08: b9400be8     ldr     w8, [sp, #8]           ; Load the value at [sp + 8] into w8
100003c0c: b94013e9     ldr     w9, [sp, #16]          ; Load the value at [sp + 16] into w9
100003c10: 6b090108     subs    w8, w8, w9            ; Subtract w9 from w8 and update flags
100003c14: 1a9fb7e8     cset    w8, ge                ; Set w8 to 1 if result is greater than or equal, 0 otherwise
100003c18: 37000788     tbnz    w8, #0, 0x100003d08 <_grayscale+0x138>  ; Branch if the result is not zero
100003c1c: 14000001     b       0x100003c20 <_grayscale+0x50>  ; Branch to the next instruction
100003c20: b9400be8     ldr     w8, [sp, #8]           ; Load the value at [sp + 8] into w8
100003c24: b94017e9     ldr     w9, [sp, #20]          ; Load the value at [sp + 20] into w9
100003c28: 1b097d08     mul     w8, w8, w9            ; Multiply w8 by w9
100003c2c: b9400fe9     ldr     w9, [sp, #12]          ; Load the value at [sp + 12] into w9
100003c30: 0b090109     add     w9, w8, w9            ; Add w8 to w9
100003c34: 52800068     mov     w8, #3                ; Load the value 3 into w8
100003c38: 1b097d08     mul     w8, w8, w9            ; Multiply w8 by w9
100003c3c: b90007e8     str     w8, [sp, #4]           ; Store w8 at [sp + 4]
100003c40: f9400fe8     ldr     x8, [sp, #24]          ; Load the value at [sp + 24] into x8
100003c44: b98007e9     ldrsw   x9, [sp, #4]           ; Load the signed value at [sp + 4] into x9
100003c48: 8b090108     add     x8, x8, x9            ; Add x9 to x8
100003c4c: 39400108     ldrb    w8, [x8]              ; Load the byte at address x8 into w8
100003c50: 1e630101     ucvtf   d1, w8                ; Convert w8 to double-precision floating-point and store in d1
100003c54: f9400fe8     ldr     x8, [sp, #24]          ; Load the value at [sp + 24] into x8
100003c58: b94007e9     ldr     w9, [sp, #4]           ; Load the value at [sp + 4] into w9
100003c5c: 11000529     add     w9, w9, #1             ; Increment w9 by 1
100003c60: 8b29c108     add     x8, x8, w9, sxtw      ; Add w9 (sign-extended) to x8
100003c64: 39400108     ldrb    w8, [x8]              ; Load the byte at address x8 into w8
100003
