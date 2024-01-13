section .text
global binary_convert

binary_convert:
	xor eax, eax

.loop:
	movzx ecx, byte [rdi]
	cmp ecx, 0
	je .end
	and ecx, 1 ; TODO this assumes that ecx is DEFEINITELY '0' or '1'
	; we only retain the lower order bit of the ascii
	shl eax, 1 ; Shift left accumulator by 1
	add eax, ecx
	add rdi, 1
	jmp .loop
.end:
	ret
