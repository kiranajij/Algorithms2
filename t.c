# include <stdio.h>
# include <unistd.h>
# include <stdlib.h>
//# include <linux/sys.h>

void main(){
    int pid;
    pid = fork();
    if (pid == 0){
        exec("a.out");
    } else {
        while(1){
            printf("1");
        }
    }
}
