from flask import Flask, jsonify, request
from .task import read_and_write_tweet
from .db import init_db  

app = Flask(__name__)
init_db()

@app.route("/scrape", methods=["POST"])
def scrape_tweet():
    """
    Endpoint to scrape a tweet from a given URL.
    Expects a JSON payload with the URL.
    """
    data = request.get_json()
    url = data.get("url")
    
    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    result = read_and_write_tweet(url)
    
    if result:
        return jsonify({"message": "Tweet scraped successfully", "data": result}), 200
    else:
        return jsonify({"error": "Failed to scrape tweet"}), 500
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
