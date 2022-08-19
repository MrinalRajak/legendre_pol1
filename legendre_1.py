
#Legendre polynomials

#(1) (n+1)*P(n+1,x) = (2*n+1)*x*P(n,x)-n*P(n-1,x)

import numpy as np
from scipy.special import legendre
x=float(input("Enter the x: "))
n=int(input("Enter the n: "))
LHS=(n+1)*(legendre(n+1)(x))
RHS=(2*n+1)*x*(legendre(n)(x))-n*(legendre(n-1)(x))
print("LHS: ",LHS)
print("RHS: ",RHS)
