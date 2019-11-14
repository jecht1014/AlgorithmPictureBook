#input:パターンa,一次元パターンの要素の集合V
#output:整数に変換し1文字ずつ区切ったパターンa
patternI <- function(a, V) {
  a <- strsplit(a, split = character(0))[[1]]
  for(i in 1:length(a)){
    for(j in 1:length(V)){
      if(a[i] == V[j]){
        a[i] <- j
        print(a[i])
      }
    }
  }
  a <- as.integer(a)
  return(a)
}

#input
I <- 18
J <- 26
A <- "GDVEKGKKIFIMKCSQCH"
B <- "ASFNEAPPGNPKAGEKIFKTKCAQCH"
V <- "ACDEFGHIKLMNPQRSTVWY"
V <- strsplit(V, split = character(0))[[1]]
A <- patternI(A, V)
B <- patternI(B, V)

#初期値設定
g <- matrix(-1, nrow = I+1, ncol = J+1)
g[1, 1] <- 0
