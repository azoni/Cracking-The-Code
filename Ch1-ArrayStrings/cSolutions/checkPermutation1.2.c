#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define boolean int
#define trueOrFalse(x) ((x > 0) ? "yes" : "no")


char *putInAlpha(char theString[]){
    
    int i, j;
    int length = strlen(theString);
    for(i = 0; i < length; i++){
        if(theString[i] >= 65 && theString[i] <= 90){
            theString[i] = theString[i] + 32;
        }
    }
    //bubble sort
    for(i = 0; i < length; i++){
        j = i + 1;
        for(j = i; j < length; j++){
            if(theString[i] > theString[j]){
                char temp = theString[i];
                theString[i] = theString[j];
                theString[j] = temp;
            }
        }
    }
    return theString;
}

boolean isPerm(char * theFirst, char * theSecond){
    char *firstString = putInAlpha(theFirst);
    char *secondString = putInAlpha(theSecond);
    return !strcmp(firstString, secondString);
}

int main(int argc, char *argv[]){
   
    char string1[] = "ABcdEFgh";
    char string2[] = "fhgecdab";
    printf("Is %s and %s a permutation?\n", string1, string2);
    printf("Answer: %s\n", trueOrFalse(isPerm(string1, string2)));

}