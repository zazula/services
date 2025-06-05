# MCP Service

This service implements the Model Context Protocol (MCP).
It exposes two endpoints:

- `GET /tools` — returns a list of available tools.
- `POST /invoke` — invokes a named tool with parameters.

Usage:
```bash
curl -X GET http://localhost:${MCP_SERVICE_PORT:-5002}/tools
curl -X POST http://localhost:${MCP_SERVICE_PORT:-5002}/invoke \
     -H 'Content-Type: application/json' \
     -d '{"tool":"tool1","params":{...}}'
```

Extend `main.py` to wire up real tool implementations.