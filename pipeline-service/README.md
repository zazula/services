# Pipeline Service

This service provides a "pipeline" endpoint to run custom processing or model workflows.

Endpoint:
- `POST /run` — submit a JSON payload to execute the pipeline

Example:
```bash
curl -X POST http://localhost:${PIPELINE_SERVICE_PORT:-5004}/run \
     -H 'Content-Type: application/json' \
     -d '{"foo":"bar"}'
```

Customize `main.py` with your orchestration logic.