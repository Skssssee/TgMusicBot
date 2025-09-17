import os
import threading
from flask import Flask
from bot import main  # Your main bot function

# Minimal Flask server to open port
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# Start Flask in a separate thread
threading.Thread(target=run_flask).start()

# Run your bot in the main thread
main()
