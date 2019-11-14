#include<stdio.h>
#include<stdlib.h>
#include<math.h>

void add_matrix(double **mat1, double **mat2, int row, int column, double **result);
void sub_matrix(double **mat1, double **mat2, int row, int column, double **result);
void mult_matrix(double **mat1, int row1, int column1, double **mat2, int row2, int column2, double **result);
void mult_matrix2(double **mat, int row, int column, double num, double **result);
void transpose_matrix(double **mat, int row, int column, double **result);
void cofactor_matrix(double **mat, int row, double **result);
void inverse_matrix(double **mat, int row, double **result);
double det(double **mat, int row);
void cholesky_decomposition(double **sigma, int row, double **under_result);

int simulation(double **sigma, int row, double **mu1, double **mu2, double c1, double c2, double w0, double **w);
int gen_class(double c1, double c2);
double ran0();
double box_muller();
void seekx(double **sigma, int row, double **mu, double **x);

int main(){
	//input
	double c1, c2;
	int n;
	puts("c1 c2");
	scanf("%lf %lf", &c1, &c2);

	int r;
	puts("r");
	scanf("%d", &r);

	double mu1[r][1], mu2[r][1], sigma[r][r];
	int i, k;
	for(i = 0; i < r; i++)
		printf("mu1[%d][0] ", i);
	printf("\n");
	for(i = 0; i < r; i++)
		scanf("%lf", &mu1[i][0]);

	for(i = 0; i < r; i++)
		printf("mu2[%d][0] ", i);
	printf("\n");
	for(i = 0; i < r; i++)
		scanf("%lf", &mu2[i][0]);

	for(i = 0; i < r; i++){
		for(k = 0; k < r; k++)
			printf("sigma[%d][%d] ", i, k);
		printf("\n");
	}
	for(i = 0; i < r; i++)
		for(k = 0; k < r; k++)
			scanf("%lf", &sigma[i][k]);
	
	printf("n\n");
	scanf("%d", &n);

	//計算開始
	double theta = log(c1/c2);
	double *mu1c[r];
	double *mu2c[r];
	double *resultc[r];
	double result1[r][1];
	for(i = 0; i < r; i++){
		mu1c[i] = mu1[i];
		mu2c[i] = mu2[i];
		resultc[i] = result1[i];
	}
	add_matrix(mu1c, mu2c, r, 1, resultc);
	
	double mu1t[1][r];
	double *mu1tc[1];
	mu1tc[0] = mu1t[0];
	transpose_matrix(resultc, r, 1, mu1tc);

	mult_matrix2(mu1tc, 1, r, 1/2.0, mu1tc);
	
	double result2[r][1];
	for(i = 0; i < r; i++)
		resultc[i] = result2[i];
	sub_matrix(mu1c, mu2c, r, 1, resultc);
	
	double *sigmac[r];
	double inverse_sigma[r][r];
	double *inverse_sigmac[r];
	for(i = 0; i < r; i++){
		sigmac[i] = sigma[i];
		inverse_sigmac[i] = inverse_sigma[i];
	}
	inverse_matrix(sigmac, r, inverse_sigmac);
		
	double w0[1][1];
	double *w0c[1];
	w0c[0] = w0[0];
	
	mult_matrix(mu1tc, 1, r, inverse_sigmac, r, r, mu1tc);
	mult_matrix(mu1tc, 1, r, resultc, r, 1, w0c);
	w0[0][0] += theta;
	
	double wt[r][1];
	double *wtc[r];
	for(i = 0; i < r; i++)
	  wtc[i] = wt[i];
	mult_matrix(inverse_sigmac, r, r, resultc, r, 1, wtc);
	printf("x2 = %fx1 + %f\n", -wt[0][0]/wt[0][1], -w0[0][0]/wt[0][1]);
	//シュミレーション開始
	int nr = 0;
	srand(time(NULL));
	for(i = 0; i < n; i++){
	  nr += simulation(sigmac, r, mu1c, mu2c, c1, c2, w0[0][0], wtc);
	}
	
	printf("識別率%f\n", (double)nr/n);
	return 0;
}

double ran0(){
  	return (double)rand()/((double)RAND_MAX);
}

double box_muller(){
  	double u0 = ran0();
  	double u1 = ran0();
  	double z0 = pow(-2 * log(u0), 0.5) * cos(2 * M_PI * u1);
  	double z1 = pow(-2 * log(u0), 0.5) * sin(2 * M_PI * u1);
  	return z0;
}

int gen_class(double c1, double c2){
	double ran = ran0();
	if(ran <= c1)
		return 0;
	else
	    return 1;
}

void seekx(double **sigma, int row, double **mu, double **x){
	int i, j;
	double z[row];
	double cholesky_sigma[row][row];
	double *cholesky_sigmac[row];
	for(i = 0; i < row; i++){
		z[i] = box_muller();
		cholesky_sigmac[i] = cholesky_sigma[i];
	}
	
	cholesky_decomposition(sigma, row, cholesky_sigmac);
	
	for(i = 0; i < row; i++){
		x[0][i] = mu[i][0];
		for(j = 0; j <= i; j++){
			x[0][i] += cholesky_sigma[i][j] * z[j];
		}
	}
}

