#重さを初期化
def_wei <- function(input_n, output_n) {
  return (matrix(1, nrow = output_n, ncol = input_n+1))
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
  return(a*(h-d)*h*(1-h))
}

#修正誤差delta1を求める
modify_error <- function(delta2, v, fwx) {
  return((delta2 %*% v) * fwx * (1-fwx))
}

#誤差を求める
new_error <- function(x, a, w, v, d) {
  f <- output_element(x, w)
  h <- output_element(f, v)
  h <- h[,-1]
  e <- 1 / (2 * nrow(x)) * colSums(a * rowSums((h - d) ^ 2))
  return(e)
}

n <- 2
m <- 2
l <- 2
d <- rbind(c(0.5, 0.5), c(0.1, 0.6))
X <- rbind(c(0.2, 0.7), c(0.3, 0.6))
bigdelta <- 0.1
epsilon <- 0.1
X <- cbind(matrix(1, nrow = nrow(X), ncol = 1), X)

#w <- def_wei(n, m)
#v <- def_wei(m, l)
w <- rbind(c(1, 0, 0), c(0, 1, 0))
v <- rbind(c(1, 0, 0), c(0, 1, 0))
ax <- matrix(1, nrow = nrow(X), ncol = 1)

count <- 0
repeat {
  fwx <- output_element(X, w)
  hkx <- output_element(fwx, v)
  delta2 <- modify_error2(hkx[,2:(l+1)], d, ax)
  delta1 <- modify_error(delta2, v[,-1], fwx[,-1])

  #重みの最大量を求める
  max <- 0
  vjk <- t(fwx) %*% delta2
  if(max(abs(vjk)) > max) {
    max <- max(abs(vjk))
  }
  wij <- t(X) %*% delta1
  if(max(abs(wij)) > max) {
    max <- max(abs(wij))
  }

  delta <- bigdelta / max

  #重みの修正
  v <- v - delta * t(vjk)
  w <- w - delta * t(wij)

  E <- new_error(X, ax, w, v, d)
  count <- count + 1
  print(E)
  if(E < epsilon) break
}

count