from flask import Flask, jsonify, request
from .scraper import scrape_tweet
from .db import SessionLocal, Tweet, init_db

app = Flask(__name__)
init_db()

@app.route("/scrape", methods=["POST"])
def scrape_and_store():
    data = request.get_json()
    tweet_url = data.get("url")

    if not tweet_url:
        return jsonify({"error": "No tweet URL provided"}), 400

    try:
        tweet_data = scrape_tweet(tweet_url)
        db = SessionLocal()
        tweet = Tweet(
            username=tweet_data['core']['user_results']['result']['legacy']['screen_name'],
            content=tweet_data['legacy']['full_text']
        )
        db.add(tweet)
        db.commit()
        db.close()
        return jsonify({"status": "success", "tweet": tweet_data['legacy']['full_text']})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
