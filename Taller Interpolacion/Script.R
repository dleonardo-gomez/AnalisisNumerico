require(PolynomF)
x = c(100,200,300,400,500,600) # n+1 = 11
y = c(-160,-35,-4.2,9,16.9,21.3)
# Polinomio de ajuste (polinomio interpolante en este caso)
datx = x[1:5]; daty = y[1:5]
polyAjuste = poly.calc(datx,daty)
polyAjuste = polyAjuste
print(round(polyAjuste,digits=3))
print(round(polyAjuste(450),digits=3))
#-0.1 + 4.433333*x - 15*x^2 + 16.66667*x^3 + 4.4833e-11*x**5
plot(x,y, pch=19, cex=1, col = "red", asp=1) # Representación con puntos
curve(polyAjuste,add=T)

