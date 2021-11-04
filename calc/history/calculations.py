"""Calculation history Class"""
class Calculations:
    """Create calculations for the calculator"""
    history = []
    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """clears the history of the calculator"""
        Calculations.history.clear()
        return True
    @staticmethod
    def get_last_calculation():
        """gives the last calculation in the history"""
        return Calculations.history[-1]