int simulation(double **sigma, int row, double **mu1, double **mu2, double c1, double c2, double w0, double **wt){
  	int c = gen_class(c1, c2);
 	double x[1][row];
  	double *xc[1];
	xc[0] = x[0];
  	if(c == 0){
    	seekx(sigma, row, mu1, xc);
  	}
  	else{
  		seekx(sigma, row, mu2, xc);
  	}
  	
  	double gx[1][1];
  	double *gxc[1];
  	gxc[0] = gx[0];
  	mult_matrix(xc, 1, row, wt, row, 1, gxc);
  	gx[0][0] += w0;
  	
  	//printf("%d\t%d\t%f\t%f\n", c, ((c == 0 && gx[0][0] < 0) || (c == 1 && gx[0][0] < 0)), x[0][0], x[0][1]);
  	
  	return ((c == 0 && gx[0][0] >= 0) || (c == 1 && gx[0][0] < 0));
}

void add_matrix(double **mat1, double **mat2, int row, int column, double **result){
	int i, k;
	for(i = 0; i < row; i++)
		for(k = 0; k< column; k++)
			result[i][k] = mat1[i][k] + mat2[i][k];
}

void sub_matrix(double **mat1, double **mat2, int row, int column, double **result){
	int i, k;
	for(i = 0; i < row; i++)
		for(k = 0; k< column; k++)
			result[i][k] = mat1[i][k] - mat2[i][k];
}

void mult_matrix(double **mat1, int row1, int column1, double **mat2, int row2, int column2, double **result){
	int i, k;
	for(i = 0; i < row1; i++){
		for(k = 0; k < column2; k++){
			result[i][k] = 0;
			int j;
			for(j = 0; j < column1; j++){
				result[i][k] += mat1[i][j] * mat2[j][k];
			}
		}
	}
}

void mult_matrix2(double **mat, int row, int column, double num, double **result){
	int i, k;
	for(i = 0; i < row; i++)
		for(k = 0; k< column; k++)
			result[i][k] = num*mat[i][k];
}

//転置行列の計算
void transpose_matrix(double **mat, int row, int column, double **result){
	int i, k;
	for(i = 0; i < column; i++)
		for(k = 0; k < row; k++)
			result[i][k] = mat[k][i];
}

//余因子行列の計算
void cofactor_matrix(double **mat, int row, double **result){
	int i, k;
	for(i = 0; i < row; i++){
		for(k = 0; k < row; k++){
			double x[row-1][row-1];
			int j, l;
			for(j = 0; j < row; j++){
				for(l = 0; l < row; l++){
					int a = j;
					int b = l;
					if(j == i || l == k)
						continue;
					
					if(i < j)
						a--;
					if(k < l)
						b--;
					
					x[a][b] = mat[j][l];
				}
			}
			double *p[row-1];
			for(j = 0; j < row-1; j++)
				p[j] = x[j];
			result[i][k] = pow(-1, i+1+k+1) * det(p, row-1);
		}
	}
}

//逆行列の計算
void inverse_matrix(double **mat, int row, double **result){
	double det_mat = det(mat, row);
	cofactor_matrix(mat, row, result);
	mult_matrix2(result, row, row, 1/det_mat, result);
}

//行列式の計算
double det(double **mat, int row){
	double result = 0;
	int i, k, j;
	if(row == 1)
		return mat[0][0];
	else if(row == 2){
		printf("c");
		return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0];
	}
	else{
		double mat2[row-1][row-1];
		double *mat2c[row-1];
		for(i = 0; i < row; i++){
			for(k = 0; k < row; k++){
				for(j = 1; j < row; j++){
					if(i == k)
						continue;
					printf("a");
					if(i > k)
						mat2[k][j-1] = mat[k][j];
					else
						mat2[k-1][j-1] = mat[k][j];
					printf("a");
				}
			}
			for(k = 0; k < row-1; k++)
				mat2c[k] = mat2[k];
			printf("b");
			result += pow(-1, i) * mat[i][0] * det(mat2c, row-1);
			printf("b");
		}
		return result;
	}
}

// コレスキー分解の計算
void cholesky_decomposition(double **sigma, int row, double **under_result){
	int i, j;
	for(i = 0; i < row; i++){
		for(j = 0; j < row; j++){
			int k;
			if(i == j){
				under_result[j][i] = sigma[j][i];
				for(k = 0; k <= j-1; k++)
					under_result[j][i] -= pow(under_result[j][k], 2);
				under_result[j][i] = sqrt(under_result[j][i]);
			}
			else if(i < j){
				under_result[j][i] = sigma[j][i];
				for(k = 0; k <= i-1; k++)
					under_result[j][i] -= under_result[i][k]*under_result[j][k];
				under_result[j][i] /= under_result[i][i];
			}
			else{
				under_result[j][i] = 0;
			}
		}
	}
}