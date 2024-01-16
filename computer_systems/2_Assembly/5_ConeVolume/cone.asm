default rel

section .text
global volume

section .data
    data            dq 3.14159
volume:
    mov edx, 3
    movlpd  xmm3, [data]
    cvtsi2sd xmm2, edx
    mulsd xmm0, xmm1
    mulsd xmm0, xmm3
    divsd xmm0, xmm2
    ret
