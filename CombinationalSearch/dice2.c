#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXSIZE 30

int dice(int n, int s)
{
	int i, j, k;			/* counters */
	int a[MAXSIZE+1][MAXSIZE+1];

	memset(a, 0, sizeof(a));
	
	for (i=1; i<=MAXSIZE+1 && i <=6; i++)
	{
		/*
		* setting the first row of the array a
		* to 1
		*/
		a[1][i] = 1;
	}

	for (i=2; i<=n; i++)
	{
		for (j=1; j<=MAXSIZE+1; j++)
		{
			for (k=1; k<=6 && k<j; k++)
			{
				a[i][j] += a[i-1][j-k];
			}
		}
	}

	return a[n][s];
}

int main(int argc, char* argv[]){

	int n, s, w;
	n = 3;
	s = 15;
	w = dice(n, s);
	printf("%d\n", w);

}