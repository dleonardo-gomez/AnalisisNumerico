#install.packages("phaseR")
#install.packages("pracma")
#library(phaseR)
library(pracma)

# funcion, h, y(xi) = yi, x final
metodoEulerMod <- function(f, h, xi, yi, xf)
{
  N = (xf - xi) / h
  x = y = numeric(N+1)
  x[1] = xi; 
  y[1] = yi;
  i = 1
  while (i <= N)
  {
    x[i+1] = x[i]+h
    y[i+1] = y[i]+(h/2*(f(x[i],y[i])+f(x[i+1],y[i+1])))
    i = i+1
  }
  return (data.frame(X = x, Y = y))
}

f <- function(x, y) {x+y+1-x^2}

e2 = metodoEulerMod(f, 0.1 , 0, 1, 1)

e2[nrow(e2),]

plot(e1$X,e1$Y, type='l', lwd=2, col='red', 
     xlab="X", ylab="Y")

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

e1 = metodoEuler(f, 0.1, 0, 1, 1)

e1[nrow(e1),]


lines(e2$X,e2$Y, type='l', lwd=2, col='black', 
      main="Euler",xlab="X", ylab="Y")




legend(0,4.3, # places a legend at the appropriate place 
       c('Modificado','Euler'), # puts text in the legend
       lty=c(1,1), # gives the legend appropriate symbols (lines)
       lwd=c(2.5,2.5),col=c('black','red'))
