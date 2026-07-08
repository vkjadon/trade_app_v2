from dataclasses import dataclass


@dataclass
class Trade:

    # ----------------------------
    # Direction
    # ----------------------------

    direction: str

    # ----------------------------
    # Entry
    # ----------------------------

    entry_time: object

    entry_price: float

    # ----------------------------
    # Exit
    # ----------------------------

    exit_time: object = None

    exit_price: float = 0.0

    # ----------------------------
    # Performance
    # ----------------------------

    points: float = 0.0

    # ----------------------------
    # Strategy
    # ----------------------------

    confidence: str = ""

    reason: str = ""

    # ----------------------------
    # Future Fields
    # ----------------------------

    score: int = 0

    quantity: int = 1

    pnl: float = 0.0

    brokerage: float = 0.0

    net_pnl: float = 0.0

    status: str = "OPEN"