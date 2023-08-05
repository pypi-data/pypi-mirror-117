%macro print_macro 1
            mov         r13, utsname + %1
            mov         r14, 24
            call        print
            mov         r13, NEW_LINE
            mov         r14, 1
            call        print
%endmacro
            section     .data
SYS_UNAME:  equ         63
SYS_WRITE:  equ         1
STD_IN:     equ         1
INV_MSG:    db          "Invalid option"
NEW_LINE:   db          10

struc UTSNAME
    sysname:    resb 64
    nodename:   resb 64
    release:    resb 64
    version:    resb 64
    machine:    resb 64   
endstruc

utsname:    istruc      UTSNAME
    at sysname, db ""
    at nodename, db ""
    at release, db ""
    at version, db ""
    at machine, db ""
iend

            global      print_info
            section     .text

print_info:
            mov         r15, rdi
            call        uname

            cmp         r15, 0
            je          _issysname
            cmp         r15, 1
            je          _isnodename
            cmp         r15, 2
            je          _isrelease
            cmp         r15, 3
            je          _isversion
            cmp         r15, 4
            je          _ismachine
            jmp         _isinvalid

_issysname:
            print_macro sysname
            ret

_isnodename:
            print_macro nodename
            ret

_isrelease:
            print_macro release
            ret

_isversion:
            print_macro version
            ret

_ismachine:
            print_macro machine
            ret

_isinvalid:
            mov         r13, INV_MSG
            mov         r14, 24
            call        print
            ret

uname:
            mov         rax, SYS_UNAME
            mov         rdi, utsname
            syscall
            ret

print:
            mov         rax, SYS_WRITE
            mov         rdi, STD_IN
            mov         rsi, r13
            mov         rdx, r14
            syscall
            ret