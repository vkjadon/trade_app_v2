import plotly.graph_objects as go


class RSIChart:

    def create(self, df):

        fig = go.Figure()

        fig.add_trace(

            go.Scatter(

                x=df.index,

                y=df["RSI"],

                mode="lines",

                name="RSI",

            )

        )

        fig.add_hline(y=70)

        fig.add_hline(y=30)

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