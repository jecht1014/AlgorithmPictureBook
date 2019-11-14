#include<stdio.h>

void ForwardAlgorithm(int n, int m,int t, double a[n][n], double pi[], double b[n][m], double *p, double **alfa);

#define n 2
#define m 2
#define t 2

int main() {

	//printf("n m t : ");
	//scanf("%d %d %d", &n, &m, &t);
	
	double a[n][n] = {{0.8, 0.2}, {0.6, 0.4}};
	double b[n][m] = {{0.1, 0.9}, {0.5, 0.5}};
	double pi[n] = {0.3, 0.7};
	char o[n][10] = {"o1", "o2"};
	
	double *alfa[n];
	double p;
	
	ForwardAlgorithm(n, m, t, a, pi, b, &p, alfa);
	
	/*
	int i, j;
	for(i = 0; i < n; i++){
		for(j = 0; j < n; j++){
			 printf("a[%d][%d] : ", i+1, j+1);
			 scanf("%f", &a[i][j]);
		}
	}
	for(i = 0; i < n; i++){
		for(j = 0; j < m; j++){
			 printf("b[%d][%d] : ", i+1, j+1);
			 scanf("%f", &b[i][j]);
		}
	}
	for(i = 0; i < n; i++){
		printf("pi[%d] : ", i+1);
		scanf("%f", &pi[i]);
	}
	for(i = 0; i < n; i++){
		printf("o[%d] : ", i+1);
		scanf("%f", &o[i]);
	}
	*/
	
	return 0;
}

void ForwardAlgorithm(int n, int m,int t, double a, double pi, double b, double *p, double **alfa){
	int i;
	for(i = 0; i < n; i++)
		alfa
}