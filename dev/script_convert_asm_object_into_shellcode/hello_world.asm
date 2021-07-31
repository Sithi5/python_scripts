global _start

section .text

_start:
    jmp MESSAGE      ; 1) lets jump to MESSAGE

GOBACK:
    mov rax, 0x4
    mov rbx, 0x1
    pop rcx          ; 3) we are poping into `ecx`, now we have the
                     ; address of "Hello, World!\r\n"
    mov rdx, 0xF
    int 0x80

    mov rax, 0x1
    mov rbx, 0x0
    int 0x80

MESSAGE:
    call GOBACK       ; 2) we are going back, since we used `call`, that means
                      ; the return address, which is in this case the address
                      ; of "Hello, World!\r\n", is pushed into the stack.
    db "Hello, World!", 0dh, 0ah
