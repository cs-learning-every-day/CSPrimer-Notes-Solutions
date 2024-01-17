default rel

section .text
global volume

;section .data
;    const            dd 3.14159

volume:
    ; V = r * r * h * pi / 3
    ;; Load 3 into xmm3
    mov edx, 3 
    ;; Loading into xmm2 as a 32 bit float
    cvtsi2ss xmm2, edx
    ;; Load pi into xmm3 as a 32 bit float
    mov eax,__?float32?__(3.14159)
    movd xmm3,eax
    mulss xmm0, xmm0 ; V = r * r
    mulss xmm0, xmm1 ; V *= h
    mulss xmm0, xmm3 ; V *= pi 
    divss xmm0, xmm2 ; V /= 3
    ret
