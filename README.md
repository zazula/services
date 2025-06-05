# Infrastructure Services

This repository contains five independently-deployable services:

1. **Puppeteer Service**
   - Runs a browserless Chrome instance accessible via the DevTools Protocol.
   - Default host port: 3000 (override via \\`PUPPETEER_PORT\\` env var).

2. **Google CSE Proxy**
3. **MCP Service**
   - Implements the Model Context Protocol (MCP).
   - Default host port: 5002 → container port 8000 (override via `MCP_SERVICE_PORT`).

4. **OpenAPI Service**
   - Hosts the OpenAPI specification and interactive docs.
   - Default host port: 5003 → container port 8000 (override via `OPENAPI_SERVICE_PORT`).

5. **Pipeline Service**
   - Provides a generic `/run` endpoint to execute custom workflows.
   - Default host port: 5004 → container port 8000 (override via `PIPELINE_SERVICE_PORT`).
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
   - MCP Service: http://localhost:${MCP_SERVICE_PORT:-5002}/tools (or /invoke)
   - OpenAPI Service: http://localhost:${OPENAPI_SERVICE_PORT:-5003}/
   - Pipeline Service: http://localhost:${PIPELINE_SERVICE_PORT:-5004}/run
