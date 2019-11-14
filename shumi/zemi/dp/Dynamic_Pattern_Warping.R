library("ramify")

#input:パターンの長さn,一次元パターンの構成要素V
#output:ランダムな整数1:length(V)で表されるパターンa
#一次元パターンの構成要素Vの要素数を用いて整数1からlength(V)までの整数を
#乱数でn+1個生成し新たなパターンを返す関数
ranP <- function(n, V) {
  x <- 1/length(V)
  a <- runif(n+1)
  for(i in 1:length(V)) {
    for(j in 1:(n+1)) {
      if(a[j] < x){
        a[j] <- i
      }
    }
    x <- x+1/length(V)
  }

#  for(i in 1:(n+1)) {
#    a[i] <- V[a[i]]
#  }
  return(a)
}

#input:整数に変更したパターンa, 一次元パターンの要素の集合V
#output:一次元パターンの要素で作られたパターンb
#ranPで作られた整数の一次元パターンをVの一次元パターンに変換し返す関数
pback <- function(a, V) {
  for(i in 1:length(a))
    a[i] <- V[a[i]]
  return(a)
}

#input
I <- 10 #パターンAの長さ
J <- 10 #パターンBの長さ
V <- c(0,1) #一次元パターンの要素の集合
alpha <- rbind(c(0,1),c(1,0)) #Vの類似度
A <- ranP(I, V)
B <- ranP(J, V)

#begin
#初期値設定
g <- matrix(-1, nrow = I+1, ncol = J+1) #gの初期化
g[1,1] <- alpha[A[1],B[1]]
for(j in 2:(J+1))
  g[1,j] <- 10000

#最適伸縮関数wの情報
h <- matrix(-1, nrow = I+1, ncol = J+1)

#D(A,B)の計算
for(i in 2:(I+1)) {
  for(j in 1:(J+1)) {
    #最小値探索範囲の場合分け
    if(j == 1) {
      g[i, j] <- alpha[A[i], B[j]] + g[i-1, j]
      h[i, j] <- j
    } else if(j == 2) {
      g[i, j] <- alpha[A[i], B[j]] + min(g[i-1, c(j-1, j)])
      h[i, j] <- argmin(rbind(g[i-1, c(j-1, j)]), rows = TRUE) + j - 2
    } else {
      g[i, j] <- alpha[A[i], B[j]] + min(g[i-1, c(j-2, j-1, j)])
      h[i, j] <- argmin(rbind(g[i-1, c(j-2, j-1, j)]), rows = TRUE) + j - 3
    }
  }
}
D <- g[I+1, J+1]

#最適伸縮関数の決定
w <- numeric(I+1)
w[I+1] <- J+1
for(i in (I+1):2)
  w[i-1] <- h[i, w[i]]
w <- w-1

A <- pback(A, V)
B <- pback(B, V)

A
B
w
