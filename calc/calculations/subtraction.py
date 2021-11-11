"""Subtraction Class"""
import pprint

from calc.calculations.calculation import Calculation

class Subtraction(Calculation):
    """subtraction calculation object"""
    def get_result(self):
        """get the subtraction results"""
        return 0 - sum(self.values)
