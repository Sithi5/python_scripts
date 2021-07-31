#include <stdio.h>
#include <string.h>
unsigned char shellcode[] = "\xb8\x0a\x00\x00\x00\xc3";
int main(int argc, char **argv)
{
    void (*fp)(void);
    fp = (void *)shellcode;
    fp();
}