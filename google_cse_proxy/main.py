from fastapi import FastAPI, HTTPException, Query
import os
import httpx

app = FastAPI(title="Google CSE Proxy")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")
if not GOOGLE_API_KEY or not GOOGLE_CSE_ID:
    raise RuntimeError("Environment vars GOOGLE_API_KEY and GOOGLE_CSE_ID must be set")

@app.get("/search")
async def search(q: str = Query(..., min_length=1), num: int = Query(10, ge=1, le=10)):
    """
    Proxy endpoint to Google Custom Search Engine.

    Query parameters:
    - q: search query string
    - num: number of results (1-10)
    """
    params = {
        "key": GOOGLE_API_KEY,
        "cx": GOOGLE_CSE_ID,
        "q": q,
        "num": num,
    }
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get("https://www.googleapis.com/customsearch/v1", params=params)
            resp.raise_for_status()
            return resp.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
