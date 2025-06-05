# OpenAPI Service

This service hosts the OpenAPI specification and interactive API docs.

Endpoints:
- `GET /` — health check
- `GET /docs` — Swagger UI
- `GET /openapi.json` — raw OpenAPI spec

Run locally:
```bash
curl http://localhost:${OPENAPI_SERVICE_PORT:-5003}/
```

Extend `main.py` to add additional API routes.