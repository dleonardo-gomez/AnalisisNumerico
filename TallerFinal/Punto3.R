#install.packages("phaseR")
#install.packages("pracma")
#library(phaseR)
library(pracma)

f <- function(x, y) {x+y+1-x^2}

metodoEuler <- function(f, h, xi, yi, xf)
{
  N = (xf - xi) / h
  x = y = numeric(N+1)
  x[1] = xi; 
  y[1] = yi;
  i = 1
  while (i <= N)
  {
    x[i+1] = x[i]+h
    y[i+1] = y[i]+(h*f(x[i],y[i]))
    i = i+1
  }
  return (data.frame(X = x, Y = y))
}

e1 = metodoEuler(f, 0.1, 0, 1, 2)

e1[nrow(e1),]


plot(e1$X,e1$Y, type='l', lwd=2, col='red', 
      main="Euler",xlab="X", ylab="Y")
