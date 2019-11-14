n <- 2  #s‚Ì”
m <- 2  #o‚Ì”
t <- 4  #ŽžŠÔ

#lambda
pi <- c(1, 0)
a <- rbind(c(0.2, 0.8), c(0.8, 0.2))
b <- rbind(c(0.8, 0.2), c(0.2, 0.8))

o <- c(1, 2, 2, 1)

beta <- matrix(0, nrow = t, ncol = n)
beta[t,] <- 1
c <- numeric(t)
c[t] <- 1 / rowSums(beta)[t]
beta[t,] <- beta[t,] * c[t]

for(i in (t-1):1) {
  for(j in 1:n) {
    beta[i,j] <- sum(a[j,] * b[, o[i+1]] * beta[i+1,])
    c[i] <- 1 / rowSums(beta)[i]
    beta[i,] <- beta[i,] * c[i]
  }
}
logp <- -sum(log(c))