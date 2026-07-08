import pandas as pd


class TrendStructure:

    def calculate(self, df):

        df = df.copy()

        df["HH"] = False
        df["HL"] = False
        df["LH"] = False
        df["LL"] = False

        previous_high = None
        previous_low = None

        for i in range(len(df)):

            # ----------------------------
            # Swing High
            # ----------------------------

            if df.iloc[i]["SwingHigh"]:

                current = df.iloc[i]["High"]

                if previous_high is not None:

                    if current > previous_high:

                        df.iat[
                            i,
                            df.columns.get_loc("HH")
                        ] = True

                    else:

                        df.iat[
                            i,
                            df.columns.get_loc("LH")
                        ] = True

                previous_high = current

            # ----------------------------
            # Swing Low
            # ----------------------------

            if df.iloc[i]["SwingLow"]:

                current = df.iloc[i]["Low"]

                if previous_low is not None:

                    if current > previous_low:

                        df.iat[
                            i,
                            df.columns.get_loc("HL")
                        ] = True

                    else:

                        df.iat[
                            i,
                            df.columns.get_loc("LL")
                        ] = True

                previous_low = current

        return df