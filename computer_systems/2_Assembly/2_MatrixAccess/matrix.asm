; Mov is turing complete, any computable program can be rewritten in just mov instructions
;
;
; rdi: matrix
; esi: rows
; edx: cols
; ecx: rindex
; r8d: cindex

; Simplifications:
; Understanding the microarchitecture reveals that these 
; changes don't actually make any difference

section .text
global index, _main
_main:

index:
	imul ecx, edx ; Multiply rows by index
	add ecx, r8d ; Add column index to intermediate result
	mov eax, [rdi + 4 * rcx] ; Dereference pointer to rax
	ret 
