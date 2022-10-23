#include <stdio.h>

int main(void){
FILE *fp;
int min_pin = 1340078;
int max_pin = 1349978;
char *filename = "pinCracker.txt";
fp = fopen(filename, "w+");
for(min_pin = 1340078; min_pin < max_pin; min_pin++){
fprintf(fp, "%d\n", min_pin);
}
printf("DONE!!!\nPin Generated Successfully\nRock on Boss!\n");
fclose(fp);
return 0;
}
