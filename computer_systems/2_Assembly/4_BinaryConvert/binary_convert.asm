section .text
global binary_convert
binary_convert:
	xor eax, eax ; zero out eax
	xor ebx, ebx ; zeor out ebx
	xor ecx ,ecx ; zero out ecx

.find_number_of_points:
	movzx edx, byte [rdi] ; read byte from RDI
	cmp edx, 0
	je .reset_rdi
	add ecx, 1
	add rdi, 1
	jmp .find_number_of_points

.reset_rdi:
	sub rdi, rcx
	sub ecx, 1


.loop:
	movzx edx, byte [rdi] ; Read byte from RDI
	cmp edx, 0
	je .exit
	cmp edx, '1'
	sete bl
	shl ebx, cl
	add eax, ebx
	sub cl, 1
	add rdi, 1
	jmp .loop

.exit:
	ret
