section .text
global pangram

pangram:
	call _prep

_prep: 
	xor rsi, rsi ; Create bitset
	xor rax, rax ; Prep - zero out rax
	xor rcx, rcx ; Prep - Zero out rcx
	xor rdx, rdx ; Prep - zero out rdx
	xor rbp, rbp ; Prep - zero out rbp
	mov dl, 0x1f ; Move value into dl for masking
	mov r11d, 0x07fffffe ; MOve value into r11d for masking

_looping: 
	mov al, [rdi] ; Read first byte from rdi
	cmp al, 0x00; Compare byte to 0
	jz _exit; If 0, jump to exit
	cmp al, 0x40 ; Ignore first 64 chars of ascii
	jl _looping ; Take next byte if it is any lower than 64
	and al, dl ; Bitwise and of al register to mask out 0x1f
	mov cl, al ; Move result of comparison into cl register
	mov rbp, 0 ; Zero out rbp
	mov bpl, 0x01 ; Put 1 into an empty register
	shl ebp, cl ; Shift 1 by number of bits in al
	or esi, ebp ; Bitwise or of bitset and result in r9
	add rdi, 0x01 ; Increment rdi by 1 bit
	jmp _looping ; Continue Looping 

_exit:
	and esi, r11d ; Mask out lower bit values
	cmp esi, r11d ; Compare to mask
	sete eax ;
	jz decline ; If equal to mask - then return 0 else 1

_exit: 
	

_res:
	mov eax, 0
	ret


_decline:
	mov eax, 1
	ret ; 

	
		section		.data
mask1:  db			0x1f         
mask2:	dq			0x07fffffe

