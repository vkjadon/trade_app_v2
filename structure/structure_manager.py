from structure.previous_day import PreviousDay
from structure.opening_range import OpeningRange
from structure.swing import Swing
from structure.trend_structure import TrendStructure

class StructureManager:

    def __init__(self):

        self.calculators = [

            PreviousDay(),

            OpeningRange(),

            Swing(),

            TrendStructure(),
    
        ]

    def calculate(self, df):

        for calculator in self.calculators:

            df = calculator.calculate(df)

        return df