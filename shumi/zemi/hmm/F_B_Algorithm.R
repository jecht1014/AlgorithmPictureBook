#input
#n:状態集合の要素数
#m:出力記号集合の要素数
#t:出力記号列の数
#pi:初期分布
#a:推移確率
#b:出力確率
#o:出力記号列
#output
#logp:log(p(lambda))
#alfa:途中経過
#c:スケーリング係数
Forward_Algorithm <- function(n, m, t, pi, a, b, o) {
  alfa <- matrix(0, nrow = t, ncol = n)
  alfa[1,] <- pi * b[, o[1]]
  c <- numeric(t)
  c[1] <- 1 / rowSums(alfa)[1]
  alfa[1,] <- alfa[1,] * c[1]
  
  for(i in 1:(t-1)) {
    for(j in 1:n) {
      alfa[i+1,j] <- alfa[i,] %*% a[,j] * b[j,o[i+1]]
    }
    c[i+1] <- 1 / rowSums(alfa)[i+1]
    alfa[i+1,] <- alfa[i+1,] * c[i+1]
  }
  logp <- list(-sum(log(c)), alfa, c)
  return(logp)
}

#input
#n:状態集合の要素数
#m:出力記号集合の要素数
#t:出力記号列の数
#pi:初期分布
#a:推移確率
#b:出力確率
#o:出力記号列
#c:前向きアルゴリズムで求めたスケーリング係数
#output
#beta:途中経過
Backward_Algorithm <- function(n, m, t, pi, a, b, o, c) {
  beta <- matrix(0, nrow = t, ncol = n)
  beta[t,] <- 1
  beta[t,] <- beta[t,] * c[t]
  
  for(i in (t-1):1) {
    for(j in 1:n) {
      beta[i,j] <- sum(a[j,] * b[, o[i+1]] * beta[i+1,])
    }
    beta[i,] <- beta[i,] * c[i]
  }
  return(beta)
} 

n <- 2
m <- 2
t <- 4

#lambda
pi <- c(1, 0)
a <- rbind(c(0.2, 0.8), c(0.8, 0.2))
b <- rbind(c(0.8, 0.2), c(0.2, 0.8))

o <- c(1, 2, 2, 1)

result <- Forward_Algorithm(n, m, t, pi, a, b, o)
logp <- result[[1]]
alfa <- result[[2]]
c <- result[[3]]

beta <- Backward_Algorithm(n, m, t, pi, a, b, o, c)