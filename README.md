# twitter_scraper_app
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
Component       Technology
OS Environment  Windows + WSL2
API Framework   Flask
Scraping Tool   Requests + BeautifulSoup / Playwright / Scrapfly.io
Database        PostgreSQL

Docker:
Open the Command Palette:
Press
Ctrl+Shift+P (Windows/Linux)

Cmd+Shift+P (macOS)

Type and select:
🔁 Dev Containers: Rebuild and Reopen in Container

(Optional clean up)
# Shut down any running containers
docker compose down --volumes --remove-orphans

# Remove dangling build cache
docker builder prune -f
Database Client DBeaver
Containerization        Docker + Docker Compose
Orchestration   Airflow
Scheduling Trigger      curl to Flask API

# Handy Docker Commands
## Docker
docker ps               # running containers
docker images           # list images
docker volume ls        # list volumes
docker volume rm <v>    # delete volume
docker exec -it <id> bash  # enter a container shell

## Compose
docker-compose up       # starts everything
docker-compose down     # stops & removes containers
docker-compose build    # (re)build containers
docker-compose logs     # logs from all services

## Dev container
# From inside VS Code
> Rebuild Container
> Reopen in Container
> Rebuild and Reopen in Container

# Pro Tip:
Use named volumes for databases, bind mounts for code.

Don't rebuild unless needed — it'll save you time.

Add a .devcontainer/.env to store shared secrets or configs.

Avoid storing Git config inside the container — use your WSL2 Git setup or bind-mount it.