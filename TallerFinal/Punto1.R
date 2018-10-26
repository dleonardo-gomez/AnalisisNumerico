#install.packages("phaseR")
#install.packages("pracma")
#library(phaseR)
library(pracma)

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

f <- function(x, y) {(-5.6e-8*0.8*0.5*(x^4-200^4)) / 100}

e1 = metodoEuler(f, 10, 0, 180, 200)

e1[nrow(e1),]

plot(e1$X,e1$Y, type='l', lwd=2, col='red', 
     main="Temperatura",xlab="X", ylab="Y")

