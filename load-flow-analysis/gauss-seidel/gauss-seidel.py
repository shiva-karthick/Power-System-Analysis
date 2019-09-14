# This formula is iterated many times until the required bus bar voltage
# stabilises.

# This program assumes you have calculated your Admittance matrix

import math
import cmath  # for complex numbers
import numpy
import sympy


class GaussSeidel():
    def __init__(self, n, i, Y_ii, phi_ii, P_i, Q_i, V_i, delta_i):
        self.n = n  # (n) is the total number of busbars
        self.i = i  # (i) is the bus bar we are interested to find
        self.Y_ii = Y_ii
        self.phi_ii = phi_ii
        self.P_i = P_i
        self.Q_i = Q_i
        self.V_i = V_i
        self.delta_i = delta_i
        self.k = 1  # (k) is default to 1
        # (r) = iterations; the number of iterations starting from 0
        self.r = 0

    def step1(self):
        step1_result_r = 1.0 / self.Y_ii
        step1_result_phase_angle = 0 - self.phi_ii
        # print("r is {} and angle is {}".format(step1_result_r, step1_result_phase_angle))
        return cmath.rect(step1_result_r, step1_result_phase_angle)

    def step2(self):
        numerator = cmath.polar(complex(self.P_i, -self.Q_i))
        numerator_r = numerator[0]
        numerator_angle_theta = math.degrees(numerator[1])
        step2_result_r = numerator_r / 1.0
        step2_result_angle_theta = numerator_angle_theta - 0
        # print(cmath.rect(step2_result_r, step2_result_angle_theta))

        return cmath.rect(step2_result_r, step2_result_angle_theta)

    def step3(self):
        if self.k == self.i:
            self.k += 1
            if (self.k == self.n):
                print("Y{}{} * V{}".format(self.i, self.k, self.k))
            else:
                for _ in range((self.n - self.k) + 1):

                    if (self.k != self.i):
                        # print("Y{}{} * V{} \t".format(self.i, self.k, self.k))
                        summation_string = ""
                        summation_string = ("(Y" +
                                            str(self.i) + str(self.k) +
                                            " * " + "V" + str(self.k) + ")")
                        print(summation_string, end=" ")

                        if (self.k < self.n):
                            self.k += 1
                    else:
                        if (self.k < self.n):
                            self.k += 1
                        continue
        else:
            if (self.k == self.n):
                print("Y{}{} * V{}".format(self.i, self.k, self.k))
            else:
                for _ in range((self.n - self.k) + 1):

                    if (self.k != self.i):
                        # print("Y{}{} * V{} \t".format(self.i, self.k, self.k))
                        summation_string = ""
                        summation_string = ("(Y" +
                                            str(self.i) + str(self.k) +
                                            " * " + "V" + str(self.k) + ")")
                        print(summation_string, end=" ")

                        if (self.k < self.n):
                            self.k += 1
                    else:
                        if (self.k < self.n):
                            self.k += 1
                        continue

    def step4(self, *args):
        matrices_list = [(x, y) for x, y in args]
        # print("matrices_list is " + str(matrices_list))
        total_r = 1
        total_angle_theta = 0
        for a in range(len(matrices_list)):
            total_r *= matrices_list[a][0]
            # print(total_r)
            total_angle_theta += matrices_list[a][1]
            # print(total_angle_theta)
        # print(cmath.rect(total_r, total_angle_theta))

        half_final_result = GaussSeidel.step2(
            self) - cmath.rect(total_r, total_angle_theta)
        print(cmath.polar(half_final_result * GaussSeidel.step1(self)))
        # cmath.polar(half_final_result * GaussSeidel.step1(self))


gaussSeidel = GaussSeidel(2, 1, 31.55, -46.28, -2.4, -1.8, 1.0, 0)
# gaussSeidel.step1()
# gaussSeidel.step2()
# gaussSeidel.step3()
gaussSeidel.step4(cmath.polar(-21.81 + 22.80j), cmath.polar(1))
