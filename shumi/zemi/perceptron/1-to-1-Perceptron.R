#重さを初期化
def_wei <- function(input_n, output_n) {
  return (matrix(runif(output_n * (input_n+1), min = -2, max = 2), nrow = output_n, ncol = input_n+1))
}

#シグモイド関数
sigmoid <- function(x) {
  return(1 / (1+exp(-x)))
}

#素子を出力
output_element <- function(x, w) {
  fxw <- sigmoid(x %*% t(w))
  fxw <- cbind(c(1),fxw)
  return(fxw)
}

#修正誤差delta2を出力
modify_error2 <- function(h, d, ax) {
  a <- ax
  if(ncol(h) > 1) {
    for (i in 1:(ncol(h)-1)) {
      a <- cbind(a, ax)
    }
  }
  del <- a*(h-d)*h*(1-h)
  return(del)
}

#修正誤差delta1を出力
modify_error <- function(delta2, v, fwx) {
  del <- (delta2 %*% v) * fwx * (1-fwx)
}

delta_max <- function(delta, x) {
  delta_max <- max(abs(t(x) %*% delta))
  return(delta_max)
}

new_error <- function(x, a, w, v, d) {
  f <- output_element(x, w)
  h <- output_element(f, v)
  h <- matrix(h[,-1], nrow = nrow(h), ncol = ncol(g)-1)
  #print(h)
  e <- (1 / (2 * nrow(x))) * colSums(a * rowSums((h - d) * (h - d)))
  return(e)
}

#目標関数の重みを設定
objective_f <- function(n ,m) {
  w <- matrix(0, nrow = 1, ncol = n+1)
  for(i in 1:m) {
    w <- rbind(w, runif(n+1))
  }
  return(matrix(w[-1,], nrow = m, ncol = n+1))
}

#学習パターンの生成
learning_patterns <- function(n) {
  x <- matrix(0, nrow = 1, ncol = 1)
  for(i in 1:n) {
    x <- rbind(x, i / (n+1) + runif(1, min = 0, max = 1 / (n+1.5)))
  }
  return(x[-1,])
}

m <- 5
N <- 10
bigdelta <- 0.01
epsilon <- 0.01

dp <- objective_f(1, m)
dq <- objective_f(m, 1)
w <- def_wei(1, m)
v <- def_wei(m, 1)
X <- learning_patterns(N)
X <- cbind(matrix(1, nrow = N, ncol = 1), X)
dx <- output_element(output_element(X, dp), dq)[,-1]
dx
ax <- matrix(1, nrow = nrow(X), ncol = 1)

count <- 0
repeat {
  fwx <- output_element(X, w)
  hkx <- output_element(fwx, v)
  delta2 <- modify_error2(matrix(hkx[,-1]), dx, ax)
  delta1 <- modify_error(delta2, v[,-1], fwx[,-1])
  
  #重みの最大量を求める
  dmax <- 0
  vjk <- t(fwx) %*% delta2
  if(max(abs(vjk)) > dmax) {
    dmax <- max(abs(vjk))
  }
  wij <- t(X) %*% delta1
  if(max(abs(wij)) > dmax) {
    dmax <- max(abs(wij))
  }
  
  delta <- bigdelta / dmax
  
  #重みの修正
  v <- v - delta * t(vjk)
  w <- w - delta * t(wij)
  
  E <- new_error(X, ax, w, v, dx)
  count <- count + 1
  print(E)
  if(E < epsilon) break
}
count
dx
X

dp
dq
x <- matrix(seq(from = 0, to = 1, 0.1))
x2 <- cbind(1, x)
y <- output_element(output_element(x2, dp), dq)
y <- matrix(y[,-1], nrow = nrow(y), ncol = ncol(y)-1)
plot(x = x2[,-1], y = y[,1], type = "l", xlab = "", ylab = "",ann = F, xlim = c(0, 1), ylim = c(-1,1))
par(new = T)
y2 <- output_element(output_element(x2, w), v)
y2 <- matrix(y2[,-1], nrow = nrow(y2), ncol = ncol(y2)-1)
plot(x = x2[,-1], y = y2[,1], type = "l", xlim = c(0, 1), ylim = c(-1,1))