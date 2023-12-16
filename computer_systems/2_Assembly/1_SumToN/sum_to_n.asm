            global      sum_to_n
            section     .text

sum_to_n:
            mov eax, edi
            add edi, 1
            imul eax, edi
            shr eax, 1
            ret
