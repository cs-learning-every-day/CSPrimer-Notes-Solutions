section .text
global pangram
pangram:
	mov rsi, 0 ; Create bitset
	mov r10, 0x17f ; Move value into r10 for masking
	mov r11, 0x07fffffe ; MOve value into r11 for masking


loop: 
	mov rax, [rdi] ; Read first byte from rdi
	cmp rax, 0; Compare to 0
	jz res; If 0, jump to exit
	cmp rax, 64 ; Ignore first 64 chars of ascii
	jl loop ; Take next byte if is any lower than 64
	and rax, r10 ; Bitwise and of al register to mask out 0x1f
	mov r9, 1 ; Put 1 into an empty register
	shl r9, rax ; Shift 1 by number of bits in al
	or rsi, r9 ; Bitwise or of bitset and result in r9
	and rsi, r11 ; Mask out lower bit values
	cmp rsi, r11 ; Compare to mask
	jz res ; If equal to mask - then return 0 else 1

decline:
	mov eax, 1
	ret ; 

res:
	mov eax, 0
	ret

	
