# Defines how your app container is built (Linux base, Python, dependencies)	
# When you need a custom app image with system & Python packages
# Think of it like setting up your dev machine, but for your app.

FROM python:3.11-slim

# Install system dependencies for Playwright
RUN apt-get update && apt-get install -y \
    wget curl unzip fonts-liberation libappindicator3-1 \
    libasound2 libatk-bridge2.0-0 libatk1.0-0 libcups2 libdbus-1-3 \
    libgdk-pixbuf2.0-0 libnspr4 libnss3 libxcomposite1 libxdamage1 \
    libxrandr2 xdg-utils libu2f-udev libvulkan1 libxss1 \
    libgtk-3-0 libgbm-dev libxshmfence-dev xvfb && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Git and SSH client
RUN apt-get update && apt-get install -y \
git openssh-client \
&& apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python packages + browser deps
RUN pip install --no-cache-dir playwright && playwright install --with-deps

WORKDIR /app

COPY . .

CMD ["python", "-m", "app.api"]
