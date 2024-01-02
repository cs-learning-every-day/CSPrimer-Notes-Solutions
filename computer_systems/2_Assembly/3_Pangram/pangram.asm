section .text
global pangram
pangram:
	mov esi, 0 ; Create bitset
	mov dl, 0x1f ; Move value into dl for masking
	mov r11d, 0x07fffffe ; MOve value into r11d for masking

looping: 
	mov al, [rdi] ; Read first byte from rdi
	cmp al, 0; Compare byte to 0
	jz masking; If 0, jump to exit
	cmp al, 0x40 ; Ignore first 64 chars of ascii
	jl looping ; Take next byte if it is any lower than 64
	and al, dl ; Bitwise and of al register to mask out 0x1f
	mov cl, al ; Move result of comparison into cl register
	mov rbp, 0 ; Zero out ecx
	mov bpl, 0x01 ; Put 1 into an empty register
	shl ebp, cl ; Shift 1 by number of bits in al
	or esi, ebp ; Bitwise or of bitset and result in r9
	add rdi, 0x01 ; Increment rdi by 1 bit
	jmp looping ; Continue Looping 

masking:
	and esi, r11d ; Mask out lower bit values
	cmp esi, r11d ; Compare to mask
	jz decline ; If equal to mask - then return 0 else 1

res:
	mov eax, 0
	ret


decline:
	mov eax, 1
	ret ; 

	
