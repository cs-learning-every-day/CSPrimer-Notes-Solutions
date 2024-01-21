section .text
global fib
fib:
	; base case:
	; if n <= 1: return n
	; general case:
	; return fib(n -1) + fib(n -2)

	mov eax, edi	; Base Case: if n <= 1 return n 
	cmp eax, 1		
	jle .end		

	sub edi, 1
	; NOTE -> you should use 64 bit registers for pop push
	push rdi		; push n - 1 to top of stack, as edi will be clobbered
	call fib		; fib(n - 1)
	pop rdi			; Return value into edi
	; we get result in eax

	push rax		; push f(n -1) to stack, as eax will be clobbered
	sub edi, 1
	call fib		; fib(n - 2)
	pop rcx			; Pop previously computed f(n - 1) from top of stoack and...
	add eax, ecx	; ... add it into newly computed f(n - 2)

.end:
	ret
