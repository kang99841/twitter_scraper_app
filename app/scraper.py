from playwright.sync_api import sync_playwright


def scrape_tweet(url: str) -> dict:
    """
    Scrape a single tweet page for Tweet thread e.g.:
    https://twitter.com/Scrapfly_dev/status/1667013143904567296
    Return parent tweet, reply tweets and recommended tweets
    """
    _xhr_calls = []

    def intercept_response(response):
        """capture all background requests and save them"""
        # we can extract details from background requests
        if response.request.resource_type == "xhr":
            _xhr_calls.append(response)
        return response

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)  # Change to True for Docker
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        # enable background request intercepting:
        page.on("response", intercept_response)
        # go to url and wait for the page to load
        page.goto(url)
        page.wait_for_selector("[data-testid='tweet']")

        # find all tweet background requests:
        tweet_calls = [f for f in _xhr_calls if "TweetResultByRestId" in f.url]
        for xhr in tweet_calls:
            data = xhr.json()
            return data['data']['tweetResult']['result']



if __name__ == "__main__":
    url = "http://x.com/elonmusk/status/1910204495360843813"
    results = scrape_tweet(url)
    core = results.get("core")
    legacy = results.get("legacy")
    
    print(core.get("user_results").get("result").get("legacy").get("favourites_count"))
    
    favourites_count = core.get("user_results").get("result").get("legacy").get("favourites_count")
    full_text = legacy.get("full_text")
    print(favourites_count)
    print(full_text)
    
    # git remote set-url origin git@github.com:kang99841/twitter_scraper_app.git
