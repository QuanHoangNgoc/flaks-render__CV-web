from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/")
def home():
    return render_template("index.html")


# Ensure static files are served correctly
@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Use Render's port
    app.run(host="0.0.0.0", port=port)
