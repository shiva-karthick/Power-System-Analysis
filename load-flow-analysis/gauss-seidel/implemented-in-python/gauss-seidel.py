# This formula is iterated many times until the required bus bar voltage
# stabilises.

# This program assumes you have calculated your Admittance matrix


class GaussSeidel(object):
    def __init__(self):
        self.admittanceValue = 0

    def getInput(self):
        print("Please enter the following parameters: \n")
        self.admittanceValue = input(
            "Enter the admittance value of corresponding to the respective bus bar voltage -> ")
