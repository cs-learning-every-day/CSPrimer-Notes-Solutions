; Mov is turing complete, any computable program can be rewritten in just mov instructions
;
;

section .text
global index, _main
_main:

index:
	; TODO - Make General
	imul ecx, edx ; Multiply indices by 4 bytes to get offset
	add ecx, r8d
	imul ecx, ecx, 4
	add rdi, rcx ; Add offset to matrix pointer
	mov rax, [rdi] ; Dereference pointer to rax
	; rdi: matrix
	; esi: rows
	; edx: cols
	; ecx: rindex
	; r8d: cindex
	ret 
