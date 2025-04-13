from .scraper import scrape_tweet
from .db import check_schema, write_tweet
from datetime import datetime
from typing import Optional

def read_and_write_tweet(url: str):
    """
    Read a tweet from the given URL and write it to the database.
    """
    results = scrape_tweet(url)
    core = results.get("core")
    legacy = results.get("legacy")

    if not core or not legacy:
        return None

    user_name = core.get("user_results").get("result").get("legacy").get("name")
    full_text = legacy.get("full_text")
    
    favourites_count = core.get("user_results").get("result").get("legacy").get("favourites_count")
    
    print(f"favourites_count: {favourites_count}")
    
    write_tweet(user_name, full_text)
    
    return user_name, full_text

# Example usage:
# url = "http://x.com/elonmusk/status/1910204495360843813"
# read_and_write_tweet(url)