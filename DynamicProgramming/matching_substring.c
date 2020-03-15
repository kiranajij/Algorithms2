/*
Solution on the Dynamic Porgramming on Matching Substrings.
*/

# include <stdio.h>
# include <stdlib.h>
# include <string.h>

# define MAXLEN 20

# define MATCH 0    // For match
# define INSERT 1   // for insertsion
# define DELETE 2   // for deleting a character 


typedef struct _cell{
    int cost;       /* cost of reacing that cell */
    int parent;     /* operation on parent */
} cell;

cell m[MAXLEN+1][MAXLEN+1];     /* Array to store the dynamic
                              generated costs */

void row_init(int i){
    m[0][i].cost = i;
    if ( i > 0 ) m[0][i].parent = INSERT;
    else m[0][i].parent = -1;
}

void column_init(int i){
    m[i][0].cost = i;
    if (i > 0 ) m[i][0].parent = DELETE;
    else m[i][0].parent = -1;
}

int match(char c, char p){
    if (c == p ) return 0;
    return 1;
}

int indel(char c){
    return 1;
}

void goal_cell(char* text, char* patt, int* i, int* j){
    *j = strlen(patt) - 1;
    *i = strlen(text) - 1;
}

void do_insert(char *t, int j){
    printf("I");
}

void do_match(char *s, char* t, int i){
    if (s[i] == t[i]) printf("M");
    else printf("S");
}

void do_delete(char *s, int i){
    printf("D");
}

int string_compare(char *s, char *t){
    int i, j;       /* counters */
    int opt[3];

    for (i=0; i<MAXLEN; i++){
        row_init(i);
        column_init(i);
    }

    for (i=1; i<strlen(s); i++){
        for (j=1; j<strlen(t); j++){
            opt[MATCH] = m[i-1][j-1].cost + match(s[i], t[i]);
            opt[INSERT] = m[i][j-1].cost + indel(t[j]);
            opt[DELETE] = m[i-1][j].cost + indel(s[i]);

            m[i][j].cost = opt[MATCH];
            m[i][j].parent = MATCH;

            for (i=1; i<=2; i++){
                if (opt[i] < m[i][j].cost){
                    m[i][j].cost = opt[i];
                    m[i][j].parent = i;
                }
            }
        }

    }

    goal_cell(s, t, &j, &i);
    return (m[i][j].cost );
}

void main(){
    char *s, *p;

    printf("Enter the string\n");
    fgets(s, MAXLEN, stdin);

    printf("Enter Pattern\n");
    fgets(p, MAXLEN, stdin);

    int cost = string_compare(p, s);
    printf("Cost:\t%d\n", cost);

}