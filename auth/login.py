import os
import webbrowser
from pathlib import Path

from dotenv import load_dotenv, set_key
from flask import Flask, request
from kiteconnect import KiteConnect

# -----------------------
# Load .env
# -----------------------

ENV_FILE = Path(".env")

load_dotenv(ENV_FILE)

API_KEY = os.getenv("KITE_API_KEY")
API_SECRET = os.getenv("KITE_API_SECRET")

if not API_KEY or not API_SECRET:
    raise RuntimeError(
        "KITE_API_KEY or KITE_API_SECRET not found in .env"
    )

kite = KiteConnect(api_key=API_KEY)

app = Flask(__name__)


@app.route("/login")
def login():

    request_token = request.args.get("request_token")

    if not request_token:
        return "Request Token not received."

    try:

        session = kite.generate_session(
            request_token,
            api_secret=API_SECRET,
        )

        access_token = session["access_token"]

        kite.set_access_token(access_token)

        # Save to .env
        set_key(
            str(ENV_FILE),
            "KITE_ACCESS_TOKEN",
            access_token,
        )

        profile = kite.profile()

        return f"""
        <h2>Login Successful</h2>

        <p>Welcome {profile['user_name']}</p>

        <p>Access Token saved to .env</p>

        <h3>You may close this browser window.</h3>
        """

    except Exception as e:

        return f"<h3>Login Failed</h3><pre>{e}</pre>"


if __name__ == "__main__":

    print("Opening Zerodha Login...")

    webbrowser.open(kite.login_url())

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
    )