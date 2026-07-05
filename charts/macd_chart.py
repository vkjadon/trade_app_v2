import plotly.graph_objects as go


class MACDChart:

    def create(self, df):

        fig = go.Figure()

        fig.add_trace(

            go.Scatter(

                x=df.index,

                y=df["MACD_12_26_9"],

                name="MACD",

            )

        )

        fig.add_trace(

            go.Scatter(

                x=df.index,

                y=df["MACDs_12_26_9"],

                name="Signal",

            )

        )

        fig.update_layout(

            height=220,

            template="plotly_white",

            margin=dict(
                l=20,
                r=20,
                t=20,
                b=20,
            ),

        )

        return fig