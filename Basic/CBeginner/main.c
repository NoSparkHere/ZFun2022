#include <stdio.h>
#include <string.h>

unsigned char flag[]={90,70,117,110,123,89,111,117,95,107,110,111,119,95,116,111,95,99,111,109,112,105,108,101,95,99,33,33,125,0};

int main()
{   
    int i;

    for(i = 0; i < strlen(flag); i++)
        printf("%c", flag[i]);
    return 0;
}

