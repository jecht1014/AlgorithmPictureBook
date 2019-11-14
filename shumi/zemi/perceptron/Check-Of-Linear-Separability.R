hikaku <- function(x) {
  e0 <- matrix(0, nrow = nrow(x), ncol = 1)
  if(length(which(e0 == x)) == nrow(x)) {
    return (0)
  } else if (length(which(x <= e0)) == nrow(x)) {
    return (-1)
  } else {
    return (1)
  }
}

n <- 3
X0 <- rbind(c(0, 1, 1), c(0, 1, 0), c(1, 1, 0))
X1 <- rbind(c(1, 1, 1), c(1, 0, 0), c(0, 0, 1))

X0 <- cbind(1, X0)
X1 <- cbind(1, X1)
A <- rbind(-X0, X1)
A2 <- solve(t(A) %*% A) %*% t(A)
b <- matrix(1:ncol(A2))
w <- A2 %*% b
e <- A %*% w - b
delta <- 0.1

repeat {
  judge <- hikaku(e)
  if(judge == -1 | judge == 0) {
    break
  }
  b <- b + delta * (e + abs(e))
  w <- w + delta * A2 %*% (e + abs(e))
  e <- A %*% w - b
}

if(judge == -1) {
  printf("üŒ`•ª—£•s‰Â")
} else {
  w
}