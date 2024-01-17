default rel

section .text
global volume

volume:
    mulss xmm0, xmm0 ; V = r * r
    mulss xmm0, xmm1 ; V  *= h
    mulss xmm0, [pi_on_3] ; V *= pi/3
    ret


section .rodata
pi_on_3: dd 1.0471975512
