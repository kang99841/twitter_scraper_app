Prompt: I want to develop an app on local desktop.
Now I need your help to make it happen, as detailed as possible.
First I am using windows WSL. I want you to build my app in a docker container, so that I can deploy the web anywhere.
Also I want to use a flask api. dbeaver for conneting postgres database.
The purpose of the app is to scrape data from twitter https://scrapfly.io/blog/how-to-scrape-twitter/ and store the data in a local database.
I want to make it an app api, so that I can schedule and curl it from airflow.
Give me an overlay and then a detailed implementation plan and code sample.

Note, exit code 137 == OOM. If memory runs out, you need to go to powershell to configue wsl memory: 
1. Go powershell, enter command
notepad "$env:USERPROFILE\.wslconfig"
# LINK: https://learn.microsoft.com/en-us/windows/wsl/wsl-config#wslconfig


Installation:
pip install playwright
playwright install
sudo apt-get install libgbm1

Response:
App Functional Overview:
Scrape Twitter Data
Uses headless browser (via Playwright or API method via Scrapfly).

Store in Postgres
Save tweets in structured format.

Expose API with Flask
Flask exposes /scrape endpoint.

Dockerized
App and DB both run in containers.

DBeaver
For browsing and querying DB locally.

Triggerable via curl / Airflow
Trigger via Airflow DAG or manual curl.


Techstack:
Component	Technology
OS Environment	Windows + WSL2
API Framework	Flask
Scraping Tool	Requests + BeautifulSoup / Playwright / Scrapfly.io
Database	PostgreSQL
Database Client	DBeaver
Containerization	Docker + Docker Compose
Orchestration	Airflow
Scheduling Trigger	curl to Flask API
