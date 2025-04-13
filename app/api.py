from flask import Flask, jsonify, request
from app.task import read_and_write_tweet
from app.db import init_db  

app = Flask(__name__)
init_db()

@app.route("/scrape", methods=["POST"])
def scrape_tweet():
    """
    Endpoint to scrape a tweet from the URL query parameter.
    Example Usage: 
        curl -X POST http://localhost:5001/scrape   -H "Content-Type: application/json"   -d '{"url": "http://x.com/elonmusk/status/1910204495360843813"}'
        curl -X POST http://localhost:5000/scrape   -H "Content-Type: application/json"   -d '{"url": "https://x.com/elonmusk/status/1911201291730034760"}'
        curl -X POST http://localhost:5000/scrape   -H "Content-Type: application/json"   -d '{"url": "https://x.com/realDonaldTrump/status/1908300360810479821"}'        
    """
    url = request.json.get("url")  # Grab URL from JSON body

    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    result = read_and_write_tweet(url)
    
    if result:
        return jsonify({"message": "Tweet scraped successfully", "data": result}), 200
    else:
        return jsonify({"error": "Failed to scrape tweet"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
