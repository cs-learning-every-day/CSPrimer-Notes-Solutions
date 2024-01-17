default rel

section .text
global volume

;section .data
;    const            dd 3.14159

volume:
    ;; Load 3 into xmm3
    mov edx, 3 
    ;; Loading into xmm2 as a 32 bit float
    cvtsi2ss xmm2, edx
    ;; Load pi into xmm3 as a 32 bit float
    mov eax,__?float32?__(3.14159)
    movd xmm3,eax
    ;; Square the radius - mulss multiplies 32 bit floats
    mulss xmm0, xmm0
    ;; Multiply by pi
    mulss xmm0, xmm3
    ;; Multiply by height
    mulss xmm0, xmm1
    ;; Divide by 3
    divss xmm0, xmm2
    ret
