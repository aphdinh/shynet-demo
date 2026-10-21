import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    shynet_script_url = os.environ.get("SHYNET_SCRIPT_URL", "")
    return render_template("index.html", shynet_script_url=shynet_script_url)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
