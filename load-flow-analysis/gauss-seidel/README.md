# Gauss Seidel method

is used to calculate the Voltage and Angle of the required bus bar.

## How does a Gauss Seidel method ?

Here is how it works:
1\. Start with an initial value of the voltage V(i).
2\. For each bus bar i, calculate new voltages using the below formula.
3\. Repeat step 2 with the voltages calculated until the voltages stabilize.

It is necessary to select one bus, called the slack bus or swing bus to provide the additional real and reactive power to supply the transmission losses, since these are unknown until the final solution is obtained. At this bus, the voltage magnitude and phase angle are specified as V = 1.0 and delta = 0 degrees.

## The mathematics behind Gauss Seidel method

**i** = Individual bus bar number
**n** = Total number of bus bars
**r** = Iteration number (starts from 0)

![alt text](https://github.com/shankar-shiv/Power-System-Analysis/blob/master/load%20flow%20analysis/gauss%20seidel/gauss-seidel.PNG "Gauss-Seidel equation")

## An Example
