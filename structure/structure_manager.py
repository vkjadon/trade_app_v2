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
        # ----------------------------------
        # Opening Range (09:15 - 09:30)
        # ----------------------------------

        orb = df.between_time("09:15", "09:30")

        orb_high = orb["High"].max()
        orb_low = orb["Low"].min()

        df["ORB_High"] = orb_high
        df["ORB_Low"] = orb_low
        
        return df