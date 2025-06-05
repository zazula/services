# Infrastructure Services

This repository contains two independently-deployable services:

1. **Puppeteer Service**
   - Runs a browserless Chrome instance accessible via the DevTools Protocol.
   - Default host port: 3000 (override via \\`PUPPETEER_PORT\\` env var).

2. **Google CSE Proxy**
   - FastAPI proxy to Google Custom Search Engine.
   - Default host port: 5001 → container port 5000 (override via \\`GOOGLE_CSE_PROXY_PORT\\`).

## Setup

1. Copy \\`.env.example\\` to \\\`.env\\\` and fill in your credentials:
   \\\`\\\`bash
   cp .env.example .env
   # Edit .env:
   # GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
   # GOOGLE_CSE_ID=YOUR_GOOGLE_CSE_ID
   # PUPPETEER_PORT=3000
   # GOOGLE_CSE_PROXY_PORT=5001
   \\\`\\\` 

2. Build and start both services:
   \\\`\\\`bash
   docker-compose up --build
   \\\`\\\`

3. The services will be available at:
   - Puppeteer: http://localhost:${PUPPETEER_PORT:-3000}/json/version
   - Google CSE Proxy: http://localhost:${GOOGLE_CSE_PROXY_PORT:-5001}/search?q=example&num=5
