# Newton Raphson method is used to solve non-linear algebraic equations in power analysis systems
It works faster and it converges in most cases as compared to the Gauss-Seidel method.

The subscript (calc) refers to a calculated value as opposed to a specified value. Therefore,  
![alt text](https://github.com/shankar-shiv/Power-System-Analysis/blob/master/load%20flow%20analysis/newton%20raphson/images/PI(calc)QI(calc).PNG "Pi[calc] Qi[calc]")

The following mismatch terms are defined:
![alt text](https://github.com/shankar-shiv/Power-System-Analysis/blob/master/load%20flow%20analysis/newton%20raphson/images/mismatch_terms.PNG "Mismatch terms")

Now we introduce the Jacobian matrix which is a square matrix of the partial derivatives of Pi and Qi. 
The Jacobian matrix elements for a two-bus system are:
![alt text](https://github.com/shankar-shiv/Power-System-Analysis/blob/master/load%20flow%20analysis/newton%20raphson/images/jacobian_matrix.PNG "Jacobian Matrix")

The Newton Raphson general equations for the load flow problem are:
![alt text](https://github.com/shankar-shiv/Power-System-Analysis/blob/master/load%20flow%20analysis/newton%20raphson/images/newton-raphon.PNG "Newton-Raphson")
