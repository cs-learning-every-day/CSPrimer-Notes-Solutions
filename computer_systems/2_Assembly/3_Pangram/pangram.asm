section .text
global pangram
pangram:
	mov rsi, 0 ; Create bitset
	mov al, [rdi] ; Read first byte from rdi
	cmp al, 0; Compare to 0
	jz res; If 0, jump to exit

res:
	cmp rsi, 0x03ffffff
	jz decline
	mov eax, 0
	ret

decline:
	mov eax, 1
	ret ; 
	
