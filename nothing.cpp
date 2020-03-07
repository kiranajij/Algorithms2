// # include <iostream>
# include <stdio.h>

struct Point{
    int x;      /* x co-ordinate */
    int y;      /* Y co-ordinate */
};

enum Edge {
    TREE_EDGE,
    BACK_EDGE,
    FORWARD_EDGE,
    CROSS_EDGE,
    PARENT_BACK_EDGE,
};

int print_point(void* vp){
    struct Point* p = (struct Point*) vp;
    int x = p->x, y = p->y;
    
    //std:: cout << x << y << std::endl;
    
    printf("(%d, %d)\n", x, y);
    
    return 0;
}

int main(void){
    struct Point p;
    p.x = 1;
    p.y = 2;   
    
    print_point(&p);
    return 0;
}
