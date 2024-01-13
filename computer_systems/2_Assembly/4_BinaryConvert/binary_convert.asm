section .text
global binary_convert
binary_convert:
	xor eax, eax ; zero out eax
	xor ebx, ebx ; zero out ebx
	xor ecx ,ecx ; zero out ecx

.find_number_of_points:
	movzx edx, byte [rdi] ; read byte from RDI
	cmp edx, 0 ; Check if byte is zero 
	je .reset_rdi ; If byte is zero -> Exit routine 
	add ecx, 1 ; Increase ecx - counter for powers of 2
	add rdi, 1 ; Move pointer 1 byte forward
	jmp .find_number_of_points ; loop

.reset_rdi:
	sub rdi, rcx ; Subtract number of powers of 2
	sub ecx, 1 ; Subtract ecx by one to get correct power of 2 for each place


.loop:
	movzx edx, byte [rdi] ; Read byte from RDI
	cmp edx, 0 ; Check if byte is 0
	je .exit ; If zero  Exit
	cmp edx, '1' ;  If byte is 1
	sete bl ;  Set bl to 1
	shl ebx, cl ;  Shift ebx by powers of 2
	add eax, ebx ; Add result to result register
	sub cl, 1 ; Subtract powers of 2 by one
	add rdi, 1 ; Increment pointer by 1 byte
	jmp .loop ; Loop

.exit:
	ret
