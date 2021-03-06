"""Division Class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """ calculation division class"""
    def get_result(self):
        """get the division results"""
        quotient_of_values = 1
        for value in self.values:
            try:
                quotient_of_values  /= value
            except Exception as error_e:
                raise ZeroDivisionError from error_e
        return quotient_of_values
