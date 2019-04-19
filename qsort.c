# include <stdio.h>
# include <stdlib.h>

int sortint(const void *a, const void *b){
    int *s = (int*) a, *t = (int*) b;
    if (*s > *t) return 1;
    if (*s < *t) return -1;
    return 0;
}

void main(){
    int a[] = {1, 4, 5, 7, 3, 0};
    qsort(a, 6, sizeof(int), &sortint);
    for (int i=0; i<6; i++){
        printf("%d\n", a[i]);
    }
}