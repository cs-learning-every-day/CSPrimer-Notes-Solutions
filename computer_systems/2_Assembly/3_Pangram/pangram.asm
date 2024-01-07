section .text
global pangram

pangram:
	xor rsi, rsi ; Create bitset
	xor rax, rax ; Prep - zero out rax
	xor rcx, rcx ; Prep - Zero out rcx
	xor rdx, rdx ; Prep - zero out rdx
	xor rbp, rbp ; Prep - zero out rbp

_looping: 
	mov al, [rdi] ; Read first byte from rdi
	cmp al, 0x00; Compare byte to 0
	jz _exit; If 0, jump to exit
	cmp al, 0x40 ; Ignore first 64 chars of ascii
	jl _looping ; Take next byte if it is any lower than 64
	and al, 0x1f ; Bitwise and of al register to mask out 0x1f
	mov cl, al ; Move result of comparison into cl register
	mov rbp, 0 ; Zero out rbp
	mov bpl, 0x01 ; Put 1 into an empty register
	shl ebp, cl ; Shift 1 by number of bits in al
	or esi, ebp ; Bitwise or of bitset and result in r9
	add rdi, 0x01 ; Increment rdi by 1 bit
	jmp _looping ; Continue Looping 

_exit:
	and esi, 0x07fffffe ; Mask out lower bit values
	cmp esi, 0x07fffffe ; Compare to mask
	sete al ; Set result of comparison to eax
	ret

