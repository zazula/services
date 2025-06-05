from fastapi import FastAPI

app = FastAPI(
    title="OpenAPI Service",
    description="Hosts OpenAPI specs and documentation.",
    docs_url="/docs",
    openapi_url="/openapi.json"
)


@app.get("/", summary="Health check")
async def root():
    return {"message": "OpenAPI Service is running."}