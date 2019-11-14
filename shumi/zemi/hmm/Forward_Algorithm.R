n <- 2  #s‚Ì”
m <- 2  #o‚Ì”
t <- 4  #ŽžŠÔ

#lambda
pi <- c(1, 0)
a <- rbind(c(0.2, 0.8), c(0.8, 0.2))
b <- rbind(c(0.8, 0.2), c(0.2, 0.8))

o <- c(1, 2, 2, 1)

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
logp <- -sum(log(c))