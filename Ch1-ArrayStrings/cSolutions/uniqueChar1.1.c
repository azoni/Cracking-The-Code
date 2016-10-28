#include <stdio.h>
#include <stdlib.h>

#define boolean int
#define false 0
#define true 1

// Function for the array Solving
boolean arraySolution(char *theString){
    int ascii[256] = {0};
    while(*theString != '\0'){
        if(ascii[*theString] == 1){
            return false;
        } else {
            ascii[*theString] = 1;
        }
        theString++;
    }
    return true;
}

int main(int argc, char *argv[]){

    char *stringInput;
    if(argc > 1){
        stringInput = argv[1];
    } else {
        stringInput = "abcdefghijklmnopqrstuvwxyz";
    }

    printf("The string is: %s", (arraySolution(stringInput) ? "unique" : "not-unique"));


}