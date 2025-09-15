#include <stdio.h>

int main() {
    int smallInteger = 42; // declaring a small integer
    printf("Value: %d\n", smallInteger);
    return 0;
}

// Example of memory
//
// +----------+----------+----------+----------+
// | byte 1   | byte 2   | byte 3   | byte 4   |
// +----------+----------+----------+----------+
// | 00000000 | 00000000 | 00000000 | 00101010 |
// +----------+----------+----------+----------+