%define MASK 0x07fffffe

section .text
global pangram

pangram:
	; rdi: source string
	xor ecx, ecx ; bs = 0

.loop:
	movzx edx, byte [rdi] ; movzx -> fill remainder 3 bytes with 0
						  ; other 32 bits in 64 bit register are zeroed out automatically
					      ; by operations on 32 bit register
	cmp edx, 0
	je .end
	add rdi, 1  ; s++
	cmp edx, '@'  ; if c is in first 64 bits of ascii table,
	jl .loop      ; continue
;	and edx, 0x1f ; Not needed b/c of behavior of bts wrapping around 32 bit integers
	bts ecx, edx  
	jmp .loop

.end:
	xor eax, eax
	and ecx, MASK
	cmp ecx, MASK
	sete al
	ret

