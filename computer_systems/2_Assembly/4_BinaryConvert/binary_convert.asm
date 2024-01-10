section .text
global binary_convert
binary_convert:
	xor eax, eax ; zero out eax
	movzx edx, byte [rdi] ; Read byte from RDI
	cmp edx, 0x31
	sete al
	ret
