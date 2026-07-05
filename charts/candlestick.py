import plotly.graph_objects as go


class CandlestickChart:

    def create(self, df, trades=None):

        fig = go.Figure()

        # --------------------------------------------------
        # Candlestick
        # --------------------------------------------------

        fig.add_trace(

            go.Candlestick(

                x=df.index,

                open=df["Open"],

                high=df["High"],

                low=df["Low"],

                close=df["Close"],

                name="Price",

            )

        )

        # --------------------------------------------------
        # EMA20
        # --------------------------------------------------

        if "EMA20" in df.columns:

            fig.add_trace(

                go.Scatter(

                    x=df.index,

                    y=df["EMA20"],

                    mode="lines",

                    name="EMA20",

                    line=dict(

                        color="orange",

                        width=2,

                    ),

                )

            )

        # --------------------------------------------------
        # Previous Day High
        # --------------------------------------------------

        if "PDH" in df.columns:

            fig.add_trace(

                go.Scatter(

                    x=df.index,

                    y=df["PDH"],

                    mode="lines",

                    name="PD High",

                    line=dict(

                        color="green",

                        dash="dash",

                        width=1,

                    ),

                )

            )

        # --------------------------------------------------
        # Previous Day Low
        # --------------------------------------------------

        if "PDL" in df.columns:

            fig.add_trace(

                go.Scatter(

                    x=df.index,

                    y=df["PDL"],

                    mode="lines",

                    name="PD Low",

                    line=dict(

                        color="red",

                        dash="dash",

                        width=1,

                    ),

                )

            )

        # --------------------------------------------------
        # Opening Range High
        # --------------------------------------------------

        if "ORH" in df.columns:

            fig.add_trace(

                go.Scatter(

                    x=df.index,

                    y=df["ORH"],

                    mode="lines",

                    name="OR High",

                    line=dict(

                        color="blue",

                        dash="dot",

                        width=1,

                    ),

                )

            )

        # --------------------------------------------------
        # Opening Range Low
        # --------------------------------------------------

        if "ORL" in df.columns:

            fig.add_trace(

                go.Scatter(

                    x=df.index,

                    y=df["ORL"],

                    mode="lines",

                    name="OR Low",

                    line=dict(

                        color="purple",

                        dash="dot",

                        width=1,

                    ),

                )

            )

        # # --------------------------------------------------
        # # Swing High
        # # --------------------------------------------------

        # if "SwingHigh" in df.columns:

        #     swing_high = df[df["SwingHigh"]]

        #     if not swing_high.empty:

        #         fig.add_trace(

        #             go.Scatter(

        #                 x=swing_high.index,

        #                 y=swing_high["High"],

        #                 mode="markers",

        #                 name="Swing High",

        #                 marker=dict(

        #                     symbol="triangle-down",

        #                     size=10,

        #                     color="red",

        #                 ),

        #             )

        #         )

        # # --------------------------------------------------
        # # Swing Low
        # # --------------------------------------------------

        # if "SwingLow" in df.columns:

        #     swing_low = df[df["SwingLow"]]

        #     if not swing_low.empty:

        #         fig.add_trace(

        #             go.Scatter(

        #                 x=swing_low.index,

        #                 y=swing_low["Low"],

        #                 mode="markers",

        #                 name="Swing Low",

        #                 marker=dict(

        #                     symbol="triangle-up",

        #                     size=10,

        #                     color="green",

        #                 ),

        #             )

        #         )

        # --------------------------------------------------
        # Remove non-trading gaps
        # --------------------------------------------------

        fig.update_xaxes(

            rangebreaks=[

                dict(bounds=["sat", "mon"]),

                dict(

                    pattern="hour",

                    bounds=[15.5, 9.25],

                ),

            ]

        )

        # --------------------------------------------------
        # Layout
        # --------------------------------------------------

        fig.update_layout(

            title="Price",

            height=650,

            template="plotly_white",

            xaxis_title="",

            yaxis_title="Price",

            xaxis_rangeslider_visible=False,

            hovermode="x unified",

            legend=dict(

                orientation="h",

                yanchor="bottom",

                y=1.02,

                xanchor="left",

                x=0,

            ),

            margin=dict(

                l=20,

                r=20,

                t=40,

                b=20,

            ),

        )

        # --------------------------------------------------
        # Trades
        # --------------------------------------------------

        if trades is not None and not trades.empty:

            ce = trades[trades["Signal"] == "BUY CE"]

            if not ce.empty:
                fig.add_trace(
                    go.Scatter(
                        x=ce["Entry Time"],
                        y = df.loc[ce["Entry Time"], "Low"] - 15,
                        mode="markers",
                        name="BUY CE",
                        marker=dict(
                            symbol="triangle-up",
                            color="green",
                            size=12,
                        ),
                    )
                )

            pe = trades[trades["Signal"] == "BUY PE"]

            if not pe.empty:
                fig.add_trace(
                    go.Scatter(
                        x=pe["Entry Time"],
                        y = df.loc[pe["Entry Time"], "High"] + 15,
                        mode="markers",
                        name="BUY PE",
                        marker=dict(
                            symbol="triangle-down",
                            color="red",
                            size=12,
                        ),
                    )
                )
                
                # --------------------------------------------------
                # Summary
                # --------------------------------------------------

                ce_signals = (df["Signal"] == "BUY CE").sum()
                pe_signals = (df["Signal"] == "BUY PE").sum()

                signal_count = ce_signals + pe_signals
                trade_count = len(trades) if trades is not None else 0

                fig.add_annotation(
                    xref="paper",
                    yref="paper",
                    x=0.99,
                    y=0.99,
                    showarrow=False,
                    align="right",
                    bgcolor="white",
                    bordercolor="black",
                    borderwidth=1,
                    font=dict(size=12),
                    text=(
                        f"<b>Signals:</b> {signal_count}<br>"
                        f"<b>Trades:</b> {trade_count}"
                    ),
                )
        return fig